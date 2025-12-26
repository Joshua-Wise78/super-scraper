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
    retrieve_from_json
        Retrieve file from json text.
        Args:
            key (str): The key of the site URL
    """
    if not os.path.exists(STORAGE_INFO["dir"]):
        os.makedirs(STORAGE_INFO["dir"])
        return False, "Files not found, no site retrievable."

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return "File is empty or broken. Refreshing file and returning."

    if key in data:
        return True, data[key]
    else:
        return False, "Data not found inside of the file."


def list_sites():
    """
    list_sites
        List out every single site stored inside of the file.

    NOTE:
        Will error out if the folder contains more than 2000 characters.

    """
    if not os.path.exists(STORAGE_INFO["dir"]):
        os.makedirs(STORAGE_INFO["dir"])
        print("Files not found sites not listable.")
        return False

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False, "File is empty or broken. Nothing to list"

    if not data:
        return False, "No sites currently stored."

    formattedSites = []
    for key, value in data.items():
        formattedSites.append(f"**{key}**: {value}")

    return True, formattedSites


def search_sites():
    """
    search_sites
        Search sites from keywords using the key.
        Args:
            search (str): Keyword to search for a list of sites.
    TODO:
        Needs finished and tested

    """
    if not os.path.exists(STORAGE_INFO['dir']):
        print("Files not found sites not searchable.")
        return False, "Files not found 404: Not searchable"

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False, "Data not loadable, either empty or broken."

    results = []
    if data is not None:
        return True, results
        
