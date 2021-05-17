"""
Name: utilities.py
Purpose: File which contains the utilities of the program - Validators and others.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""
import os

INPUT_FILES_INDEX = 1
EXTENSION_INDEX = 1


def refactor_tuple(tup):
    stringed_tup = str(tup)
    stringed_tup = stringed_tup.replace('\'', '')
    return stringed_tup


def remove_file(filepath):
    os.remove(filepath)


def validate_types(supported_types):
    """
    Decorator which validates types inputted in the input folder.
    :param supported_types: Supplied supported extensions.
    :return: function object.
    """
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            obj, files_list = args
            for f in files_list:
                _, fileextension = os.path.splitext(f)
                if fileextension[EXTENSION_INDEX:] not in supported_types:
                    remove_file(f)
                    files_list.pop(files_list.index(f))
            newargs = obj, files_list
            return func(*newargs, **kwargs)
        return wrapper
    return outer_wrapper


def validate_folders(folders_list):
    """
    Checks if log and input folder exists - generic function.
    :param folders_list: Folders list
    :return: None
    """
    for path in folders_list:
        if not os.path.exists(path):
            os.makedirs(path)
