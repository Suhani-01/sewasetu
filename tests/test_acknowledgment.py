from io import BytesIO
from pypdf import PdfReader
import sys
from pathlib import Path
from unittest.mock import MagicMock

# Add the app folder to the Python path.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import generate_acknowledgment


def test_assamese_name_is_preserved_in_acknowledgment_pdf():
    # Assamese name to test.
    name = "অসমীয়াৰ নাম"

    # Create a mock database cursor.
    cur = MagicMock()

    # Return sample application data when the function fetches a database row.
    cur.fetchone.return_value = (
        "APP-001", name, "9876543210", "01/01/1960",
        "Village", "Block", "1234567890", "ABCD0123456",
        "2026-10-19", "PENDING"
    )

    # Generate the acknowledgment PDF.
    pdf_bytes = generate_acknowledgment(cur, 1)

    # Check that the PDF was generated.
    assert pdf_bytes, "PDF should be generated"

    # Extract text from the PDF.
    reader = PdfReader(BytesIO(pdf_bytes))
    pdf_text = "\n".join(
        page.extract_text() or ""
        for page in reader.pages
    )

    # Check that the Assamese name appears in the PDF text.
    assert name in pdf_text, (
        f"Assamese name missing from PDF text: {pdf_text!r}"
    )