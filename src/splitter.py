from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []

	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue

		x = node.text.split(delimiter)

		if len(x) % 2 == 0:
			raise ValueError(f"Invalid syntax: {delimiter} != delimiter.")

		z = False
		for y in x:
			if y:
				node_type = text_type if z else TextType.TEXT
				new_nodes.append(TextNode(y, node_type))
			z = not z
	return new_nodes

def split_nodes_image(old_nodes):
	new_nodes = []

	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue

		text = node.text
		matches = extract_markdown_images(text)

		if not matches:
			new_nodes.append(node)
			continue

		for alt_text, url in matches:
			sections = text.split(f"![{alt_text}]({url})", 1)
			if sections[0]:
				new_nodes.append(TextNode(sections[0], TextType.TEXT))
			new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
			text = sections[1] if len(sections) > 1 else ""


		if text:
			new_nodes.append(TextNode(text, TextType.TEXT))

	return new_nodes

def split_nodes_link(old_nodes):
	new_nodes = []

	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue

		text = node.text
		matches = extract_markdown_links(text)

		if not matches:
			new_nodes.append(node)
			continue

		for anchor_text, url in matches:
			sections = text.split(f"[{anchor_text}]({url})", 1)
			if sections[0]:
				new_nodes.append(TextNode(sections[0], TextType.TEXT))
			new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
			text = sections[1] if len(sections) > 1 else ""

		if text:
			new_nodes.append(TextNode(text, TextType.TEXT))

	return new_nodes
