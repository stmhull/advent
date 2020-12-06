#!usr/bin/python3

with open("day2_input.txt", "r") as f:
    lines = f.readlines()
    input = [line.split(" ") for line in lines]
    
def part_1():
    valid_count = 0
    
    def count_char(char, string):
        count = 0
        for i in string:
            if i == char:
                count += 1
        return count
    
    for i in input:
        range = i[0].split("-")
        low = int(range[0])
        hi = int(range[1])
        char = i[1][0]
        pw = i[2]
    
        char_count = count_char(char, pw)
    
        if char_count >= low and char_count <= hi:
            valid_count += 1
    
    return valid_count


def part_2():
    valid_count = 0
    
    for entry in input:
        range = entry[0].split("-")
        pos1 = int(range[0])
        pos2 = int(range[1])
        char = entry[1][0]
        password = entry[2]
        
        if (char == password[pos1 - 1]) ^ (char == password[pos2 - 1]):
            valid_count += 1
    
    return valid_count

print("part 1:", part_1())
print("part 2:", part_2())
