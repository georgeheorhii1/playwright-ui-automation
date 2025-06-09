import json
import os


def load_test_data():
    file_path = os.path.join(os.path.dirname(__file__), 'test_data.json')
    with open(file_path, 'r') as f:
        return json.load(f)
