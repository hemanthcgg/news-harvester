# news-harvester
Lightweight scraper to harvest latest headlines from News.
---

## Project Structure
```
bbc-news-scraper/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── config/
│   │   └── settings.py
│   │
│   ├── scrapers/
│   │   └── bbc_scraper.py
│   │
│   ├── parsers/
│   │   └── bbc_parser.py
│   │
│   ├── pipelines/
│   │   └── storage.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   └── main.py
│
├── requirements.txt
├── .env_template
├── .gitignore
└── README.md
```

---

##  Installation Setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
# source .venv/bin/activate   # On Mac/Linux

pip install -r requirements.txt
```

---