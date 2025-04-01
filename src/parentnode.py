from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		if tag is None:
			raise ValueError("ParentNode must have a tag.")
		if not children or not isinstance(children, list):
			raise ValueError("ParentNode must have a list of children")

		super().__init__(tag=tag, value=None, children=children, props=props or {})

	def to_html(self):
		if self.tag is None:
			raise ValueError("ParentNode needs tag to render to HTML")
		if not self.children:
			raise ValueError("ParentNode needs a child to render to HTML")

		props_str = self.props_to_html()

		children_html = "".join(child.to_html() for child in self.children)

		if props_str:
			return f"<{self.tag} {props_str}>{children_html}</{self.tag}>"
		else:
			return f"<{self.tag}>{children_html}</{self.tag}>"

	def __repr__(self):
		return f"HTMLNode(tag={self.tag}, children={self.children}, props={self.props})"
