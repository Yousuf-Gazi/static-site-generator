import os
from os.path import isfile
import shutil
import sys

from copystatic import copy_files_recursively
from generate_page import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    # get base_path from CLI args, default to "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print("Deleting docs directory")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    
    print("Copying static files to docs directory")
    copy_files_recursively(dir_path_static, dir_path_docs)

    # generate page
    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_docs,
        basepath,
    )


if __name__ == "__main__":
    main()
