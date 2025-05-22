import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode 


class TestHTMLNode(unittest.TestCase): 
    def test_similar(self): 
        node = HTMLNode("span", "this is span") 
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "this is span")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        child1 = HTMLNode("span", "Child 1")
        child2 = HTMLNode("image", "Child 2")
        parent = HTMLNode(
            "div", "this is div", [child1, child2], {"class": "wrapper"}
        )
        self.assertEqual(
            repr(parent), "HTMLNode(div, this is div, children: [HTMLNode(span, Child 1, children: None, None), HTMLNode(image, Child 2, children: None, None)], {'class': 'wrapper'})"
        )

    def test_props_to_html(self):
        child1 = HTMLNode("span", "Child 1")
        child2 = HTMLNode("image", "Child 2")
        parent = HTMLNode(
            "div",
            "this is div",
            [child1, child2],
            {
                "class": "wrapper",
                "target": "_blank"
            }
        )
        self.assertEqual(
            parent.props_to_html(), ' class="wrapper" target="_blank"'
        )

    # test for LeafNode
    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode(tag="a", value="Click me!", props={
            "href": "https://www.google.com"
        })
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="This is no tag value raw data.")
        self.assertEqual(node.to_html(), "This is no tag value raw data.")

    # test for ParentNode
    def test_to_html_with_children(self):
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(tag="b", value="grandchild")
        child_node = ParentNode(tag="span", children=[grandchild_node])
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_many_children(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_heading(self):
        node = ParentNode(
            tag="h1",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h1><b>Bold text</b>Normal text<i>italic text</i>Normal text</h1>"
        )



if __name__ == "__main__":
    unittest.main()
