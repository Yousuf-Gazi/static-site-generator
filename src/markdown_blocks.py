from enum import Enum
from htmlnode import (
    LeafNode,
    ParentNode,
)
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes


# Enum representing various block types in markdown (e.g., heading, paragraph, code).
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


# Converts markdown into a list of blocks (divided by paragraph breaks).
def markdown_to_blocks(markdown):
    # Split based on blank lines (paragraphs).
    blocks = markdown.split("\n\n")

    cleaned_blocks = []
    for block in blocks:
        if block == "":
            continue

        stripped_block = block.strip()
        cleaned_blocks.append(stripped_block)

    return cleaned_blocks


# Determines the block type (heading, paragraph, code, etc.) for a given markdown block.
def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        order = 1
        for line in lines:
            if not line.startswith(f"{order}. "):
                return BlockType.PARAGRAPH
            order += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


# Converts markdown text to an HTML node by processing all blocks within the markdown.
def markdown_to_html_node(markdown):
    # Split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        # Convert each block to HTML node
        html_node = block_to_html_node(block)
        children.append(html_node)
    # Wrap all nodes in a parent div
    return ParentNode(tag="div", children=children)


# Converts a single markdown block to its corresponding HTML node.
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ul_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ol_to_html_node(block)
    raise ValueError("invalid block type")


# Converts text into a list of child nodes, each representing a segment of formatted text.
def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode(tag="p", children=children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    
    # Ensure heading is properly formatted
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")

    # Extract the heading text
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(tag=f"h{level}", children=children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")

    # Strip the code block markers (```)
    text = block[4:-3]
    raw_text_node = TextNode(text=text, text_type=TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode(tag="code", children=[child])
    return ParentNode(tag="pre", children=[code])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode(tag="blockquote", children=children)


def ul_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        # Remove the '- ' prefix
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode(tag="li", children=children))
    return ParentNode(tag="ul", children=html_items)


def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        # Remove the '1. ' prefix
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode(tag="li", children=children))
    return ParentNode(tag="ol", children=html_items)
