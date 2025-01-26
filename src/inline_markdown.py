import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        # Clever technique here
        # If you split on the delimiter:
        #   - You know that the values in the odd numbered indices are wrapped by the delimiter
        #       - Also works in the case where the whole string is wrapped: `code`.split('`') --> ['', 'code', '']
        #   - You know that if the split list length is even, we're missing a closing delimiter
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for idx, val in enumerate(sections):
            if val == "":
                continue
            if idx % 2 == 0:
                split_nodes.append(TextNode(val, TextType.TEXT))
            else:
                split_nodes.append(TextNode(val, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        split_nodes = []
        remaining_text = old_node.text
        links = extract_markdown_images(remaining_text)
        if not links:
            new_nodes.append(old_node)
            continue
        for alt_text, image_url in links:
            first_section_text, second_section_text = remaining_text.split(f"![{alt_text}]({image_url})", 1)
            if first_section_text:
                split_nodes.append(TextNode(first_section_text, TextType.TEXT))
            split_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            remaining_text = second_section_text
        if remaining_text:
            split_nodes.append(TextNode(remaining_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        split_nodes = []
        remaining_text = old_node.text
        links = extract_markdown_links(remaining_text)
        if not links:
            new_nodes.append(old_node)
            continue
        for link_text, link_url in links:
            first_section_text, second_section_text = remaining_text.split(f"[{link_text}]({link_url})", 1)
            if first_section_text:
                new_nodes.append(TextNode(first_section_text, TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            remaining_text = second_section_text
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes
