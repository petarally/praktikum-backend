import json
from pathlib import Path

def load_data(file_path):
    try:
        if not Path(file_path).exists():
            with open(file_path, "w") as f:
                json.dump({}, f)
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Error loading data from {file_path}: {e}")

def save_data(file_path, data):
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        raise ValueError(f"Error saving data to {file_path}: {e}")
