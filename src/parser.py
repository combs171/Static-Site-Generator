from textnode import *
from splitter import *

def text_to_textnodes(text):
	intial_node = TextNode(text, TextType.TEXT)
	nodes = [intial_node]

	nodes = split_nodes_image(nodes)
	nodes = split_nodes_link(nodes)
	nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
	nodes = split_nodes_delimiter(nodes, "__", TextType.ITALIC)
	nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

	return nodes
