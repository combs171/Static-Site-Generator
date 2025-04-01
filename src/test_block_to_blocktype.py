import unittest
from blocktype import BlockType
from block_to_blocktype import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
	def test_heading(self):
		self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
		self.assertEqual(block_to_block_type("### Heading 2"), BlockType.HEADING)
		self.assertEqual(block_to_block_type("##### Heading 3"), BlockType.HEADING)

	def test_code_block(self):
		self.assertEqual(block_to_block_type("```\nprint('abc123')\n```"), BlockType.CODE)

	def test_quote_block(self):
		self.assertEqual(block_to_block_type("> So say\n> you"), BlockType.QUOTE)

	def test_unordered_list(self):
		self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

	def test_ordered_list(self):
		self.assertEqual(block_to_block_type("1. First thing\n2. Second thing"), BlockType.ORDERED_LIST)

	def test_paragraph(self):
		self.assertEqual(block_to_block_type("Paragraph text"), BlockType.PARAGRAPH)

if __name__ == "__main__":
	unittest.main()
