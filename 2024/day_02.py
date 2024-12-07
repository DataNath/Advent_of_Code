# Rule check function:

def rule_checker(given_list):

    if given_list == sorted(given_list) or given_list == sorted(
        given_list, reverse=True
    ):
        if all(
            abs(given_list[i] - given_list[i - 1]) in [1, 2, 3]
            for i in range(1, len(given_list))
        ):
            return 1
    return 0

p1_ans = 0
p2_lists = set()

with open("./inputs/Day 2.txt", "r") as start_data:
    for line in start_data:
        numbers = list(map(int, line.strip().split()))

        # Part 1:

        p1_ans += rule_checker(numbers)

        # Part 2:
        
        for j in range(0, len(numbers)):
            new_list = numbers[:j] + numbers[j + 1:]
            if rule_checker(new_list) == 1:
                p2_lists.add(tuple(numbers))

p2_ans = len(p2_lists)

print(f"P1 ans: {p1_ans} | P2 ans: {p2_ans}")