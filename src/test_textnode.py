import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_NotEqual(self):
        node = TextNode("some text", TextType.BOLD)
        node2 = TextNode("some text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_URL(self):
        node = TextNode("some text", TextType.BOLD)
        node2= TextNode("some text", TextType.BOLD, "https://youtube.com")
        self.assertNotEqual(node, node2)
    


if __name__ == "__main__":
    unittest.main()