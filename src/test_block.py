import unittest
from block import block_to_block_type,  BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        text = "###### This is a heading"
        check = block_to_block_type(text)
        self.assertEqual(check, BlockType.HEADING)
    
    def test_code(self):
        text = "```\nthis is code\n```"
        check = block_to_block_type(text)
        self.assertEqual(check, BlockType.CODE)

    def test_quote(self):
        text = "> this is\n> a quote"
        check = block_to_block_type(text)
        self.assertEqual(check, BlockType.QUOTE)

    def test_unordered(self):
        text = "- this is\n- an unordered\n- list"
        check = block_to_block_type(text)
        self.assertEqual(check, BlockType.UNORDERED)

    def test_ordered(self):
        text = "1. this is\n2. an ordered\n3. list"
        check = block_to_block_type(text)
        self.assertEqual(check, BlockType.ORDERED)

    def test_paragraph(self):
        text = "this is just text"
        check = block_to_block_type(text)
        self.assertEqual(check, BlockType.PARAGRAPH)