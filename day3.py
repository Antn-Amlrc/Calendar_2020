file = open('input3.txt', "r")
lines = file.readlines()
file.close()

# PART 1
def tree_encountered_during_ride(strat):
    strategy = [strat[0],strat[1]] # form DOWN, RIGHT
    n_lines, n_columns = len(lines), len(lines[0])
    X, Y = 0, 0
    tree_encountered = 0
    while X<n_lines:  # While we're not at the end of the ride
        Y = (Y+strategy[1])%(n_columns-1)
        X += strategy[0]
        # Detect if there is a tree at current location
        if X<n_lines and lines[X][Y]=="#": # Hit a tree
            tree_encountered+=1
    return tree_encountered
    #print("I encountered ",tree_encountered, "trees along the ride")


strategies = [[1,1],[1,5],[1,7],[2,1]]  # All slopes
total_tree_encountered = tree_encountered_during_ride([1,3])
for s in strategies:
    total_tree_encountered *= tree_encountered_during_ride(s)
print("There is a total of", total_tree_encountered,"at the end of all slopes.")
