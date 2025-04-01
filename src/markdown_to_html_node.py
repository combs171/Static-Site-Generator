from htmlnode import *
from textnode import *
from blocktype import *
from block_splitter import *
from block_to_blocktype import *
from converter import *
from parser import *
from parentnode import *

def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)

	block_nodes = []

	for block in blocks:
		block_type = block_to_block_type(block)

		if block_type == BlockType.PARAGRAPH:
			block_nodes.append(create_paragraph(block))

		elif block_type == BlockType.HEADING:
			block_nodes.append(create_heading(block))

		elif block_type == BlockType.CODE:
			block_nodes.append(create_code_block(block))

		elif block_type == BlockType.QUOTE:
			block_nodes.append(create_quote(block))

		elif block_type == BlockType.UNORDERED_LIST:
			block_nodes.append(create_unordered_list(block))

		elif block_type == BlockType.ORDERED_LIST:
			block_nodes.append(create_ordered_list(block))

	return ParentNode("div", block_nodes)

def text_to_children(text):
	normalized_text = " ".join(text.split())
	text_nodes = text_to_textnodes(normalized_text)
	return [text_node_to_html_node(node) for node in text_nodes]

def create_paragraph(block):
	children = text_to_children(block)
	return ParentNode("p", children)

def create_heading(block):
	count = 0
	for x in block:
		if x == "#":
			count +=1
		else:
			break
	content = block[count + 1:]
	children = text_to_children(content)
	return ParentNode(f"h{count}", children)

def create_code_block(block):
	code_content = block[4:-3]
	code_node = LeafNode("code", code_content)
	return ParentNode("pre", [code_node])

def create_quote(block):
	lines = [line[1:].strip() for line in block.splitlines()]
	quote_text = " ".join(lines)
	children = text_to_children(quote_text)
	return ParentNode("blockquote", children)

def create_unordered_list(block):
	items = [line[2:].strip() for line in block.splitlines()]
	list_items = [ParentNode("li", text_to_children(item)) for item in items]
	return ParentNode("ul", list_items)

def create_ordered_list(block):
	items = [line.split(". ", 1)[1].strip() for line in block.splitlines()]
	list_items = [ParentNode("li", text_to_children(item)) for item in items]
	return ParentNode("ol", list_items)

