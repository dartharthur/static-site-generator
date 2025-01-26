import re

PARAGRAPH = "paragraph"
HEADING = "heading"
CODE = "code"
QUOTE = "quote"
UNORDERED_LIST = "unordered_list"
ORDERED_LIST = "ordered_list"

def is_paragraph(block):
    return False

def is_heading(block):
    pattern = r"^#{1,6}\s[^#].*$|^#{1,6}\s.*[^#\s]#*\s*$"
    return bool(re.match(pattern, block))

def is_code(block):
    return False

def is_quote(block):
    return False

def is_unordered_list(block):
    return False

def is_ordered_list(block):
    return False

block_handler_map = {
    PARAGRAPH: is_paragraph,
    HEADING: is_heading
}

def markdown_to_blocks(markdown):
    # blocks = markdown.split("\n\n")
    # filtered_blocks = []
    # for block in blocks:
    #     if block == "":
    #         continue
    #     block = block.strip()
    #     filtered_blocks.append(block)
    # return filtered_blocks
    return [block for block in markdown.split("\n\n") if block.strip()]

def block_to_block_type(block):
    return block
