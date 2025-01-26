import unittest

from markdown_blocks import markdown_to_blocks, is_heading


class TestBlockMarkdown(unittest.TestCase):
    def test_create_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        expected_blocks = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"]
        result = markdown_to_blocks(markdown)
        self.assertEqual(expected_blocks, result)

    def test_is_heading(self):
        # Valid headings
        self.assertTrue(is_heading("# Simple heading"))
        self.assertTrue(is_heading("# Simple heading"))
        self.assertTrue(is_heading("###### Level 6 heading"))
        self.assertTrue(is_heading("# Heading with # in middle"))
        self.assertTrue(is_heading("# Heading #"))

        # Invalid headings
        self.assertFalse(is_heading("####### Too many #'s"))
        self.assertFalse(is_heading("####### Too many #'s"))
        self.assertFalse(is_heading("#No space"))
        self.assertFalse(is_heading("# Heading # #"))
        self.assertFalse(is_heading("# Heading  #  #"))


if __name__ == "__main__":
    unittest.main()
