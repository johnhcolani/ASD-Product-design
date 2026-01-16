try:
    from PIL import Image
    print("PIL/Pillow available")
except ImportError:
    print("PIL/Pillow not available")

try:
    import pytesseract
    print("pytesseract (OCR) available")
except ImportError:
    print("pytesseract (OCR) not available")
