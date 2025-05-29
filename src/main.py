from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)


def main():
    # test split_nodes_link function
    text2 = "[home](https://example.com) is where the heart is"
    node2 = TextNode(text2, TextType.TEXT)
    new_nodes = split_nodes_link([node2])
    print(new_nodes)

    # test split_nodes_image function
    # text = "![start](https://example.com/start.png) some text in the middle ![end](https://example.com/end.png)"
    # node = TextNode(text, TextType.TEXT)
    # new_nodes = split_nodes_image([node])
    # print(new_nodes)

main()
