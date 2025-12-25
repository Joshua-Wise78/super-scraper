import json
import os

STORAGE_INFO = {"dir": "storage", "file": "sites.json"}

FILE_PATH = os.path.join(STORAGE_INFO["dir"], STORAGE_INFO["file"])


def save_to_json(key, value):
    """
    TODO:
        1. Add abilities to manage multiple files & directories
            for the capabilities of scraping/storing multiple sites at once.
        2. Needs more robust error handling with unique messages per error and
            maybe traceback logs.

    """
    if not os.path.exists(STORAGE_INFO["dir"]):
        os.makedirs(STORAGE_INFO["dir"])

    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("File is empty or broken starting fresh.")
            data = {}
    else:
        print("File is empty initalize file.")
        data = {}

    data[key] = value

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return True


def retrieve_from_json(key):
    """
    NOTE:
        Not finished needs testing and tweaks.
    """
    if not os.path.exists(STORAGE_INFO["dir"]):
        os.makedirs(STORAGE_INFO["dir"])
        return False, "Files not found, no site retrievable."

    else:
        try:
            with open(FILE_PATH, "w", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = {}
            return "File is empty or broken. Refreshing file and returning."

        if data[key] is not None:
            return True, data[key]

        else:
            return False, "Data not found inside of the file."

    return True


def list_sites():
    """
    TODO:
        Method needs finished as mainly just a stub w/ file&dir checker.

    """
    if not os.path.exists(STORAGE_INFO["dir"]):
        os.makedirs(STORAGE_INFO["dir"])
        print("Files not found sites not listable.")
        return False

    return True
