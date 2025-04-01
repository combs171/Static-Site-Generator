import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        expected_output = 'href="https://www.google.com" target="_blank"'
       	self.assertEqual (node.props_to_html(), expected_output)

    def test_empty_props(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_empty_node(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

if __name__ == "__main__":
    unittest.main()
