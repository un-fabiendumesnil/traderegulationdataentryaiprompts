# helpers.py
def ocr_pdf(path):
    from pdf2image import convert_from_path
    import pytesseract, io
    pages = convert_from_path(path, dpi=300)
    return "\n".join(pytesseract.image_to_string(p) for p in pages)
