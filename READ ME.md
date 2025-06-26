# Text to PDF Converter for Google Docs

This project provides a Python tool to automatically download a Google Docs document, split it into chapters, and export each chapter as a separate, well-formatted PDF file.

## Features

- Downloads Google Docs as plain text using the document's share link.
- Splits the document into chapters based on headings like `1. Chapter Title`.
- Cleans and organizes chapter content.
- Converts each chapter into a separate PDF with clean margins and text wrapping.
- Handles multi-page output and safe filenames.
- Simple command-line interface.

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [reportlab](https://pypi.org/project/reportlab/)

Install dependencies with:

```sh
pip install requests reportlab
```

## Usage

1. Make sure both `doctopdf.py` and `pdfwriter.py` (with the `text_to_pdf` function) are in the same folder.
2. Run the script:

```sh
python doctopdf.py
```

3. Follow the prompts:
   - Paste your Google Docs share link (must be viewable by "Anyone with the link").
   - Enter the output directory for the PDFs (leave blank for current folder).

Each chapter will be saved as a separate PDF in the chosen directory.

### Example

```
Paste your Google Docs link: https://docs.google.com/document/d/1aBcD.../edit?usp=sharing
✅ Extracted Doc ID: 1aBcD...
✅ Document downloaded successfully.
['1. Introduction\nThis is the intro...', '2. Chapter Two\nContent...']
Enter directory to save PDFs (leave blank for current folder):
✅ Saved: Introduction.pdf
✅ Saved: Chapter Two.pdf

✅ All chapters exported as PDFs to: C:\Users\gokul\doctopdfauto
```

## How It Works

- Extracts the document ID from your Google Docs link.
- Downloads the document as plain text.
- Splits the text into chapters using headings like `1. ...`, `2. ...`, etc.
- Cleans up chapter titles and content.
- Uses the `text_to_pdf` function to convert each chapter to a PDF.

## Error Handling

- Invalid Google Docs links will show an error.
- If the document is not accessible, you will see a status code error.
- Chapters without titles are skipped.
- Temporary files are cleaned up automatically.

## File Structure

- `doctopdf.py` – Main script for downloading, splitting, and converting chapters.
- `pdfwriter.py` or `dtop.py` – Contains the `text_to_pdf` function for PDF conversion.

## License

This project is provided for educational purposes.

---

**Author:**  
Gokul Soundarapandian