import unittest

from markdown_blocks import (
    markdown_to_blocks,
    is_heading,
    is_code,
    is_quote
)


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

    def test_is_heading_block(self):
        # Valid headings
        self.assertTrue(is_heading("# Simple heading"))
        self.assertTrue(is_heading("# Simple heading"))
        self.assertTrue(is_heading("###### Level 6 heading"))
        self.assertTrue(is_heading("# Heading with # in middle"))
        self.assertTrue(is_heading("# Heading #"))
        self.assertTrue(is_heading("# Heading # #"))
        self.assertTrue(is_heading("# Heading  #  #"))

        # Invalid headings
        self.assertFalse(is_heading("####### Too many #'s"))
        self.assertFalse(is_heading("#No space"))

    def test_is_code_block(self):
        # Valid code blocks
        self.assertTrue(is_code("```\nsome code\n```"))
        self.assertTrue(is_code("```\n```"))  # Empty code block
        
        # Invalid code blocks
        self.assertFalse(is_code("```\ncode with ``` inside\n```"))
        self.assertFalse(is_code("some text ```\ncode\n```"))
        self.assertFalse(is_code("```\ncode\n``` extra"))
        self.assertFalse(is_code("``\ncode\n``"))  # Only 2 backticks
        self.assertFalse(is_code("````\ncode\n````"))  # 4 backticks
        self.assertFalse(is_code("```\ncode"))  # Missing closing
        self.assertFalse(is_code("```"))  # Just backticks
        self.assertFalse(is_code("```\ncode\n```\n```\nmore code\n```"))  # Multiple blocks

    def test_quote_block(self):
        # Valid quotes - single line
        self.assertTrue(is_quote(">Simple quote"))
        self.assertTrue(is_quote("> Quote with space after >"))
        self.assertTrue(is_quote(">Quote with>special>characters"))
        
        # Valid quotes - multiple lines
        self.assertTrue(is_quote(">First line\n>Second line"))
        self.assertTrue(is_quote(">One\n>Two\n>Three"))
        self.assertTrue(is_quote("> Spaced\n> Multiple\n> Lines"))
        
        # Invalid quotes
        self.assertFalse(is_quote("Regular text"))
        self.assertFalse(is_quote(">First line\nSecond line"))  # Missing > on second line
        self.assertFalse(is_quote("Text\n>Quote"))  # First line not quote
        self.assertFalse(is_quote(""))  # Empty string
        self.assertFalse(is_quote("\n"))  # Just newline
        self.assertFalse(is_quote(">"))  # Just >


if __name__ == "__main__":
    unittest.main()
