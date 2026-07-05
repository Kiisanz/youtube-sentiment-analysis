# YouTube Sentiment Analysis

This repository contains a Python project for analyzing sentiment in YouTube comments. Using the VADER sentiment analysis tool from NLTK, it classifies comments into positive, neutral, and negative categories. The results are visualized with Seaborn and Matplotlib to provide clear insights into public opinion on specific videos.

The dataset used is sourced from Kaggle and includes YouTube comments with usernames. This project demonstrates data preprocessing, sentiment scoring, and professional-quality visualization suitable for academic assignments or beginner data science portfolios.

## Features

- Reads YouTube comments from an Excel file
- Accepts CSV comment exports with `comment`, `comments`, or Xquik-style `text` columns
- Performs sentiment analysis with VADER (NLTK)
- Categorizes comments into Positive, Neutral, and Negative
- Visualizes sentiment distribution with polished bar charts
- Saves the results with sentiment labels back to Excel

## Repository Structure

- `data/` : stores the original comment data files
- `notebooks/` : sentiment analysis notebooks
- `scripts/` : Python scripts (optional)
- `requirements.txt` : list of required libraries

## Installation

1. Clone this repository
2. Install required dependencies:
  `pip install -r requirements.txt`
  
3. Run notebook file `notebooks/sentiment_analysis.ipynb` in Jupyter Lab/Notebook.
   
## Usage

1. Prepare your Excel or CSV file with comment text:

   * Column A: Username
   * Column B: Comment text
   * Or a headered CSV with `comment`, `comments`, or `text`

2. Run the Jupyter Notebook `sentiment_analysis.ipynb` step by step.

3. The script will output:

   * A new Excel file with sentiment labels added
   * A professional bar chart showing sentiment distribution

## Dataset Source

The YouTube comments dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/faiqkhoirulmuna/indonesias-vice-president-youtube-comment). Please ensure you have the rights to use the data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Mochamad Rifki Maulana
