# Base class representing an HTML node.
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method will be overwritten by child class")

    def props_to_html(self):
        # Converts props dict to HTML attribute string.
        if self.props is None:
            return ""

        return ''.join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        # Debug-friendly representation of the node.
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


# Represents a leaf HTML node (i.e., one without children).
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if self.tag is None:
            return self.value

        # Render as a standard HTML element with optional props.
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


# Represents an HTML node that can have children.
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag must be provided!")

        if not self.children:
            raise ValueError("Children are required for Parentnode!")

        # Recursively render all child nodes to HTML.
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
