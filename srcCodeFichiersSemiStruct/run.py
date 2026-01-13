import json
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "BDD101", "data.json")

f = open(file_path)
data = json.load(f)
f.close()

print(data)
print(data["features"])
print(data["features"][0]["geometry"])

for i in data["features"]:
    print(i["geometry"]["coordinates"][0])

