file = open('input9.txt', "r")
lines = file.readlines()
file.close()

# PART 1

def is_the_sum_of_two_numbers(n, preambule):
    for i in range(len(preambule)):
        n1 = int(preambule[i])
        for j in range(i+1,len(preambule)):
            n2 = int(preambule[j])
            if n1+n2==n:
                preambule.remove(preambule[0])  # We remove the head of the list
                preambule.append(n)  # We add the last valid number found
                return True
    return False


preambule = [line[:-1] for line in lines[:25]]
invalid_number = 0
for line in lines[25:]:
    invalid_number = int(line[:-1])
    if not(is_the_sum_of_two_numbers(invalid_number, preambule)):
        print("The following number does not have XMAS property", invalid_number)
        break


# PART 2
contiguous_list = []
for index_to_start in range(len(lines)): # For each possible start
    first_number = int(lines[index_to_start])  # Start number
    contiguous_list.clear()
    cpt_to_search = 0  # index to see following numbers
    if not(first_number == invalid_number):  # Will only give at least two number set
        while sum(contiguous_list)<invalid_number and index_to_start+cpt_to_search<len(lines):  # While sum lower than invalid number
            new_number = int(lines[index_to_start+cpt_to_search])
            contiguous_list.append(new_number)
            cpt_to_search += 1  # We increment to go to next number
        if invalid_number == sum(contiguous_list) and len(contiguous_list)>1:
            encryption_weakness = min(contiguous_list)+max(contiguous_list)
            print("The encryption weakness in my list is", encryption_weakness)
