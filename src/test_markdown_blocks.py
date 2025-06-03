import unittest

from markdown_blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
)


class TestMarkdownToHTML(unittest.TestCase):
    # test markdown_to_blocks function
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_with_empty_blocks(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    # test block_to_block_types function
    def test_block_to_block_types_heading_code_quote(self):
        heading_md = "# Heading\n## Another heading"
        self.assertEqual(block_to_block_type(heading_md), BlockType.HEADING)
        code_md = "```\ndef hello():\n    return 'world'\n```"
        self.assertEqual(block_to_block_type(code_md), BlockType.CODE)
        quote_md = "> Line one of quote\n> Line two of quote\n> Line three"
        self.assertEqual(block_to_block_type(quote_md), BlockType.QUOTE)

    def test_block_to_block_types_unorderd_list_ordered_list_paragraph(self):
        unordered_list_md = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(unordered_list_md), BlockType.UNORDERED_LIST)
        ordered_list_md = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(ordered_list_md), BlockType.ORDERED_LIST)
        paragraph_md = "This is the first line of the paragraph.\nThis is the second line, still the same paragraph.\nAnd here's the third line continuing the thought."
        self.assertEqual(block_to_block_type(paragraph_md), BlockType.PARAGRAPH)

    # test markdown_to_html_node function
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
