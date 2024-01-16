import os
import json

from .presets import DEFAULT

PRIMARY_COLORS = {**DEFAULT}
HEADERS = {
    "Background": "frame",
    "Canvas Background": "canvas",
    "Node": "node",
    "Data": "data",
    "Text Background": "bg-label",
    "Button Text": "btn_text",
    "Button": "btn_primary",
    "Insert Button": "btn_success",
    "Delete Button": "btn_danger",
}
PATH = "./ui/styles/current.json"

try:
    if os.path.isfile(PATH):
        with open(PATH, "r") as current:
            PRIMARY_COLORS = json.load(current)
except FileNotFoundError as e:
    with open(PATH, "w") as current:
        json.dump(PRIMARY_COLORS, current)
