file = open('input16.txt', "r")
lines = file.readlines()
file.close()

# PART 1

line, idx = lines[0], 0
all_possible_value_for_fields = set()  # empty set
wrong_fields = 0
fields_name = []  # List of all field names
good_tickets = []  # list of all goods tickets
all_possible_value_by_field = {}  # Dic with association field name ---> set of values

while line != "\n":  # Here is select all possible values for ticket fields
    splited_line = line.split(":")
    fields_name.append(splited_line[0]) # We add the field name to the list of them
    possibles_values = splited_line[1]
    sets_values = possibles_values.split("or")
    s = set()  # empty set
    for st in sets_values:  # for each couple of value
        values = st.split("-")
        s = s | { x for x in range(int(values[0]),int(values[1])+1) }
    idx+=1
    line = lines[idx]
    all_possible_value_by_field[splited_line[0]] = s
    all_possible_value_for_fields |= s

my_ticket = lines[lines.index("your ticket:\n")+1][:-1].split(",")
idx = lines.index("nearby tickets:\n")
is_a_nice_ticket = True
for i in range(idx+1, len(lines)):
    is_a_nice_ticket = True
    ticket = lines[i][:-1].split(",")
    for field in ticket:
        f = int(field)
        if not(f in all_possible_value_for_fields):
            is_a_nice_ticket = False
            wrong_fields+=f
    if is_a_nice_ticket:
        good_tickets.append(ticket)

print("The total error of all tickets is", wrong_fields)

# PART 2
"""
Establish a set of value for each field name.
Establish a set of value for each index of ticket. For a given index, the set
of value will be the union of every value at the index position in every ticket.
If this problem is solvable, then at every iteration I must be capable of corresponding
with certainty a field name to its index position. Then suppresing a possibility,
other might appear because there was once more possibilities. And so on... Until
all field name are attributed.
"""

# Here are my first two steps from above
good_tickets.append(my_ticket)
tickets_values = []  # each set of values by index
tickets_values = [set() for i in range(len(fields_name))]
for ticket in good_tickets:
    for i in range(len(ticket)):
        tickets_values[i].add(ticket[i])

association = {}  # dico of association index --> list of field names
for i in range(len(my_ticket)):
    association[i] = fields_name[:]

for j in range(len(my_ticket)):  # For each field in the ticket
    for fn in fields_name: # For each field name
        values_for_field = all_possible_value_by_field[fn]  # Get its values
        valid_field = True  # Field is supposed valid until proved otherwise
        for value in tickets_values[j]:  # For each value in particular index
            if not(int(value) in values_for_field):
                valid_field = False
                break
        if not(valid_field):
            association[j].remove(fn)
"""
Not a resolution.
I simply propagate the following constraints :
    -> All index must be associated to a different field
    -> All index must be associated to only one field
"""
maj = True
while maj:
    maj = False
    for v in association.values():
        if len(v)==1:  # Only possibility
            for w in association.values():
                if w!=v and v[0] in w:
                    w.remove(v[0])
                    maj = True


final_res = 1
list_of_departure_index = []
# Get index from departure field
for key, value in association.items():
    if len(value[0])>9 and value[0][:9]=="departure":
        list_of_departure_index.append(key)
# Get from our ticket the value of those fields
for idx in list_of_departure_index:
    final_res*= int(my_ticket[idx])
print(final_res)
