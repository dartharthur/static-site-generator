import re

BLOCK_TYPE_PARAGRAPH = "paragraph"
BLOCK_TYPE_HEADING = "heading"
BLOCK_TYPE_CODE = "code"
BLOCK_TYPE_QUOTE = "quote"
BLOCK_TYPE_UNORDERED_LIST = "unordered_list"
BLOCK_TYPE_ORDERED_LIST = "ordered_list"

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
    if not block:
        return False
    return all((line.startswith('* ') or line.startswith("- ")) for line in block.splitlines())

def is_ordered_list(block):
    if not block:
        return False
    line_count = 1
    for line in block.splitlines():
        beg = line[:3]
        if beg != f"{line_count}. ":
            return False
        line_count += 1
    return True

block_handler_map = {
    BLOCK_TYPE_HEADING: is_heading,
    BLOCK_TYPE_CODE: is_code,
    BLOCK_TYPE_QUOTE: is_quote,
    BLOCK_TYPE_UNORDERED_LIST: is_unordered_list,
    BLOCK_TYPE_ORDERED_LIST: is_ordered_list,
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
    return BLOCK_TYPE_PARAGRAPH

# Alternative, simpler approach
# def block_to_block_type(block):
#     lines = block.split("\n")

#     if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
#         return block_type_heading
#     if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
#         return block_type_code
#     if block.startswith(">"):
#         for line in lines:
#             if not line.startswith(">"):
#                 return block_type_paragraph
#         return block_type_quote
#     if block.startswith("* "):
#         for line in lines:
#             if not line.startswith("* "):
#                 return block_type_paragraph
#         return block_type_ulist
#     if block.startswith("- "):
#         for line in lines:
#             if not line.startswith("- "):
#                 return block_type_paragraph
#         return block_type_ulist
#     if block.startswith("1. "):
#         i = 1
#         for line in lines:
#             if not line.startswith(f"{i}. "):
#                 return block_type_paragraph
#             i += 1
#         return block_type_olist
#     return block_type_paragraph
