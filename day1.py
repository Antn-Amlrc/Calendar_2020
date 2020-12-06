file = open('input1.txt', "r")
lines = file.readlines()
file.close()
YEAR = 2020

# PART 1

for i in range(len(lines)):
    number1 = int(lines[i])
    for j in range(i+1, len(lines)):
        number2 = int(lines[j])
        if number1+number2==YEAR:
            print("The numbers are ", number1, "&", number2,"\n","The entry is :", number1*number2)

# PART 2

for i in range(len(lines)):
    number1 = int(lines[i])
    for j in range(i+1, len(lines)):
        number2 = int(lines[j])
        for k in range(j+1, len(lines)):
            number3 = int(lines[k])
            if number1+number2+number3==YEAR:
                print("The numbers are ", number1, "&", number2,"&",number3,"\n","The entry is :", number1*number2*number3)
