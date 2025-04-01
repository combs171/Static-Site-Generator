import unittest
from textnode import *
from parser import *

class Test_Text_to_TextNodes(unittest.TestCase):
	def test_basic_text(self):
		text = "This is text."
		nodes = text_to_textnodes(text)
		self.assertListEqual([TextNode("This is text.", TextType.TEXT)], nodes)

	def test_combined(self):
		text = "This is **bold** and __italic__ with `code` and ![image1](https://image1.com) and [link1](https://link1.com)."
		nodes = text_to_textnodes(text)
		self.assertListEqual(
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("bold", TextType.BOLD),
				TextNode(" and ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" with ", TextType.TEXT),
				TextNode("code", TextType.CODE),
				TextNode(" and ", TextType.TEXT),
				TextNode("image1", TextType.IMAGE, "https://image1.com"),
				TextNode(" and ", TextType.TEXT),
				TextNode("link1", TextType.LINK, "https://link1.com"),
				TextNode(".", TextType.TEXT),
			],
			nodes,
		)

	def test_empty_string(self):
		text = ""
		nodes = text_to_textnodes(text)
		self.assertListEqual([], nodes)

if __name__ == "__main__":
	unittest.main()
