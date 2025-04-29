# 📋 Divar Scrapper 

A simple Python-based Divar ad scraper that automatically searches for a keyword, opens ads, retrieves phone numbers, and saves them into a CSV file.

## ✨ Features
- Human-like typing into search box.
- Randomized click and wait times to avoid detection.
- Automatically opens ads one by one and extracts phone numbers.
- Saves data into a `phones.csv` file.
- Skips ads without phone numbers.
- Designed to work smoothly with minimal setup.

## 📋 Requirements
- Python 3.7+
- Google Chrome (installed)
- ChromeDriver (matching your Chrome version)
- The following Python packages:
  - `selenium`
  - `csv` (builtin)

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/masoudv/divar-scrapper.git
cd divar-scrapper
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Make sure you have `chromedriver` installed and it matches your Chrome version.
   - [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

4. Run the script:

```bash
python divar-scrapper.py
```

or

```bash
python3 divar-scrapper.py
```

✅ **Tip:** You can change the search keyword directly in the script (`divar-scrapper.py`) inside the `human_typing()` function.

## ⚠️ Important Notes
- You must be logged in to Divar website at least once before running the scraper (the script uses Chrome profile `chrome1` to keep you logged in).
- Do not abuse scraping to avoid IP ban.
- This script is for educational purposes only.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

