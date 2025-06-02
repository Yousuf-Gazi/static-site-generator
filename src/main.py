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
)


def main():
    # test test_markdown_to_blocks function
    md = "1. First item\n2. Second item\n3. Third item"
    block_type = block_to_block_type(md)
    print(block_type)

main()
