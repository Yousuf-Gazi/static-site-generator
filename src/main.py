from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    # test text_node_to_html_node function
    node = TextNode("Click here", TextType.LINK, "https://example.com")
    html_node = text_node_to_html_node(node)
    node2 = TextNode("An image of a cat", TextType.IMAGE, "https://example.com/cat.jpg")
    html_node2 = text_node_to_html_node(node2)
    print(html_node.value, html_node2.value)
    print(html_node.tag, html_node2.tag)
    print(html_node.props, html_node2.props)
    print(html_node.children, html_node2.children)

main()
