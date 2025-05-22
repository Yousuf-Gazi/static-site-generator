from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    # ParentNode
    node = ParentNode(
        tag="p",
        children=[
            LeafNode(tag="b", value="Bold text"),
            LeafNode(tag=None, value="Normal text"),
            LeafNode(tag="i", value="italic text"),
            LeafNode(tag=None, value="Normal text"),
        ],
    )
    print(node)
    print(node.to_html())

main()
