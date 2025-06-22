# PDF Form Data Extractor

This project extracts data from a filled PDF form (`Form ADT-1-29092023_signed.pdf`) and outputs the extracted fields as a structured JSON file (`output.json`).

## Requirements

- Python 3.7 or higher
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (also known as `pymupdf`)

## Installation

1. **Clone or download this repository.**
2. **Install the required Python package:**

```bash
pip install pymupdf
```

## Usage

1. Place your filled PDF form as `Form ADT-1-29092023_signed.pdf` in the project directory (or update the filename in `extractor.py`).
2. Run the extractor script:

```bash
python extractor.py
```

3. After execution, the extracted data will be saved in `output.json` in the same directory.

## Output

- `output.json`: Contains the extracted and organized form data in JSON format.

## Notes

- You can modify the `key_mapping` dictionary in `extractor.py` to change which PDF fields are extracted and how they are named in the output.
- The script is currently set up for the specific structure of the provided PDF form. For other forms, you may need to adjust the field names and logic.

## License

This project is for educational and demonstration purposes.
