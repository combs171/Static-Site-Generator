import os
from markdown_to_html_node import *
from extract_title import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using template '{template_path}'")

    try:
        # Open and read the Markdown file
        with open(from_path, "r", encoding="utf-8") as x_markdown:
            markdown_content = x_markdown.read()

        # Open and read the HTML template file
        with open(template_path, "r", encoding="utf-8") as x_template:
            template_content = x_template.read()

        # Convert Markdown content
        html_node = markdown_to_html_node(markdown_content)
        html_content = html_node.to_html()

        # Extract the title
        title = extract_title(markdown_content)

        # Replace placeholders with actual content in the generated HTML
        final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

        # Ensure destination directory exists
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        # Write the final HTML to the destination path
        with open(dest_path, "w", encoding="utf-8") as x_output:
            x_output.write(final_html)
        print(f"Successfully generated {dest_path}")

    except Exception as e:
        print(f"Error generating page from '{from_path}': {e}")

def traverse_and_generate(from_dir, template_path):
    for root, _, files in os.walk(from_dir):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)

                dest_path = md_path.replace("content", "public").replace(".md", ".html")

                generate_page(md_path, template_path, dest_path)

if __name__ == "__main__":
    content_dir = "content"
    template_path = "template.html"
    traverse_and_generate(content_dir, template_path)
