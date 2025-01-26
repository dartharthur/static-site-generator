import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    is_heading,
    is_code,
    is_quote,
    is_unordered_list,
    is_ordered_list,
    BLOCK_TYPE_PARAGRAPH,
    BLOCK_TYPE_HEADING,
    BLOCK_TYPE_CODE,
    BLOCK_TYPE_QUOTE,
    BLOCK_TYPE_UNORDERED_LIST,
    BLOCK_TYPE_ORDERED_LIST,
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

    def test_is_heading(self):
        self.assertTrue(is_heading("# Simple heading"))
        self.assertTrue(is_heading("# Simple heading"))
        self.assertTrue(is_heading("###### Level 6 heading"))
        self.assertTrue(is_heading("# Heading with # in middle"))
        self.assertTrue(is_heading("# Heading #"))
        self.assertTrue(is_heading("# Heading # #"))
        self.assertTrue(is_heading("# Heading  #  #"))

        self.assertFalse(is_heading("####### Too many #'s"))
        self.assertFalse(is_heading("#No space"))

    def test_is_code(self):
        self.assertTrue(is_code("```\nsome code\n```"))
        self.assertTrue(is_code("```\n```"))
        
        self.assertFalse(is_code("```\ncode with ``` inside\n```"))
        self.assertFalse(is_code("some text ```\ncode\n```"))
        self.assertFalse(is_code("```\ncode\n``` extra"))
        self.assertFalse(is_code("``\ncode\n``"))
        self.assertFalse(is_code("````\ncode\n````"))
        self.assertFalse(is_code("```\ncode"))
        self.assertFalse(is_code("```"))
        self.assertFalse(is_code("```\ncode\n```\n```\nmore code\n```"))

    def test_is_quote(self):
        self.assertTrue(is_quote(">Simple quote"))
        self.assertTrue(is_quote("> Quote with space after >"))
        self.assertTrue(is_quote(">Quote with>special>characters"))
        
        self.assertTrue(is_quote(">First line\n>Second line"))
        self.assertTrue(is_quote(">One\n>Two\n>Three"))
        self.assertTrue(is_quote("> Spaced\n> Multiple\n> Lines"))
        
        self.assertFalse(is_quote("Regular text"))
        self.assertFalse(is_quote(">First line\nSecond line"))
        self.assertFalse(is_quote("Text\n>Quote"))
        self.assertFalse(is_quote(""))
        self.assertFalse(is_quote("\n"))
        self.assertFalse(is_quote(">"))
    
    def test_is_unordered_list(self):
        self.assertTrue(is_unordered_list("* First item"))
        self.assertTrue(is_unordered_list("- First item"))
        self.assertTrue(is_unordered_list("* One\n* Two\n* Three"))
        self.assertTrue(is_unordered_list("- One\n- Two\n- Three"))
        self.assertTrue(is_unordered_list("* Item with * in text"))
        self.assertTrue(is_unordered_list("- Item with - in text"))
        self.assertTrue(is_unordered_list("* Item with spaces after marker"))
        self.assertTrue(is_unordered_list("*    Multiple spaces after marker"))

        self.assertFalse(is_unordered_list(""))
        self.assertFalse(is_unordered_list("*No space after marker"))
        self.assertFalse(is_unordered_list("-No space after marker"))
        self.assertFalse(is_unordered_list("* First line\nSecond line"))
        self.assertFalse(is_unordered_list("Text\n* List"))
        # self.assertFalse(is_unordered_list("* ")) todo: fix
        # self.assertFalse(is_unordered_list("*")) todo: fix
        self.assertFalse(is_unordered_list("Regular text"))
        self.assertFalse(is_unordered_list("1. Ordered list item"))

    def test_is_ordered_list(self):
        self.assertTrue(is_ordered_list("1. First"))
        self.assertTrue(is_ordered_list("1. First\n2. Second"))
        self.assertTrue(is_ordered_list("1. First\n2. Second\n3. Third"))

        self.assertFalse(is_ordered_list(""))
        self.assertFalse(is_ordered_list("1 First"))
        self.assertFalse(is_ordered_list("2. First"))
        self.assertFalse(is_ordered_list("1. First\n3. Third"))
        self.assertFalse(is_ordered_list("1. First\n1. Second"))
        self.assertFalse(is_ordered_list("1.First"))

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_QUOTE)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
