import unittest
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType
from converter import text_node_to_html_node

class TestConverter(unittest.TestCase):

	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_bold(self):
		node = TextNode("Bold text", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "Bold text")

	def test_italic(self):
		node = TextNode("Italic text", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "Italic text")

	def test_code(self):
		node = TextNode("This is a code node", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "This is a code node")

	def test_link(self):
		node = TextNode("This is a link", TextType.LINK, "https://www.google.com")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "This is a link")
		self.assertEqual(html_node.props, {"href": "https://www.google.com"})

	def test_IMAGE(self):
		node = TextNode("Image description", TextType.IMAGE, "https://www.google.com/image.jpg")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props, {"src": "https://www.google.com/image.jpg", "alt": "Image description"})

	def test_invalid_input(self):
		node = TextNode("Unknown type", "unknown type")
		with self.assertRaises(ValueError):
			text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
