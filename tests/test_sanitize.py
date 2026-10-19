
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import sanitize


def test_assamese_name_is_preserved():
    name = "অসমীয়াৰ নাম"

    result = sanitize(name)

    print("Original:", repr(name))
    print("Result:  ", repr(result))
    print("Original bytes:", len(name.encode("utf-8")))

    assert result == name