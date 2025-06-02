import unittest

from markdown_blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
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

if __name__ == "__main__":
    unittest.main()
