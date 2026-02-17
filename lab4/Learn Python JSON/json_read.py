import json

with open("data.json","r") as f:
    loaded = json.load(f)
print(loaded)
