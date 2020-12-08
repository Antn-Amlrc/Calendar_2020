file = open('input8.txt', "r")
lines = file.readlines()
file.close()

"""
CHANGE THE WHILE TO SWITCH FROM PART 1 TO PART 2 !
"""

# PART 1
ACCUMULATOR = 0
CPT_INSTRUCTION = [0]*len(lines)

def get_new_index(instr):
    order, index_to_go = instr.split() # Action to perform, position to go
    if order=="acc":
        global ACCUMULATOR
        ACCUMULATOR += int(index_to_go)
        return 1
    elif order=="nop":
        return 1
    elif order=="jmp":
        return int(index_to_go)


i = 0
index_instructions_done = []  # All index of instruction that have been done
index_instruction_changed = None  # Index of the changed instruction
while not(CPT_INSTRUCTION[i]):   # To do PART 1
#while i!=len(CPT_INSTRUCTION):  # To do PART 2
    instruction = lines[i][:-1]  # Slicing to ignore the '\n' character

    """
    # PART 2 is basically this ...
    if CPT_INSTRUCTION[i]:  # Here's a cycle
        if index_instruction_changed != None:  # We go back to the last instruction changed if there is one
            element = index_instructions_done.pop()
            while element!=index_instruction_changed:  # While we're not on the changed instruction
                order, range = lines[element][:-1].split()
                if order=='acc':
                    ACCUMULATOR -= int(range)
                CPT_INSTRUCTION[element]-=1  # We "unvisit" them
                element = index_instructions_done.pop()
            CPT_INSTRUCTION[index_instruction_changed] -= 1  # Not a good path
            index_instruction_changed = None
        while index_instructions_done: # Find in backtracking the next fit
            i_instr = index_instructions_done[len(index_instructions_done)-1]
            order, range = lines[i_instr][:-1].split()
            if order in ["jmp","nop"]:
                if order=="jmp":
                    instruction = "nop "+range  # Switch
                else:
                    instruction = "jmp "+range  # Switch
                i = i_instr  # New index to go forward
                index_instruction_changed = i_instr  # New instruction changed
                index_instructions_done.pop()
                break
            else:
                retired = index_instructions_done.pop()  # "acc" order to ignore
                ACCUMULATOR -= int(range)
                CPT_INSTRUCTION[retired]-=1  # And "unvisit"
    """
    CPT_INSTRUCTION[i] += 1  # Now visited
    index_instructions_done.append(i)
    #print("Done :", index_instructions_done)
    i += get_new_index(instruction)
print("The accumulator is equals to", ACCUMULATOR)

"""
# PART 2
My idea is to backtrack on jmp and nop order as soon as I detect a cycle.
Then I switch the last nop/jmp instruction to its opposite.
"""
