# PDF Form Data Extractor & Summary Generator

This project extracts data from a filled PDF form (`Form ADT-1-29092023_signed.pdf`), outputs the extracted fields as a structured JSON file (`output.json`), and generates a plain English summary using an LLM (Groq API).

## Requirements

- Python 3.8 or higher
- All dependencies are listed in `requirements.txt`.

## Installation

1. **Clone or download this repository.**
2. **Install the required Python packages:**

```bash
pip install -r requirements.txt
```

## Usage

### 1. Extract Data from PDF

1. Place your filled PDF form as `Form ADT-1-29092023_signed.pdf` in the project directory (or update the filename in `extractor.py`).
2. Run the extractor script:

```bash
python extractor.py
```

- This will create `output.json` with the extracted data.

### 2. Generate a Summary

1. Create a `.env` file in the project directory and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

2. Run the summary generator script:

```bash
python summary_generator.py
```

- This will create `summary.txt` with a plain English summary of the extracted data.

## File Descriptions

- `extractor.py` — Extracts form data from the PDF and saves it as `output.json`.
- `output.json` — The extracted structured data from the PDF.
- `summary_generator.py` — Uses the Groq LLM to generate a summary from `output.json` and saves it as `summary.txt`.
- `summary.txt` — The generated summary in plain English.
- `.env` — Stores your Groq API key (not included by default).
- `requirements.txt` — Lists all required Python packages.
