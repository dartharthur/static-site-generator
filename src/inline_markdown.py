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
