from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter


def main():
    # test inline_markdown delimiter
    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    print(new_nodes)

main()
