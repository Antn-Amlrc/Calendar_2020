file = open('input2.txt', "r")
lines = file.readlines()
file.close()

# PART 1

good_passwords = 0
for line in lines:
    elements = line.split()
    down, supp = elements[0].split('-')  # upper and lower number of occurences
    letter = elements[1][0]  # letter to find
    password = elements[2]
    cpt = password.count(letter)
    if cpt>=int(down) and cpt<=int(supp):
        good_passwords+=1
print("There are",good_passwords,"good passwords.")


# PART 2

good_passwords = 0
for line in lines:
    elements = line.split()
    pos1, pos2 = elements[0].split('-')  # position to find letter
    letter = elements[1][0]  # letter to find
    password = elements[2]
    first_position_correct, second_position_correct = 0, 0
    if password[int(pos1)-1]==letter:
        first_position_correct = 1
    if password[int(pos2)-1]==letter:
        second_position_correct = 1
    if first_position_correct+second_position_correct==1:
        good_passwords+=1
print("There are",good_passwords,"good passwords.")
