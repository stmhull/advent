#!/usr/bin/python3
with open("day6_input.txt", "r") as f:
    txt = f.readlines()
    

def part1():
    data = 0
    answers = ""
    
    for line in txt:
        if line == "\n":
            data += len(set(answers))
            answers = ""
        else:
            answers += "".join(line.split())
    
    answer_set = set(answers)
    data += len(answer_set)
    
    return data


def part2():
    data = 0
    answers = []
    
    for line in txt:
        if line == "\n":
            data += len(set.intersection(*answers))
            answers = []
        else:
            answers.append(set("".join(line.split())))

    data += len(set.intersection(*answers))
    return data
            

print("part 1:", part1())
print("part 2:", part2())