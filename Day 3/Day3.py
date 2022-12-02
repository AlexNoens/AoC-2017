from aocd import get_data
import math


def part_1():
    raw_data = get_data(day=3, year=2017)
    # raw_data = 1024
    odd_root = math.ceil(math.sqrt(int(raw_data)))

    dist_from_center = math.floor(odd_root / 2)

    thing = int(raw_data) - (odd_root) ** 2

    horiz_dist = abs((thing % (odd_root-1)) - math.floor(odd_root / 2))

    print("root:", odd_root, "Input", raw_data)

    print("ans", dist_from_center + horiz_dist, "hd", horiz_dist)


def part_2():
    print("pt2")
    raw_data = get_data(day=3, year=2017)
    matrix[100][100]
    matrix[50][50] = 1
    step = 1
    while 1:
        # Start at middle position, build out matrix until value is > than input


if __name__ == "__main__":
    part_2()
