file = open('input14.txt', "r")
lines = file.readlines()
file.close()

"""
To switch between parts, uncomment the section you want to run and comment the other.
Sections are delimited by their names #PART i.
"""

BIT_SIZE = 36

def bin(d,nb=0):
    """
    Convert a integer to its binary representation.
    nb is used to fill with zeros to match a given size of binary number.
    In this exercice, its 36.
    """
    if d==0:
        b="0"
    else:
        b=""
        while d!=0:
            b="01"[d&1]+b
            d=d>>1
    return b.zfill(nb)

def apply_mask(m, value):
    """ Apply a mask to a binary value """
    value = list(value)
    for i in range(len(m)):
        if m[i]!="X":
            value[i]=m[i]
    return "".join(value)

def find_all_adresses(m, adrs):
    """ Get all adresses from a given address with floating X """
    adrs_bin = list(bin(adrs,BIT_SIZE))  # address in binary form
    addresses = []  # List of addresses
    for i in range(len(m)):  # Apply mask on address
        if adrs_bin[i]=="0" or m[i]=="X":  # Apply mask on address
            adrs_bin[i]=m[i]
    xs = adrs_bin.count("X")  # Number of floating bits
    possible_addresses = 2**xs  # Number of possibility
    for n in range(possible_addresses):  # For each possible different address
        new_adrs = adrs_bin.copy()
        an_address = bin(n,xs)  # binary form to change X easily
        # Change floating bits on initial address
        for i in range(len(new_adrs)):
            if new_adrs[i]=="X":
                new_adrs[i] = an_address[0]
                an_address = an_address[1:]
        addresses.append(int("".join(new_adrs),2))
    return addresses


memory = {}  # dico
mask = ""


for line in lines:
    affect, affected_value = line.split(" = ")
    if affect == "mask":
        mask = affected_value[:-1]
    else:
        true_value = int(affected_value)
        affected_value = bin(true_value,BIT_SIZE)
        address = int(affect.split("[")[-1][:-1])
        # PART 1

        value_with_mask = int(apply_mask(mask, affected_value),2)
        memory[address] = value_with_mask
        """
        # PART 2
        addresses = find_all_adresses(mask, address)
        for ad in addresses:
            memory[ad] = true_value
        """
print("Sum of all values in memory is", sum(memory.values()))
