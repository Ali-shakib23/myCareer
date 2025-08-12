import json

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lists = json.load(f)
            return lists
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_file(filepath , data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)