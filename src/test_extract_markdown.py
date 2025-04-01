import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtract_Markdown(unittest.TestCase):
	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

	def test_extract_multiple_images(self):
		text = "![one](https://img1.com) and ![two](https://img2.com)"
		matches = extract_markdown_images(text)
		self.assertEqual(matches, [("one", "https://img1.com"), ("two", "https://img2.com")])

	def test_extract_no_match_images(self):
		text = "There is no image here!"
		matches = extract_markdown_images(text)
		self.assertEqual(matches, [])

	def test_extract_markdown_links(self):
		text = "Check this out [site](https://somesite.com)"
		matches = extract_markdown_links(text)
		self.assertEqual(matches, [("site", "https://somesite.com")])

	def test_extract_multiple_links(self):
		text = "[one](https://link1.com) and [two](https://link2.com)"
		matches = extract_markdown_links(text)
		self.assertEqual(matches, [("one", "https://link1.com"), ("two", "https://link2.com")])

	def test_extract_no_match_links(self):
		text = "There is no link here!"
		matches = extract_markdown_links(text)
		self.assertEqual(matches, [])

if __name__ == "__main__":
	unittest.main()
