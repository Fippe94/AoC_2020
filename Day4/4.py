f = open("Day4/input.txt")
data = f.readlines()
required_fields = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid_hcl = "0123456789abcdef"
valid_ecl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def check_valid_passport(passport):
        valid = True
        for field in required_fields:
                if field in current_passport:
                        if not check_valid_field(field, current_passport[field]):
                                valid = False
                                break
                else:
                        valid = False
                        break
        return valid

def check_valid_field(field, value):
        if field == 'byr':
                return value.isnumeric() and 1920 <= int(value) <= 2002
        elif field == "iyr":
                return value.isnumeric() and 2010 <= int(value) <= 2020
        elif field == "eyr":
                return value.isnumeric() and 2020 <= int(value) <= 2030
        elif field == "hgt":
                unit = value[-2:]
                if unit == "cm":
                        return value[:-2].isnumeric() and 150 <= int(value[:-2]) <= 193
                elif unit == "in":
                        return value[:-2].isnumeric() and 59 <= int(value[:-2]) <= 76
                else:
                        return False
        elif field == "hcl":
                if value[0] == "#":
                        for c in value[1:]:
                                if c not in valid_hcl:
                                        return False
                        return True
                else:
                        return False
        elif field == "ecl":
                return value in valid_ecl
        elif field == "pid":
                return len(value) == 9 and value.isnumeric()
        else:
                return True

counter = 0
passports = []
current_passport = {}
for line in data:
        if line.strip() == "":
                passports.append(current_passport)
                if check_valid_passport(current_passport):
                        counter += 1
                current_passport = {}
                continue
        fields = line.split()
        for field in fields:
                split_field = field.split(":")
                current_passport[split_field[0]] = split_field[1]

passports.append(current_passport)
if check_valid_passport(current_passport):
        counter += 1

print(counter)
             
