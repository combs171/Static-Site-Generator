import unitttest
from extract_title import *

class TestExtractTitle(self):
	def test_valid_title(self):
		self.assertEqual(extract_title("# Some Title"), "Some Title")

	def test_white_space(self):
		self.assertEqual(extract_title("#   Spaced Title   "), "Spaced Title")

	def test_no_title(self):
		md = "# Title1\n## Subtitle\n# Title2"
		self.assertEqual(extract_title(md), "Title1")

	def test_multi_headings(self):
		with self.assertRaises(ValueError):
			extract_title("## No h1 here")
