from aocd import get_data
import math


def part_1():
    raw_data = get_data(day=3, year=2017)
    # raw_data = 1024
    odd_root = math.ceil(math.sqrt(int(raw_data)))

    dist_from_center = math.floor(odd_root / 2)

    thing = int(raw_data) - (odd_root) ** 2

    horiz_dist = abs((thing % odd_root) - math.floor(odd_root / 2)) - 1

    print("root:", odd_root, "Input", raw_data)

    print("ans", dist_from_center + horiz_dist, "hd", horiz_dist)


def part_2():
    print("pt2")
    raw_data = get_data(day=3, year=2017)
    output = 1
    pre_out = 0
    next = 0
    while output < int(raw_data):
        next = output + pre_out
        pre_out = output
        output = next
        print(output)
    print(output)


if __name__ == "__main__":
    part_2()
