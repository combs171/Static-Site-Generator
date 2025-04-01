import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestLeafNode(unittest.TestCase):

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_with_multiple_children(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "Italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		self.assertEqual(
			node.to_html(),
			"<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
		)

	def test_to_html_with_no_children(self):
		with self.assertRaises(ValueError):
			ParentNode("body", [])

	def test_nested_parent_nodes(self):
		first_child = LeafNode("b", "Bold inner text")
		first_parent = ParentNode("div", [first_child])
		first_g_parent = ParentNode("span", [first_parent, LeafNode("p", "Normal text")])
		self.assertEqual(
			first_g_parent.to_html(),
			"<span><div><b>Bold inner text</b></div><p>Normal text</p></span>",
		)

	def test_to_html_with_props(self):
		child_node = LeafNode("span", "choose your words")
		parent_node = ParentNode("div", [child_node], {"key": "value"})
		self.assertEqual(
			parent_node.to_html(),
			'<div key="value"><span>choose your words</span></div>',
		)

	def test_to_html_with_no_props(self):
		child_node = LeafNode("span", "choose your words")
		parent_node = ParentNode("div", [child_node], {})
		self.assertEqual(
			parent_node.to_html(),
			"<div><span>choose your words</span></div>",
		)

if __name__ == "__main__":
    unittest.main()
