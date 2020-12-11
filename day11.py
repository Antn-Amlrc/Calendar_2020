file = open('input11.txt', "r")
lines = file.readlines()
file.close()

"""
I'll use a padding of zero for all sides to better utilize the input.
To switch from one part to the other you'll have to change the occupied number in get_seat_state
and to comment the corresponding line to search for neighbors in the main code.
"""

def get_seat_state(neighbors, current_state, changed):
    """
    From a list of adajacent seats and the current state of the seat, this funct
    gives the future state of the seat.
    """
    occupied = neighbors.count("#")
    if current_state=="#" and occupied>=5:  # Put "occupied>=5" instead if running part2
        return "L", True  # Seat become empty
    elif current_state=="L" and occupied==0:
        return "#", True
    else:
        if changed:
            return current_state, True
        else:
            return current_state, False

def count_occupied_seats(seats):
    total = 0
    for row in seats:
        total += row.count("#")
    return total

def visibility_method_part1(seats, i, j):
    neighbors = []
    neighbors += seats[i-1][j-1:j+2] # above row
    neighbors.append(seats[i][j-1])  # left
    neighbors.append(seats[i][j+1]) # right
    neighbors += seats[i+1][j-1:j+2] # below row
    return neighbors

def visibility_method_part2(seats, i, j):
    direction = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
    neighbors = []
    for d in direction:
        x, y = i, j
        found=None  # No seat found initially
        while seats[x][y] != "0" and found==None:  # While no seat found or padding encounter
            x, y = x + d[0], y + d[1] # We move one step in the direction given
            if seats[x][y] in ["#","L"]:  # Found a seat
                found = seats[x][y]
                neighbors.append(found)
    return neighbors

# Padding
padding_seats = []
padding_seats.append("".join(["0"]*(len(lines[0])+1))) # padding top
for line in lines:  # padding right and left
    line = line[:-1] # In order to remove the '\n' character
    line = "0"+line+"0"  # padding left and right
    padding_seats.append(line)
padding_seats.append("".join(["0"]*(len(lines[0])+1))) # padding bottom


changed = True
new_seats = []
while changed:
    changed = False
    new_seats = []
    new_seats.append("".join(["0"]*(len(lines[0])+1)))
    for i in range(1,len(padding_seats)-1): # We do not use our function and padding lines
        new_row = "0"
        for j in range(1,len(padding_seats[i])-1): # Same here

            # Reachable seats with visibility method from part1
            # neighbors = visibility_method_part1(padding_seats, i, j)

            # Reachable seats with visibility method from part2
            neighbors = visibility_method_part2(padding_seats, i, j)
            
            future_state, changed = get_seat_state(neighbors, padding_seats[i][j], changed)
            new_row += future_state
        new_row += "0"
        new_seats.append(new_row)
    new_seats.append("".join(["0"]*(len(lines[0])+1))) # padding bottom
    padding_seats = new_seats

print("The total number of occupied seats after stabilization is", count_occupied_seats(new_seats))
