from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
)


def main():
    # test test_markdown_to_blocks function
    # md = "## This is a **bold** heading with _italic_ text"
#     md = """
# This is **bolded** paragraph
# text in a p
# tag here
#
# This is another paragraph with _italic_ text and `code` here
#
# """
#     md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """
    md = """
> This is a quote with **bold text** and _italic text_
> It can also have `code` and even links
> Multiple lines are all part of the same quote
"""
#     md = """
# 1. First item with **bold text**
# 2. Second item with _italic text_
# 3. Third item with `code` and more text
# """
    blocks = markdown_to_html_node(md)
    print(blocks.to_html())

main()
