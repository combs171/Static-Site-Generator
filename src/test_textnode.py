import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_with_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://somewebsite.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://somewebsite.com")
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a link", TextType.LINK, None)
        node2 = TextNode("This is a link", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_dif_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://somewebsite.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://difwebsite.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
