import os
from os.path import isfile
import shutil

from copystatic import copy_files_recursively
from generate_page import generate_page


dir_path_static = "./static"
dir_path_public = "./public"

from_path_dir = "./content/index.md"
template_path_dir = "./template.html"
dest_path_dir = "./public/index.html"


def main():
    # test copy_static_to_public function
    print("Deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory")
    copy_files_recursively(dir_path_static, dir_path_public)

    # generate page
    print("Generating page...")
    generate_page(from_path_dir, template_path_dir, dest_path_dir)


if __name__ == "__main__":
    main()
