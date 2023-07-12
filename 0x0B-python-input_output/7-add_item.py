#!/usr/bin/python3
"""
this script that adds all arguments to a Python list, and then
save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

try:
    new_text = load_from_json_file(file_name)
    for i in range(1, len(sys.argv)):
        new_text.append(sys.argv[i])
    save_to_json_file(new_text, file_name)
except FileNotFoundError:
    save_to_json_file(sys.argv[1:], file_name)
