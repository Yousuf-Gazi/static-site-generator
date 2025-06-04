import os
from os.path import isfile
import shutil

from copystatic import copy_files_recursively


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    # test copy_static_to_public function
    print("Deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory")
    copy_files_recursively(dir_path_static, dir_path_public)


if __name__ == "__main__":
    main()
