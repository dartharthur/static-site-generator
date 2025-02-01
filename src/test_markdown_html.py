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
            "<ol><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ol>"
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
            "<ol><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ol>"
            "<pre><code>"
            "\n"
            'x = "Hello, world"'
            "\n"
            "</code></pre>"
            "</div>"
        )
        self.assertEqual(expected_markup, actual_markup)

    def test_create_html_six_block(self):
        self.maxDiff = None
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

Here is a paragraph with a [link](https://boot.dev).

Here is a paragraph with an ![image](https://i.imgur.com/zjjcJKZ.png).

* This is the **first** list item in a list block
* This is a list item
* This is another list item

1. This is the first list item in a list block
2. This is a list item
3. This is another list item

```
x = "Hello, world"
```

> Here is the first line of a quote
> and here is the second line of the quote"""

        html_node = markdown_to_html_node(markdown)
        actual_markup = html_node.to_html()
        expected_markup = (
            "<div>"
            "<h1>This is a heading</h1>"
            "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
            '<p>Here is a paragraph with a <a href="https://boot.dev">link</a>.</p>'
            '<p>Here is a paragraph with an <img src="https://i.imgur.com/zjjcJKZ.png" alt="image"></img>.</p>'
            "<ul><li>This is the <b>first</b> list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul>"
            "<ol><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ol>"
            "<pre><code>"
            "\n"
            'x = "Hello, world"'
            "\n"
            "</code></pre>"
            "<blockquote>Here is the first line of a quote and here is the second line of the quote</blockquote>"
            "</div>"
        )
        self.assertEqual(expected_markup, actual_markup)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
