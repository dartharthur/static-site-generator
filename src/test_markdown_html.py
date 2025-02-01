import unittest

from markdown_html import markdown_to_html_node


class TestMarkdownHTML(unittest.TestCase):
    def test_create_html_one_block(self):
        markdown = "# This is a heading"
        html_node = markdown_to_html_node(markdown)
        actual_markup = html_node.to_html()
        expected_markup = "<div><h1>This is a heading</h1></div>"
        self.assertEqual(expected_markup, actual_markup)

    def test_create_html_two_block(self):
        markdown = """# This is a heading

* This is the **first** list item in a list block
* This is a list item
* This is another list item"""

        html_node = markdown_to_html_node(markdown)
        actual_markup = html_node.to_html()
        expected_markup = (
            "<div>"
            "<h1>This is a heading</h1>"
            "<ul><li>This is the <b>first</b> list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul>"
            "</div>"
        )
        self.assertEqual(expected_markup, actual_markup)

    def test_create_html_three_block(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the **first** list item in a list block
* This is a list item
* This is another list item"""

        html_node = markdown_to_html_node(markdown)
        actual_markup = html_node.to_html()
        expected_markup = (
            "<div>"
            "<h1>This is a heading</h1>"
            "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
            "<ul><li>This is the <b>first</b> list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul>"
            "</div>"
        )
        self.assertEqual(expected_markup, actual_markup)

    def test_create_html_four_block(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the **first** list item in a list block
* This is a list item
* This is another list item

1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""

        html_node = markdown_to_html_node(markdown)
        actual_markup = html_node.to_html()
        expected_markup = (
            "<div>"
            "<h1>This is a heading</h1>"
            "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
            "<ul><li>This is the <b>first</b> list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul>"
            "<ol><li>1. This is the first list item in a list block</li><li>2. This is a list item</li><li>3. This is another list item</li></ol>"
            "</div>"
        )
        self.assertEqual(expected_markup, actual_markup)

    def test_create_html_five_block(self):
        self.maxDiff = None
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the **first** list item in a list block
* This is a list item
* This is another list item

1. This is the first list item in a list block
2. This is a list item
3. This is another list item

```
x = "Hello, world"
```"""

        html_node = markdown_to_html_node(markdown)
        actual_markup = html_node.to_html()
        expected_markup = (
            "<div>"
            "<h1>This is a heading</h1>"
            "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
            "<ul><li>This is the <b>first</b> list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul>"
            "<ol><li>1. This is the first list item in a list block</li><li>2. This is a list item</li><li>3. This is another list item</li></ol>"
            "<pre><code>"
            "\n"
            'x = "Hello, world"'
            "\n"
            "</code></pre>"
            "</div>"
        )
        self.assertEqual(expected_markup, actual_markup)
