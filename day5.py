#!/usr/bin/python3

with open("day5_input.txt", "r") as f:
    lines = f.readlines()
    seats = list(map(lambda x: "".join(x.split()), lines))


def findValue(seat, range):
    lo = "F" if ("F" in seat or "B" in seat) else "L"
    
    if len(seat) == 1:
        return range[0] if seat == lo else range[1]
    
    if seat[0] == lo:
        return findValue(seat[1:], range[:(int(len(range) / 2))])
    
    return findValue(seat[1:], range[(int(len(range) / 2)):])


def getIds():
    return [(findValue(seat[:7], range(0, 128)) * 8) + findValue(seat[7:], range(0, 9)) for seat in seats]

def part2():
    ids = getIds()
    id_range = {x for x in range(48, 819)}
    return list(id_range.difference(ids))[0]


print("part 1:", max(getIds()))
print("part 2:", part2())