from textnode import TextNode, TextType
from generate_page import *
from generate_pages_recursive import *
import os
import shutil


def delete_directory(directory):
	if os.path.exists(directory):
		print(f"About to delete: {directory}")
		shutil.rmtree(directory)
	else:
		print(f"Directory '{directory}' does not exist, skipping deletion.")

def copy_directory(src, dst):
	if not os.path.exists(src):
		print(f"The source directory '{src}' does not exist.")
		return

	os.makedirs(dst, exist_ok=True)

	for entries in os.listdir(src):
		src_path = os.path.join(src, entries)
		dst_path = os.path.join(dst, entries)

		if os.path.isfile(src_path):
			shutil.copy2(src_path, dst_path)

		else:
			copy_directory(src_path, dst_path)

def main():
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Print current working directory for debugging
    print("Current working directory:", current_dir)
    
    # Look inside the static_site_gen directory
    print("Contents of static_site_gen directory:")
    print(os.listdir(current_dir))
    
    # Try to construct the path to the content directory
    content_path = os.path.join(current_dir, "content")
    
    # Check if it exists
    if not os.path.exists(content_path):
        print(f"Error: Content directory not found at {content_path}")
        return

    if not os.path.exists("public"):
        os.makedirs("public")

    for entry in os.listdir("public"):
        entry_path = os.path.join("public", entry)
        if os.path.isfile(entry_path) or entry not in ("blog", "contact"):
            if os.path.isdir(entry_path):
                shutil.rmtree(entry_path)
            else:
                os.remove(entry_path)

    copy_directory("static", "public")

    generate_pages_recursive(content_path, "template.html", "public")

if __name__ == "__main__":
	main()
