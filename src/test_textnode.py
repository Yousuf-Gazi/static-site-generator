import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is another text node", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is another text node", TextType.ITALIC, "Italic text")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("check text url", TextType.IMAGE, None)
        node2 = TextNode("check text url", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("Text A", TextType.CODE, "print('hello world')")
        node2 = TextNode("Text B", TextType.CODE, "print('hello world')")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Testing __repr__ method", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(
            repr(node), "TextNode(Testing __repr__ method, link, https://www.boot.dev)"
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_link(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        # node2 = TextNode("An image of a cat", TextType.IMAGE, "https://example.com/cat.jpg")
        # html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_text_node_to_html_node_image(self):
        node = TextNode("An image of a cat", TextType.IMAGE, "https://example.com/cat.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {
                'src': 'https://example.com/cat.jpg',
                'alt': 'An image of a cat'
            }
        )


if __name__ == "__main__":
    unittest.main()
