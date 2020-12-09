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


def part1():
    max = 0
    for seat in seats:
        row = findValue(seat[:7], range(0, 128))
        column = findValue(seat[7:], range(0, 9))
        max = (row * 8) + column if (row * 8) + column > max else max
    
    return max


def part2():
    ids = [(findValue(seat[:7], range(0, 128)) * 8) + findValue(seat[7:], range(0, 9)) for seat in seats]
    id_range = {x for x in range(48, 819)}
    return id_range.difference(ids)


print("part 1:", part1())
print("part 2:", part2())