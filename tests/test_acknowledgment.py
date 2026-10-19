
import sys
from pathlib import Path
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import generate_acknowledgment


def test_assamese_name_is_preserved_in_acknowledgment_pdf():
    name = "অসমীয়াৰ নাম"

    cur = MagicMock()
    cur.fetchone.return_value = (
        "APP-001", name, "9876543210", "01/01/1960",
        "Village", "Block", "1234567890", "ABCD0123456",
        "2026-10-19", "PENDING"
    )

    pdf_bytes = generate_acknowledgment(cur, 1)

    assert pdf_bytes, "PDF should be generated"
    assert name.encode("utf-8") in pdf_bytes
