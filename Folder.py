import os
import re


def folder_count(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1

    return count


def rename_with_count(path):
    os.chdir(path)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            folder_full_path = os.path.join(root, name)
            folder_full_path_without_count = re.sub('\(.*?\)', '', folder_full_path)
            folder_full_path_with_count = folder_full_path_without_count + ' (' + str(folder_count(os.path.join(root, name))) + ')'

            os.rename(folder_full_path, folder_full_path_with_count)
