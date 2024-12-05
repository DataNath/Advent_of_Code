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

total_diff = sum(abs(pair[0] - pair[1]) for pair in combined)

print(total_diff)

# Part 2:

ans = sum((list_2.count(nums) * nums) for nums in list_1)

print(ans)