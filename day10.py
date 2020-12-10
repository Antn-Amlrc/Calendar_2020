file = open('input10.txt', "r")
lines = file.readlines()
file.close()

int_lines = list(map(int, lines))  # To convert them all in Integer
sorted_adapters = [0]+sorted(int_lines)  # Sort to better class adapters
final_adapter = sorted_adapters[-1]  # last element is max of list
"""
# PART 1
sorted_adapters+= [0,0,0]  # just a trick to optimize testing

one_jolt, three_jolts = 0, 1 # 3-jolts starts at one to count with final adapter
last_adapter = 0  # adapter near seat

while sorted_adapters!=[0,0,0]:  # Means we're at the end of the list
    possible_pairs = sorted_adapters[0:3] # First three possibility
    if abs(last_adapter-possible_pairs[0])==1:
        one_jolt+=1
    elif abs(last_adapter-possible_pairs[0])==3:
        three_jolts+=1
    last_adapter = possible_pairs[0]
    sorted_adapters = sorted_adapters[1:]  # We remove first element
print("There are", one_jolt, "1-jolt and", three_jolts, "3-jolts.")
result = one_jolt*three_jolts
print("Multiplication of 1-jolt and 3-jolts gives", result)
"""

# PART 2
"""
The idea is to begin from the final adapter and then walk our way back to all possible
arrangments. However we will not visit a branch that has already been visited. Instead
we'll remember the number of leaves this branch gives and add it to our total of possibility.
To improve the complexity of our algorithm we'll use a DFS based algo.
"""

leaves = {}  # Dico of all branches from a given number. Initially empty.

def get_neighbors(branch):
    """
    Return all number from distance 3 or less from current adapter.
    """
    index = sorted_adapters.index(branch)
    if 0<=index<3:
        possible_adapters = sorted_adapters[0:index]  # possibles adapters
    else:
        possible_adapters = sorted_adapters[index-3:index]
    print("I found those 3",possible_adapters)
    true_adapters = []
    for adpt in possible_adapters:
        if branch-adpt<=3:  # A direct neighbor
            true_adapters.append(adpt)
    return true_adapters

def count_leaves(branch):  # Recursive func
    neighbors = get_neighbors(branch)
    print(neighbors)
    number_of_possibility = 0
    if not(neighbors):
        print("Here's a branch", branch)
        leaves[branch] = 1 # Back to first adapter ( also first branch to be found )
    else:
        for n in neighbors:  # For each neighbors...
            if not(n in leaves.keys()):  # If we didn't already visit it
                print("From", branch,"to ------>", n)
                count_leaves(n)  # We count the number of leaves from it
            number_of_possibility += leaves[n]
        if not(branch in leaves.keys()):
            leaves[branch] = number_of_possibility
        print("Leave succeed", branch, "in", number_of_possibility)

print("We want each possible branch from", final_adapter)
count_leaves(final_adapter)
print("Total =", leaves[final_adapter])
