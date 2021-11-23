import os
from Config import SERVICE_SYMBOLS


def delete_service_symbols(string_to_change):
    for service_symbol in SERVICE_SYMBOLS:
        string_to_change = string_to_change.replace(service_symbol, '')

    return string_to_change


def create_dir_if_not_exist(path):
    if not os.path.isdir(path):
        os.mkdir(path)

    return os.path.isdir(path)


def is_file_exists(path):
    if os.path.isfile(path):
        return True
