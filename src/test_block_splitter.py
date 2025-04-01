import unittest
from block_splitter import *

class TestBlockSplitter(unittest.TestCase):
	def test_markdown_to_blocks(self):
		md = """
	This is **bolded** paragraph

	This is another paragraph with _italic_ text and `code` here
	This is the same paragraph on a new line

	- This is a list
	- with items
	"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
				"- This is a list\n- with items",
			],
		)

	def test_empty_string(self):
		blocks = markdown_to_blocks("")
		self.assertEqual(blocks, [])

	def test_multi_newlines(self):
		md = """
	Block 1

	Block 2



	Block 3



	"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(blocks, ["Block 1", "Block 2", "Block 3"])

if __name__ == "__main__":
	unittest.main()
