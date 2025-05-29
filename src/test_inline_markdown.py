import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)


class TestInlineMarkdown(unittest.TestCase):
    # test split nodes delimiter function
    def test_markdown_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ],
            new_nodes
        )

    def test_markdown_delimiter_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes
        )

    def test_markdown_delimiter_bold_double(self):
        node = TextNode("This is text with a **bolded word** and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD)
            ],
            new_nodes
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    # test extract_markdown_images function
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                (
                    "image",
                    "https://i.imgur.com/zjjcJKZ.png"
                )
            ],
            matches
        )

    def test_extract_markdown_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            matches
        )

    # test extract_markdown_links function
    def test_extract_markdown_links(self):
            text = "Visit [Open AI](https://openai.com)"
            matches = extract_markdown_links(text)
            self.assertListEqual(
                [
                    (
                        "Open AI",
                        "https://openai.com"
                    )
                ],
                matches
            )

    def test_extract_markdown_multiple_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ],
            matches
        )

    # test split_nodes_image function
    def test_split_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
        node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                )
            ],
            new_nodes
        )

    def test_split_images_starts_ends_with_image(self):
        text = "![start](https://example.com/start.png) some text in the middle ![end](https://example.com/end.png)"
        node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("start", TextType.IMAGE, "https://example.com/start.png"),
                TextNode(" some text in the middle ", TextType.TEXT),
                TextNode("end", TextType.IMAGE, "https://example.com/end.png")
            ],
            new_nodes
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images_multiple_nodes(self):
        text = "![start](https://example.com/start.png) some text in the middle ![end](https://example.com/end.png)"
        node = TextNode(text, TextType.TEXT)

        text2 = "![logo](https://example.com/logo.png) Welcome to the site"
        node2 = TextNode(text2, TextType.TEXT)

        text3 = "Here is the image ![chart](https://example.com/chart.png)"
        node3 = TextNode(text3, TextType.TEXT)

        new_nodes = split_nodes_image([node, node2, node3])
        self.assertListEqual(
            [
                TextNode("start", TextType.IMAGE, "https://example.com/start.png"),
                TextNode(" some text in the middle ", TextType.TEXT),
                TextNode("end", TextType.IMAGE, "https://example.com/end.png"),
                TextNode("logo", TextType.IMAGE, "https://example.com/logo.png"),
                TextNode(" Welcome to the site", TextType.TEXT),
                TextNode("Here is the image ", TextType.TEXT),
                TextNode("chart", TextType.IMAGE, "https://example.com/chart.png")
            ],
            new_nodes
        )

    # test split_nodes_link function
    def test_split_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ],
            new_nodes
        )

    def test_split_links_starts_ends_with_link(self):
        text = "[start link](https://example.com/start) some text [end link](https://example.com/end)"
        node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("start link", TextType.LINK, "https://example.com/start"),
                TextNode(" some text ", TextType.TEXT),
                TextNode("end link", TextType.LINK, "https://example.com/end")
            ],
            new_nodes
        )

    def test_split_link_single(self):
        node = TextNode(
            "[docs](https://docs.example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("docs", TextType.LINK, "https://docs.example.com"),
            ],
            new_nodes,
        )

    def test_split_links_multiple_nodes(self):
        text = "[start link](https://example.com/start) some text [end link](https://example.com/end)"
        node = TextNode(text, TextType.TEXT)

        text2 = "[home](https://example.com) is where the heart is"
        node2 = TextNode(text2, TextType.TEXT)

        text3 = "Check this out [here](https://example.com)"
        node3 = TextNode(text3, TextType.TEXT)

        new_nodes = split_nodes_link([node, node2, node3])
        self.assertListEqual(
            [
                TextNode("start link", TextType.LINK, "https://example.com/start"),
                TextNode(" some text ", TextType.TEXT),
                TextNode("end link", TextType.LINK, "https://example.com/end"),
                TextNode("home", TextType.LINK, "https://example.com"),
                TextNode(" is where the heart is", TextType.TEXT),
                TextNode("Check this out ", TextType.TEXT),
                TextNode("here", TextType.LINK, "https://example.com")
            ],
            new_nodes
        )


if __name__ == "__main__":
    unittest.main()
