#!usr/bin/python3
with open("day1_input.txt", "r") as f:
    strings = f.readlines()
    input = sorted(int(string) for string in strings)


def part_1():
    for i in input:
        for j in input:
            if 2020 - i - j < 0:
                break
            elif 2020 - i - j == 0:
                return i * j


def part_2():
    for i in input:
        for j in input:
            if 2020 - i - j > 0:
                for k in input:
                    if 2020 - i - j - k == 0:
                        return i * j * k
                    


print("part 1:", part_1())
print("part 2:", part_2())