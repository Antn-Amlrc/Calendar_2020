file = open('input7.txt', "r")
lines = file.readlines()
file.close()

MY_BAG = "shiny gold"
# PART 1 & PART 2

def extract_color(container):
    # Return all colors from colored bags contained in current bag
    description = []
    for b in container.split(","):
        detailed_description = b.split()
        description.append([detailed_description[0], detailed_description[1]+" "+detailed_description[2]])
    return description

def can_contain_shiny_gold(list):
    for c in list:
        if c==MY_BAG:
            return True
    return False

def search_arbo(dico):
    bags = []
    contain_shiny_gold_bag = [MY_BAG]
    while contain_shiny_gold_bag!=[]:  # While there is bag to visit
        to_find = contain_shiny_gold_bag.pop(0)  # Retrieve one element of the list
        for key,value in dico.items():
            if to_find in [value[i][1] for i in range(len(value))] and not(key in contain_shiny_gold_bag):  # Means that this bag can hold a shiny gold bag
                contain_shiny_gold_bag.append(key)
                bags.append(key)
    return len(set(bags))  # Return only first occurences so there is no redundance


def compute(bag):
    # Recursive function to compute bags included in current bag
    list_of_bags = luggages[bag[1]]  # All directly contained bags
    computed = 1  # number of bags
    if list_of_bags[0][0]=="no":
        return computed  # No bags here
    for element in list_of_bags:
        computed += int(element[0])*compute(element)
    return computed


luggages = {}  # A dictionnary with form : bag-->list(number_of_bag, bag_color)

for line in lines:
    form = line.split("contain")
    current_bag = form[0].split()
    bag_name = current_bag[0]+" "+current_bag[1]  # Retrieve the current bag color
    luggages[bag_name] = extract_color(form[1])  # Retrieve only the list of bags

nb_bags = search_arbo(luggages)
print("There is", nb_bags,"that can contain shiny gold bags.")

contained_in_shiny_gold_bag = (1,MY_BAG)
all_bags = compute(contained_in_shiny_gold_bag)-1  # -1 to retrieve the count of the shiny gold bag
print("There is a total of", all_bags, " in a shiny gold bag.")
