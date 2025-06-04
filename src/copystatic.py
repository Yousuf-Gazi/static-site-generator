import os
from os.path import isfile
import shutil


def copy_files_recursively(src_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    src_path_list = os.listdir(src_dir_path)
    for file in src_path_list:
        src_path = os.path.join(src_dir_path, file)
        dest_path = os.path.join(dest_dir_path, file)
        print(f" * {src_path} -> {dest_path}")

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            copy_files_recursively(src_path, dest_path)
