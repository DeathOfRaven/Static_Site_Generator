from markdown_to_html_node import markdown_to_html_node
import os
from pathlib import Path

def extract_title(markdown):
    lines = markdown.split("\n")
    found = False
    for line in lines:
        if line.startswith("# "):
            found = line
            break
    if not found:
        raise Exception("No h1 header")
    result = found[2:]
    result = result.strip()
    return result

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path, "r")
    t = open(template_path, "r")
    from_file = f.read()
    temp_file = t.read()
    from_node = markdown_to_html_node(from_file)
    from_html = from_node.to_html()
    title = extract_title(from_file)
    temp_file = temp_file.replace("{{ Title }}", title)
    temp_file = temp_file.replace("{{ Content }}", from_html)
    temp_file = temp_file.replace('href="/', f'href="{basepath}')
    temp_file = temp_file.replace('src="/', f'src="{basepath}')
    dir = os.path.dirname(dest_path)
    if dir != "":
        os.makedirs(dir, exist_ok=True)
    d = open(dest_path, "w")
    d.write(temp_file)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(full_path):
            dest_path = Path(dest_path).with_suffix(".html")
            page = generate_page(full_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(full_path, template_path, dest_path, basepath)