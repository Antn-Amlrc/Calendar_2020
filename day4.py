file = open('input4.txt', "r")
lines = file.readlines()
file.close()
lines.append("\n")

# PART 2 function

def test_key_criteria(key, content):
    if key=="byr":
        return len(content)==4 and int(content)>=1920 and int(content)<=2002
    elif key=="iyr":
        return len(content)==4 and int(content)>=2010 and int(content)<=2020
    elif key=="eyr":
        return len(content)==4 and int(content)>=2020 and int(content)<=2030
    elif key=="hgt":
        sz, oper = content[:-2], content[-2:]
        if oper=="cm":
            return int(sz)>=150 and int(sz)<=193
        elif oper=="in":
            return int(sz)>=59 and int(sz)<=76
        else:
            return False
    elif key=="ecl":
        eyes_color = ["amb","blu","brn","gry","grn","hzl","oth"]
        return content in eyes_color
    elif key=="hcl":
        if len(content)!=7 or content[0]!='#':
            return False
        for c in content[1:]:
            if not(48<=ord(c)<=57 or 97<=ord(c)<=102): # ASCII values for '0'-'9' and 'a'-'f'
                return False
        return True
    elif key=="pid":
        if len(content)!=9:
            return False
        for c in content:
            if not(48<=ord(c)<=57): # ASCII values for '0'-'9'
                return False
        return True
    else:
        return True

# PART 1

# '\n' alone means blank lines
attributes = set(["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"])
valid_passeports, good_passport = 0, True
for line in lines:
    if line=="\n":
        if (attributes == set(["cid"]) or attributes==set()) and good_passport:
            valid_passeports+=1
        # New passeport
        attributes = set(["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"])
        good_passport = True
    else:
        if good_passport:
            retrieve = line.split()
            local_attributes = set()  # empty set
            # Recover only field names
            for criteria in retrieve:
                key, content = criteria.split(':')
                local_attributes.add(key)  # Retrieve only the field name
                if not(test_key_criteria(key, content)):
                    good_passport = False
                    break # No need to check the rest of the fields
            attributes = attributes - local_attributes
print("There are", valid_passeports, "valid passeports.")
