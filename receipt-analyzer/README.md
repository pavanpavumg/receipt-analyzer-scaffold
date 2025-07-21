# Receipt Analyzer – Full Stack Python Project

## Features
- Upload and extract data from receipts (.jpg, .png, .pdf)
- OCR-based parsing using Tesseract
- Store parsed data in SQLite
- Search, sort, and aggregate bills
- Streamlit dashboard to view insights

## Setup

```bash
git clone https://github.com/yourusername/receipt-analyzer.git
cd receipt-analyzer
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python main.py
streamlit run frontend/app.py
```

## Folder Structure
- `backend/`: ingestion, OCR parsing, algorithms
- `frontend/`: Streamlit UI
- `models/`: data schemas with Pydantic
- `data/`: uploads and SQLite DB
