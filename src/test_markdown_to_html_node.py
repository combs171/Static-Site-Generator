import unittest
from markdown_to_html_node import *

class TestMarkdownToHtmlNode(unittest.TestCase):
	def test_paragraphs(self):
		md = """
	This is **bolded** paragraph
	text in a p
	tag here

	This is another paragraph with __italic__ text and `code` here

	"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
		)

	def test_codeblock(self):
		md = """
	```
	This is text that _should_ remain
	the **same** even with inline stuff
	```
	"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
		)

	def test_heading(self):
		md = "# Heading 1"
		node = markdown_to_html_node(md)
		self.assertEqual(node.to_html(), "<div><h1>Heading 1</h1></div>")

	def test_quote(self):
		md = """
	> This is a quote
	> with multiple lines
	"""
		node = markdown_to_html_node(md)
		self.assertEqual(node.to_html(), "<div><blockquote>This is a quote with multiple lines</blockquote></div>")

	def test_unordered(self):
		md = """
	- Item 1
	- Item 2
	- Item 3
	"""
		node = markdown_to_html_node(md)
		self.assertEqual(node.to_html(), "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>")

	def test_ordered(self):
		md = """
	1. First
	2. Second
	3. Third
	"""
		node = markdown_to_html_node(md)
		self.assertEqual(node.to_html(), "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>")

if __name__ == "__main__":
	unittest.main()
