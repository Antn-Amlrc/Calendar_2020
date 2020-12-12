file = open('input12.txt', "r")
lines = file.readlines()
file.close()

# PART 1

def get_new_direction(action, direction, ax):
    compass = "SWNESWNE"  # Twice SWNE to not exceed list length when fiding new direction
    new_direction = direction
    ind = compass.index(direction)  # first index of current direction
    if action=="R":
        new_direction = compass[ind+ax]
    else:
        new_direction = compass[ind-ax]
    return new_direction


position = {"E":0, "W":0, "N":0, "S":0}
direction = "E"
for instruction in lines:
    action, value = instruction[0], int(instruction[1:])
    if action=="F":
        position[direction]+=value
    elif action in ["N", "S", "E", "W"]:
        position[action]+=value
    elif action in ["R", "L"]:
        axis = value//90  # To get the number of time the ferry is 90° rotating
        axis = axis%4  # In case of an entire turn ( or more ) on itself 
        direction = get_new_direction(action, direction, axis)
manhattan_distance = abs(position["E"]-position["W"])+abs(position["N"]-position["S"])
print("Distance is", manhattan_distance)
