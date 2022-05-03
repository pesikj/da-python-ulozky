import json

import pandas

df = pandas.read_csv("battles.csv")
df.to_csv("battles.tsv", sep="\t", index=False)

with open("battles.tsv") as file:
    lines = file.readlines()

data = []
for line in lines[1:]:
    line = line.split("\t")
    row = {"name": line[0], "year": line[1]}
    attackers = [item for item in line[5:9] if len(item) > 0]
    row["attackers"] = attackers
    defenders = [item for item in line[9:13] if len(item) > 0]
    row["defenders"] = defenders
    if line[13] == "win":
        row["winners"] = attackers
    elif line[13] == "loss":
        row["winners"] = defenders
    else:
        row["winners"] = []
    data.append(row)

with open("battles.json", mode="w") as people:
    json.dump(data, people, indent=4, ensure_ascii=False)
