file = open('input15.txt', "r")
lines = file.readlines()
file.close()
lines = lines[0][:-1]
lines = lines.split(",")

FINAL_TURN = 30000000
turn = {}  # with format number --> last turn spoken

current_turn = 1
next_number = None

while lines: # first time for each starting number
    turn[lines[0]] = current_turn
    next_number = lines[0]
    lines = lines[1:]
    current_turn+=1

next_number = "0"

while current_turn!=FINAL_TURN:
    if not(next_number in turn.keys()):
        # New number so elve say 0
        turn[next_number] = current_turn
        next_number = "0"

    else:
        temp = turn[next_number]  # We preserve the last turn it was spoken
        turn[next_number] = current_turn
        next_number = str(int(current_turn) - int(temp))
    current_turn+=1
print(next_number)
