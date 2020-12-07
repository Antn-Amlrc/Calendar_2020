file = open('input5.txt', "r")
lines = file.readlines()
file.close()

# PART 1

def get_seat_ID(row, col):
    # Return seat ID
    return row*8 + col

def get_row_number(row):
    # Return the actual row on the plane
    power_of_2 = 7
    lower, upper = 0, 2**power_of_2-1
    for c in row:
        if c=='F':
            upper -= 2**(power_of_2-1)
        elif c=='B':
            lower += 2**(power_of_2-1)
        power_of_2 -=1
    return lower  # Or upper it's the same anyway


def get_column_number(col):
    power_of_2 = 3
    lower, upper = 0, 2**power_of_2-1
    for c in col:
        if c=='L':
            upper -= 2**(power_of_2-1)
        elif c=='R':
            lower += 2**(power_of_2-1)
        power_of_2 -=1
    return lower  # Or upper it's the same anyway


max = 0
seats_ids = []
for line in lines:
    row, col = get_row_number(line[:7]), get_column_number(line[-4:])
    id_seat = get_seat_ID(row, col)
    seats_ids.append(id_seat)
    if id_seat>max:
        max = id_seat
print("The highest seat ID on boarding pass is", max)


# PART 2
for i in range(len(seats_ids)):
    s1 = seats_ids[i]
    for j in range(i+1,len(seats_ids)):
        s2 = seats_ids[j]
        if abs(s1-s2)==2:
            estime_id = (s1+s2)//2
            if not(estime_id in seats_ids):
                print("Here's a seat !", estime_id)
