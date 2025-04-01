import unittest
from textnode import TextNode, TextType
from splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitter(unittest.TestCase):
	def test_split_code_block(self):
		node = TextNode("This is a `code block` example", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(
			new_nodes,
			[
				TextNode("This is a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" example", TextType.TEXT),
			],
		)

	def test_split_bold_text(self):
		node = TextNode("This is a **bold** example", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertEqual(
			new_nodes,
			[
				TextNode("This is a ", TextType.TEXT),
				TextNode("bold", TextType.BOLD),
				TextNode(" example", TextType.TEXT),
			],
		)

	def test_split_italic_text(self):
		node = TextNode("This is a _italic_ example", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
		self.assertEqual(
			new_nodes,
			[
				TextNode("This is a ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" example", TextType.TEXT),
			],
		)

	def test_split_multi_delimiters(self):
		node = TextNode("This is a _italic_ and **bold** example", TextType.TEXT)
		nodes_after_italic = split_nodes_delimiter([node], "_", TextType.ITALIC)
		new_nodes = split_nodes_delimiter(nodes_after_italic, "**", TextType.BOLD)
		self.assertEqual(
			new_nodes,
			[
				TextNode("This is a ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" and ", TextType.TEXT),
				TextNode("bold", TextType.BOLD),
				TextNode(" example", TextType.TEXT),
			],
		)

	def test_no_delimiters(self):
		node = TextNode("This is a basic example", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
		self.assertEqual(new_nodes, [node])

	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
					"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)

	def test_split_images_no_matches(self):
		node = TextNode("This is text with no images.", TextType.TEXT)
		new_nodes = split_nodes_image([node])
		self.assertListEqual([node], new_nodes)

	def test_split_links_no_matches(self):
		node = TextNode("This is text with no links.", TextType.TEXT)
		new_nodes = split_nodes_link([node])
		self.assertListEqual([node], new_nodes)

	def test_split_links(self):
		node = TextNode(
			"This is text with an [link1](https://site1.com) and another [link2](https://site2.com)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("link1", TextType.LINK, "https://site1.com"),
				TextNode(" and another ", TextType.TEXT),
				TextNode("link2", TextType.LINK, "https://site2.com"),
			],
			new_nodes,
		)

	def test_split_multi_images_and_links(self):
		node = TextNode(
			"![img1](https://img1.com) with a site [link1](https://site1.com) and another ![img2](https://img2.com) and another site [link2](https://site2.com)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image(split_nodes_link([node]))
		self.assertListEqual(
			[
				TextNode("img1", TextType.IMAGE, "https://img1.com"),
				TextNode(" with a site ", TextType.TEXT),
				TextNode("link1", TextType.LINK, "https://site1.com"),
				TextNode(" and another ", TextType.TEXT),
				TextNode("img2", TextType.IMAGE, "https://img2.com"),
				TextNode(" and another site ", TextType.TEXT),
				TextNode("link2", TextType.LINK, "https://site2.com"),
			],
			new_nodes,
		)


if __name__ == "__main__":
	unittest.main()

