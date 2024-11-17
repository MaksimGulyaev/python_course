# TODO решите задачу

import json
#from fileinput import filename
from pprint import pprint

filename = 'input.json'
Score = []
Weight = []

with open(filename, "r") as f:
    d = f.read()

data = json.loads(d)
for i in data:
    Score.append(i["score"])
    Weight.append(i["weight"])


def task(Score, Weight) -> float:
    sum = 0
    for i in range (0, len(Score)):
        sum = sum + Score[i]*Weight[i]
    return round(sum,3)



print(task(Score, Weight))
