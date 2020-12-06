file = open('input6.txt', "r")
lines = file.readlines()
file.close()
lines.append("\n")

# PART 1

def compute_answers_part1(group):
    # To recover only the unique occurences of each letter
    return len(set(group))


group = ""
sum_yes = 0
for line in lines:
    if line!="\n":
        # Gather group
        group = group + line[:-1]  # To leave the '\n' character
    else:
        # Compute total yes answer
        sum_yes += compute_answers_part1(group)
        group = ""
print("There is", sum_yes,"yes answers.")

# PART 2

def compute_answers_part2(group):
    all_yes_group = set(group[0])
    for g in group[1:]:
        all_yes_group &= set(g)
    return len(all_yes_group)

group = []
sum_yes = 0
for line in lines:
    if line!="\n":
        # Gather group
        group.append(line[:-1])  # To leave the '\n' character
    else:
        # Compute total yes answer
        sum_yes += compute_answers_part2(group)
        group = []
print("There is", sum_yes,"yes answers.")
