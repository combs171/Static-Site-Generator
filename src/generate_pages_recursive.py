import os
from generate_page import *

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	for entry in os.listdir(dir_path_content):
		entry_path = os.path.join(dir_path_content, entry)
		dest_entry_path = os.path.join(dest_dir_path, entry)

		if os.path.isfile(entry_path) and entry_path.endswith(".md"):
			dest_file_path = dest_entry_path.replace(".md", ".html")
			os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
			generate_page(entry_path, template_path, dest_file_path)

		elif os.path.isdir(entry_path):
			os.makedirs(dest_entry_path, exist_ok=True)
			generate_pages_recursive(entry_path, template_path, dest_entry_path)
