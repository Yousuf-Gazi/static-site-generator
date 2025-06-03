from enum import Enum
from htmlnode import (
    LeafNode,
    ParentNode,
)
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    cleaned_blocks = []
    for block in blocks:
        if block == "":
            continue

        stripped_block = block.strip()
        cleaned_blocks.append(stripped_block)

    return cleaned_blocks


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
    
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")

    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(tag=f"h{level}", children=children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")

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
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode(tag="li", children=children))
    return ParentNode(tag="ul", children=html_items)


def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode(tag="li", children=children))
    return ParentNode(tag="ol", children=html_items)


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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode(tag="div", children=children)
