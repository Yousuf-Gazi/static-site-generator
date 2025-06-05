import os

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:]
            return title
    raise ValueError("invalid markdown: there's no title in the markdown")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read markdown and tempalte file and stor those into variable
    with (
        open(from_path, "r") as from_path_file,
        open(template_path, "r") as template_path_file,
    ):
        markdown_file = from_path_file.read()
        template_file = template_path_file.read()

    # convert markdown -> HTML string
    html_node = markdown_to_html_node(markdown_file)
    html_string = html_node.to_html()

    # extracting title from the markdown
    title = extract_title(markdown_file)

    # replace title and content placeholder with actual title and content in the template file
    full_html_page = (
            template_file
            .replace("{{ Title }}", title)
            .replace("{{ Content }}", html_string)
    )

    # write full HTML page to dest_path and also create if dir needed or dont exist
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as html_file:
        html_file.write(full_html_page)
