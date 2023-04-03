import pandas as pd
import numpy as np
from template import template


df = pd.read_csv("fun_facts.csv", delimiter=";")

names = set(df["name"])

# # for development:
# names = ["Maggy"]

for name in names:
    facts = df[df["name"] != name]["fact"]
    random_facts = facts.sample(n=25)
    with open(f"bingos/{name}_bingo.tex", "w") as f:
        if name == "Anna1" or name == "Anna2":
            name = "Anna"
        f.write(template.format(name=name, *random_facts))
