import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

	def test_leaf_to_html_no_tag(self):
		node = LeafNode(None, "Some text.")
		self.assertEqual(node.to_html(), "Some text.")

	def test_leaf_to_html_special_char(self):
		node = LeafNode("p", "<Hello>, world!")
		self.assertEqual(node.to_html(), "<p><Hello>, world!</p>")

	def test_leaf_no_value(self):
		with self.assertRaises(ValueError):
			LeafNode("p", None)

if __name__ == "__main__":
    unittest.main()
