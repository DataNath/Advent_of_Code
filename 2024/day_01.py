# Part 1:

list_1 = []
list_2 = []

with open("./inputs/Day 1.txt", "r") as start_data:
    for line in start_data:
        value = line.strip().split()
        list_1.append(int(value[0]))
        list_2.append(int(value[1]))

list_1 = sorted(list_1)
list_2 = sorted(list_2)

combined = zip(list_1, list_2)

p1_ans = sum(abs(pair[0] - pair[1]) for pair in combined)

# Part 2:

p2_ans = sum((list_2.count(nums) * nums) for nums in list_1)

print(f"P1 ans: {p1_ans} | P2 ans: {p2_ans}")