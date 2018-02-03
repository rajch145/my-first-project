import json
from datetime import datetime


def process_json(input_data):
    json_dict = json.loads(input_data)
    for key, value in json_dict.items():
        print('For key {key} value is {value}'.format(key = key, value = value))


if __name__ == "__main__":
    json_dict = {'Name':'Raj', 'ID':'145'}
    process_json(json.dumps(json_dict))
