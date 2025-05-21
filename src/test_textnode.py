import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
