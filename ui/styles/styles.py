import os
import json

from .presets import *

PRIMARY_COLORS = {**DEFAULT}
HEADERS = ("frame", "canvas", "node", "data", "bg-label", "btn_text", "btn_primary", "btn_success", "btn_danger")
PATH = "./ui/styles/current.json"

if os.path.isfile(PATH):
    with open(PATH, "r") as current:
        PRIMARY_COLORS = json.load(current)
else:
    with open(PATH, "w") as current:
        json.dump(PRIMARY_COLORS, current)
