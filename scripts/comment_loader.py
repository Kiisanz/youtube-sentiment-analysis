from pathlib import Path

import pandas as pd


COMMENT_COLUMN_ALIASES = (
    "komentar",
    "comment",
    "comments",
    "text",
    "content",
    "message",
    "body",
)
USERNAME_COLUMN_ALIASES = ("username", "user", "author", "screenname", "name")


def _find_column(columns, aliases):
    normalized_columns = {str(column).strip().lower(): column for column in columns}
    for alias in aliases:
        if alias in normalized_columns:
            return normalized_columns[alias]
    return None


def normalize_comment_dataframe(dataframe):
    comment_column = _find_column(dataframe.columns, COMMENT_COLUMN_ALIASES)
    username_column = _find_column(dataframe.columns, USERNAME_COLUMN_ALIASES)

    if comment_column is None and len(dataframe.columns) >= 2:
        username_column = dataframe.columns[0]
        comment_column = dataframe.columns[1]
    elif comment_column is None and len(dataframe.columns) == 1:
        comment_column = dataframe.columns[0]

    if comment_column is None:
        raise ValueError("Input data must include a comment or text column.")

    normalized = pd.DataFrame(
        {
            "Username": (
                dataframe[username_column]
                if username_column in dataframe.columns
                else [""] * len(dataframe)
            ),
            "Komentar": dataframe[comment_column],
        }
    )
    normalized["Komentar"] = normalized["Komentar"].fillna("").astype(str).str.strip()
    normalized["Username"] = normalized["Username"].fillna("").astype(str).str.strip()

    return (
        normalized[normalized["Komentar"] != ""]
        .drop_duplicates(subset=["Username", "Komentar"])
        .reset_index(drop=True)
    )


def load_comment_dataframe(path):
    comment_path = Path(path)
    suffix = comment_path.suffix.lower()

    if suffix == ".csv":
        raw_dataframe = pd.read_csv(comment_path)
    elif suffix in (".xls", ".xlsx"):
        raw_dataframe = pd.read_excel(comment_path, header=None)
    else:
        raise ValueError("Use a CSV, XLS, or XLSX comment file.")

    return normalize_comment_dataframe(raw_dataframe)
