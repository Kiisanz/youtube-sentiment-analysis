import tempfile
import unittest
from pathlib import Path

import pandas as pd

from scripts.comment_loader import load_comment_dataframe, normalize_comment_dataframe


class CommentLoaderTest(unittest.TestCase):
    def test_normalizes_two_column_excel_shape(self):
        dataframe = pd.DataFrame([["ann", "Great explanation"], ["bob", ""]])

        normalized = normalize_comment_dataframe(dataframe)

        self.assertEqual(normalized.to_dict("records"), [{"Username": "ann", "Komentar": "Great explanation"}])

    def test_loads_xquik_text_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "comments.csv"
            csv_path.write_text(
                "createdAt,text,author\n2026-07-05,Useful context,ann\n2026-07-05, ,bob\n",
                encoding="utf-8",
            )

            normalized = load_comment_dataframe(csv_path)

        self.assertEqual(normalized["Komentar"].tolist(), ["Useful context"])

    def test_rejects_unsupported_file_type(self):
        with self.assertRaisesRegex(ValueError, "CSV, XLS, or XLSX"):
            load_comment_dataframe(Path("comments.json"))


if __name__ == "__main__":
    unittest.main()
