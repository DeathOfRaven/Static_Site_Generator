import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extraction(self):
        text = "# This is a title\nthis is random other text\nso is this"
        result = extract_title(text)
        self.assertEqual(result, "This is a title")