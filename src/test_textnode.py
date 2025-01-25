import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, TextType.TEXT, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_html(self):
        text_node = TextNode("this is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            text_node.text, html_node.value
        )

    def test_img_to_html(self):
        text_node = TextNode("this is a text node for an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            f' src="{text_node.url}" alt="{text_node.text}"', html_node.props_to_html()
        )

if __name__ == "__main__":
    unittest.main()
