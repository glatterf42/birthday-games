import pandas as pd
import numpy as np
from template import template


df = pd.read_csv("fun_facts.csv", delimiter=";")

names = set(df["name"])

# # Use a sample name for development/testing:
# names = ["test1"]

for name in names:
    facts = df[df["name"] != name]["fact"]
    random_facts = facts.sample(n=25)
    with open(f"bingos/{name}_bingo.tex", "w") as f:
        # Use this if two guests share the same name:
        # give them different names in fun_facts.csv,
        # then update their names here to their real names.
        if name == "example1" or name == "example2":
            name = "example"
        f.write(template.format(name=name, *random_facts))
