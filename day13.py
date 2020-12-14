file = open('input13.txt', "r")
lines = file.readlines()
file.close()


# PART 1
time_stamp = int(lines[0])  # Initial depart time
buses = list(set(lines[1].split(",")))
if "x" in buses : buses.remove("x")
buses = list(map(int, buses))

"""
buses_available = [0]*len(buses)
tps = 0  # current time
while sum(buses_available)==0 or tps<time_stamp:
    tps+=1
    buses_available = [0]*len(buses)
    for i in range(len(buses)):
        if tps%buses[i]==0:
            buses_available[i]=1

bus_ID = buses[buses_available.index(1)]
wait = tps-time_stamp
print("There is a bus available at time", tps,"with ID bus",bus_ID)
print("I'll have to wait", wait,"minutes.")
print("Therefore solution is", bus_ID*wait)
"""


# PART 2
"""
The idea here is to have a variable step when iterating.
Once an alignment of n buses is found, the new step to search the alignment of n+1 buses
is the ppcm value of all n buses. This way, we keep their alignment when iterating.
"""

def ppcm(n):
    """ ppcm calculation with n>=2 """
    def _pgcd(a,b):
        while b: a, b = b, a%b
        return a
    p = abs(n[0]*n[1])//_pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p*x)//_pgcd(p, x)
    return p


def is_solution(buses_available, all_buses, step):
    """ Return if a schedule is or is not a solution to the problem. """
    is_sol = True
    aligned = []
    for i in range(len(buses_available)):
        b = buses_available[i]
        if b!="x":  # Irrelevant bus
            if int(b)%int(all_buses[i])!=0:
                is_sol = False
            else:
                aligned.append(int(all_buses[i]))
    if not(is_sol):
        if len(aligned)>=2:
            if ppcm(aligned)>tps:
                return is_sol, ppcm(aligned)
            else:
                return is_sol, step
        else:
            return is_sol, step
    else:
        return True, step


all_buses = lines[1].split(",")
all_buses[-1] = all_buses[-1][:-1]  # To remove the '\n' character
max_ID = max(buses)
max_index = all_buses.index(str(max_ID))
buses_available = [0]*len(all_buses)  # contains the departure time of each bus
# To report "x" buses on our solution list
for i in range(len(all_buses)):
    if all_buses[i]=="x":
        buses_available[i]="x"

tps = 0  # current time
is_sol = False
step = max_ID
while not(is_sol) or tps==0 :
    tps+=step
    previous_buses = all_buses[:max_index]  # Previous buses
    next_buses = all_buses[max_index:]  # Next Buses
    for i in range(len(previous_buses)):  # For each bus before it
        if buses_available[i]!="x":
            buses_available[i] = tps - len(previous_buses)+i
    for j in range(len(next_buses)):  # For each bus after it
        if buses_available[max_index+j]!="x":
            buses_available[max_index+j] = tps + j
    is_sol, step = is_solution(buses_available, all_buses, step)

print("There is the schedule :", buses_available)
print("Therefore timestamp is", buses_available[0])
