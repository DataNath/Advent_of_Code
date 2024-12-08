import re

def product(pair):
    l = int(re.search(r"mul\((\d+),(\d+)\)", pair).group(1))
    r = int(re.search(r"mul\((\d+),(\d+)\)", pair).group(2))
    total = l * r
    return total

with open("./inputs/Day 3.txt", "r") as start_data:
    content = start_data.read()
    pairs = re.findall(r"mul\(\d+,\d+\)", content)
    objects = list(re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", content))

    # Part 1:

    p1_ans = 0
    for item in pairs:
        p1_ans += product(item)

    # Part 2:
    active = True
    p2_ans = 0
    for obj in objects:
        if obj == "don't()":
            active = False
        elif obj == "do()":
            active = True
        elif active:
            p2_ans += product(obj)
    
    print(f"P1 ans: {p1_ans} | P2 ans: {p2_ans}")