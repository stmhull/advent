#!usr/bin/python3
with open("day3_input.txt", "r") as f:
    lines = ["".join(line.split()) for line in f.readlines()]


def find_trees(slope):
    xpos = slope[0]
    ypos = slope[1]
    count = 0
    while ypos < len(lines):
        if lines[ypos][xpos % len(lines[0])] == "#":
            count += 1
        xpos += slope[0]
        ypos += slope[1]
    
    return count

print("part 1", find_trees((3, 1)))
print("part 2", find_trees((1, 1)) * find_trees((3, 1)) * find_trees((5, 1)) * find_trees((7, 1)) * find_trees((1, 2)))