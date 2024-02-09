#!/usr/bin/python3
"""
    A module that adds all arguments to a Python list and
    save them to a file
"""
import json
import sys
import pathlib

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

json_file = "add_item.json"

if pathlib.Path(json_file).exists():
    items = load(json_file)
else:
    with open(json_file, "w") as file_obj:
        items = []

for i in range(len(sys.argv)):
    if i != 0:
        items.append(sys.argv[i])

save(items, json_file)
