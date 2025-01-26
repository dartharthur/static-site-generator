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
    # ^ start of string
    # #{1,6} one to six # characters
    # \s+ at least one whitespace character
    # .+ at least one of any character
    # $ end of string
    pattern = r"^#{1,6}\s+.+$"
    return bool(re.match(pattern, block))

def is_code(block):
    split_block = block.split("```")
    if len(split_block) != 3:
        return False
    if split_block[0] != "" or split_block[2] != "":
        return False
    return True

def is_quote(block):
    if not block or block == ">":
        return False
    return all(line.startswith('>') for line in block.splitlines())

def is_unordered_list(block):
    return False

def is_ordered_list(block):
    return False

block_handler_map = {
    PARAGRAPH: is_paragraph,
    HEADING: is_heading,
    CODE: is_code,
    QUOTE: is_quote,
    UNORDERED_LIST: is_unordered_list,
    ORDERED_LIST: is_ordered_list,
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
    for block_type, handler in block_handler_map.items():
        if handler(block):
            return block_type
    raise ValueError("Unkown block type")
