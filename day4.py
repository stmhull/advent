#!/usr/bin/python3
import re

with open("day4_input.txt", "r") as f:
    txt = f.readlines()
    data = []
    passport = {}

    for line in txt:
        if line == '\n':
            data.append(passport)
            passport = {}
        else:
            line = " ".join(line.split())
            line_list = line.split(" ")
            for element in line_list:
                pair = element.split(":")
                passport[pair[0]] = pair[1]

    data.append(passport)


CODES = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def passportHasKeys(passport):
    keys = set(passport.keys())
    return len(keys.intersection(CODES)) == 7


def isValidYear(str, range):
    return re.fullmatch(r'^\d{4}', str) and (int(str) >= range[0] and int(str) <= range[1])


def isValidHeight(str):
    if str[-2:] == "in":
        digits = str.replace("in", "")
        return int(digits) >= 59 and int(digits) <= 76
    elif str[-2:] == "cm":
        digits = str.replace("cm", "")
        return int(digits) >= 150 and int(digits) <= 193
    return False


def passportDataIsValid(passport):
    validator = {
        "byr": lambda x: isValidYear(x, (1920, 2002)),
        "iyr": lambda x: isValidYear(x, (2010, 2020)),
        "eyr": lambda x: isValidYear(x, (2020, 2030)),
        "hgt": lambda x: isValidHeight(x),
        "hcl": lambda x: re.fullmatch(r'#[0-9a-f]{6}', x),
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: re.fullmatch(r'[0-9]{9}', x),
        "cid": lambda x: True
    }
    
    for key in passport.keys():
        if not validator[key](passport[key]):
            return False
    return True


def part1():
    valid = 0
    for passport in data:
        if passportHasKeys(passport):
            valid += 1
    
    return valid


def part2():
    valid = 0
    for passport in data:
        if passportDataIsValid(passport) and passportHasKeys(passport):
            valid += 1
    return valid
    

print("day 1:", part1())
print("day 2:", part2())