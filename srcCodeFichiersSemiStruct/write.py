import json

import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "BDD101", "data.json")


f = open(file_path)
data = json.load(f)
f.close()

for i in data["features"]:
    print(i["geometry"]["coordinates"][0])


for feature in data["features"]:
    geometry = feature["geometry"]
    if geometry["type"] == "Point":
        geometry["coordinates"][0] += 0.1
        geometry["coordinates"][1] += 0.1

f = open('out.json', 'w')
json.dump(data, f, indent=4)
f.close()


