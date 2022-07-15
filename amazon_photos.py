#!/usr/bin/env python3

import os
import shutil
from typing import Union
from pathlib import Path
import argparse
from sys import stderr

class AsError(Exception):
    pass

def get_directory_size(directory: str, size: str = None) -> Union[int, str]:
    """Returns the `directory` size in bytes."""
    sizes = ['B', 'KB', 'MB', 'GB']
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file() and str(entry).startswith('.'):
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        total = os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        raise AsError("[ERROR] You don't have permissions to access this folder")
    if size in sizes:
        mul = sizes.index(size)
        return total/(mul*1000)
    elif size == None:
        return total
    else :
        raise AsError("[ERROR] Size is incorrect, please select a valid size (B, KB, MB, GB).")


def separate_videos(source_path: Path, final_path: Path) -> None:
    video_extension = ('.MP4', '.AVI', '.MKV', '.FLV', '.MOV', '.WMV', '.DIVX', '.H.264')
    if get_directory_size(source_path, 'MB') == 0:
        raise AsError("[ERROR] Directory is empty, try with another directory")
    if not final_path.is_dir():
        os.mkdir(final_path)
    os.mkdir(os.path.join(final_path,'fotos'))
    os.mkdir(os.path.join(final_path,'videos'))
    for root, dirs, files in os.walk(source_path):
        for name in files:
            if '.JPG' in name:
                dir_name = ''.join(root.split('/')[1:])
                file_path = os.path.join(root, name)
                if not os.path.exists(os.path.join(final_path+'/fotos', dir_name)):
                    os.mkdir(os.path.join(final_path+'/fotos', dir_name))
                dest_path = os.path.join(f"{final_path}/fotos/{dir_name}", name)
                shutil.move(file_path, dest_path)
            if name.endswith(video_extension) or (name.upper()).endswith(video_extension):
                dir_name = ''.join(root.split('/')[1:])
                file_path = os.path.join(root, name)
                if not os.path.exists(os.path.join(final_path+'/videos', dir_name)):
                    os.mkdir(os.path.join(final_path+'/videos', dir_name))
                dest_path = os.path.join(f"{final_path}/videos/{dir_name}", name)
                shutil.move(file_path, dest_path)

def compare_items(folder1: str, folder2: str) -> bool:
    files_not_counted = ['.DS_Store']
    files1 = []
    files2 = []
    for root, dirs, files in os.walk(folder1):
        for name in files:
            if name not in files_not_counted:
                files1.append(name)
    for root, dirs, files in os.walk(folder2):
        for name in files:
            if name not in files_not_counted:
                files2.append(name) 
    return len(files1)==len(files2)

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Separate photos and videos from one folder and it's subfolder",
    )
    parser.add_argument(
        'source',
        type=Path,
        help='Source directory or file'
    )
    parser.add_argument(
        'destination',
        type=Path,
        help='Destination directory or file'
    )

    return parser.parse_args()

def main():
    args = cli()
    try:
        separate_videos(args.source, args.destination)
    except AsError as e:
        print(e, file = stderr)
        exit(1)

if __name__ == '__main__':
    main()
    