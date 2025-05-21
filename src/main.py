from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode


def main():
    # TextNode
    # node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # print(node)

    # HTMLNode
    # child1 = HTMLNode("span", "Child 1")
    # child2 = HTMLNode("image", "Child 2")
    # parent = HTMLNode(
    #     "div", "this is div", [child1, child2], {"class": "wrapper", "target": "_blank"}
    # )
    # print(parent)
    # print(parent.props_to_html())

    # LeafNode
    leaf_node = LeafNode(tag="a", value="Click me!", props={
        "href": "https://www.google.com"
    })
    print(leaf_node)
    print(leaf_node.to_html())

main()
