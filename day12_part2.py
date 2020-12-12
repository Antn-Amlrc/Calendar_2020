file = open('input12.txt', "r")
lines = file.readlines()
file.close()

# PART 2
def go_to_waypoint(wp, pos):
    """ Move to waypoint. """
    for k in wp.keys():
        pos[k] += wp[k]
    return pos

def move_waypoint(wp, act, value, computed_waypoint):
    """ Change the position of the waypoint. """
    # New waypoint relative to the ship
    if act=="S":
        computed_waypoint[1]-=value
    elif act=="N":
        computed_waypoint[1]+=value
    elif act=="E":
        computed_waypoint[0]+=value
    else:
        computed_waypoint[0]-= value

    # Transformation to a dico

    # Modification of E/W position
    if act in ["E","W"]:
        if computed_waypoint[0]<0:
            wp["W"] = abs(computed_waypoint[0])
            wp["E"] = 0
        else:
            wp["E"] = abs(computed_waypoint[0])
            wp["W"] = 0

    # Modification of N/S position
    if act in ["S","N"]:
        if computed_waypoint[1]<0:
            wp["S"] = abs(computed_waypoint[1])
            wp["N"] = 0
        else:
            wp["N"] = abs(computed_waypoint[1])
            wp["S"] = 0

    return wp, computed_waypoint

def rotate_waypoint(action, ax, computed_waypoint):
    """ Rotate waypoint. """
    x, y = computed_waypoint
    while ax:
        x,y = y,x  # y and x exchange their values at each 90° rotation
        if action=="R":
            y = -y
        else:
            x = -x
        ax-=1
    wp = {"E":0, "W":0, "N":0, "S":0}
    # Modification of E/W position
    if x<=0:
        wp["W"] = abs(x)
        wp["E"] = 0
    else:
        wp["E"] = abs(x)
        wp["W"] = 0
    # Modification of N/S position
    if y<=0:
        wp["S"] = abs(y)
        wp["N"] = 0
    else:
        wp["N"] = abs(y)
        wp["S"] = 0
    return wp, [x,y]



position = {"E":0, "W":0, "N":0, "S":0}
waypoint = {"E":10, "W":0, "N":1, "S":0}  # relative to the ship
computed_waypoint = [10,1]  # E/W --- N/S

for instruction in lines:
    action, value = instruction[0], int(instruction[1:])
    if action=="F":
        while value:  # go to waypoint value times
            position = go_to_waypoint(waypoint, position)
            value -= 1
    elif action in ["N", "S", "E", "W"]:
        new_waypoint, computed_waypoint = move_waypoint(waypoint, action, value, computed_waypoint)
    elif action in ["R", "L"]:
        axis = value//90  # To get the number of time the ferry is 90° rotating
        axis = axis%4  # In case a entire turn on itself is represented by 5 turns on itself
        waypoint, computed_waypoint= rotate_waypoint(action, axis, computed_waypoint)

manhattan_distance = abs(position["E"]-position["W"])+abs(position["N"]-position["S"])
print("Distance is", manhattan_distance)
