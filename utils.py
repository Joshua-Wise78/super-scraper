import json
import os

STORAGE_INFO = {
    "dir": "storage",
    "file": "sites.json"
}

FILE_PATH = os.path.join(STORAGE_INFO['dir'], STORAGE_INFO['file'])

def save_to_json(key, value):

    if not os.path.exists(STORAGE_INFO['dir']):
        os.makedirs(STORAGE_INFO['dir'])

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
