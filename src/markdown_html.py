from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode

from markdown_inline import text_to_textnodes

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BLOCK_TYPE_PARAGRAPH,
    BLOCK_TYPE_HEADING,
    BLOCK_TYPE_CODE,
    BLOCK_TYPE_QUOTE,
    BLOCK_TYPE_UNORDERED_LIST,
    BLOCK_TYPE_ORDERED_LIST,
)


def text_to_html_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
    return html_nodes

def block_type_paragraph_to_html_node(block):
    text = " ".join(block.split("\n")).lstrip(" ")
    p_child_nodes = text_to_html_children(text)
    p_html_node = ParentNode("p", p_child_nodes)
    return p_html_node

def block_type_heading_to_html_node(block):
    hashes, text = "".join(block.strip().splitlines()).split(" ", 1)
    hash_count = len(hashes)
    tag = f"h{hash_count}"
    heading_html_node = LeafNode(tag, text)
    return heading_html_node

def block_type_code_to_html_node(block):
    code_child_nodes = text_to_html_children(block)
    code_html_node = ParentNode("pre", code_child_nodes)
    return code_html_node

def block_type_quote_to_html_node(block):
    lines = block.strip().splitlines()
    quote_text = " ".join([text.lstrip("> ") for text in lines])
    quote_child_nodes = text_to_html_children(quote_text)
    quote_html_node = ParentNode("blockquote", quote_child_nodes)
    return quote_html_node

def block_type_unordered_list_to_html_node(block):
    lines = block.strip().splitlines()
    list_items_text = [text[2:] for text in lines]
    list_items_child_nodes = [text_to_html_children(text) for text in list_items_text]
    list_items_parent_nodes = [ParentNode("li", li_child_node) for li_child_node in list_items_child_nodes]
    unordered_list_html_node = ParentNode("ul", list_items_parent_nodes)
    return unordered_list_html_node

def block_type_ordered_list_to_html_node(block):
    numbered_lines = block.strip().splitlines()
    list_items_text = [line[3:] for line in numbered_lines]
    list_items_child_nodes = [text_to_html_children(text) for text in list_items_text]
    list_items_parent_nodes = [ParentNode("li", li_child_node) for li_child_node in list_items_child_nodes]
    ordered_list_html_node = ParentNode("ol", list_items_parent_nodes)
    return ordered_list_html_node

block_to_html_node_handler_map = {
    BLOCK_TYPE_PARAGRAPH: block_type_paragraph_to_html_node,
    BLOCK_TYPE_HEADING: block_type_heading_to_html_node,
    BLOCK_TYPE_CODE: block_type_code_to_html_node,
    BLOCK_TYPE_QUOTE: block_type_quote_to_html_node,
    BLOCK_TYPE_UNORDERED_LIST: block_type_unordered_list_to_html_node,
    BLOCK_TYPE_ORDERED_LIST: block_type_ordered_list_to_html_node,
}

def block_to_html_node(block, block_type):
    block_to_html_node_handler = block_to_html_node_handler_map[block_type]
    return block_to_html_node_handler(block)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    markdown_html_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_html_node = block_to_html_node(block, block_type)
        markdown_html_children.append(block_html_node)
    markdown_html_node = ParentNode("div", markdown_html_children)
    return markdown_html_node
