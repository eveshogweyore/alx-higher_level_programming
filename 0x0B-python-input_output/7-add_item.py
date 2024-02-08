#!/usr/bin/python3
"""
    A module that adds all arguments to a Python list and
    save them to a file
"""
import pathlib, sys, json

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

if pathlib.Path("add_item.json").exists():
    items = load("add_item.json")
else:
    with open("add_item.json", "w") as file_obj:
        items = []

for i in range(len(sys.argv)):
    if i != 0:
        items.append(sys.argv[i])

save(items, "add_item.json")
