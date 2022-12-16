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

def add_adjacent_values(matrix, x, y):
    return matrix[x+1][y] + matrix[x][y+1] + matrix[x+1][y+1] + matrix[x-1][y] + matrix[x][y-1] + matrix[x-1][y-1] + matrix[x+1][y-1] + matrix[x-1][y+1]

def part_2():
    print("pt2")
    raw_data = int(get_data(day=3, year=2017))
    # raw_data = 750
    matrix = [[0 for i in range(100)]for i in range(100)]
    x=0
    y=0
    matrix[x][y] = 1
    step = 0

    while 1:
        step += 1
        if step % 2 == 0:
            for i in range(step):
                x += 1
                matrix[x][y] = add_adjacent_values(matrix,x,y)
                if matrix[x][y] > raw_data:
                    print(matrix[x][y])
                    exit(0)
            for i in range(step):
                y -= 1
                matrix[x][y] = add_adjacent_values(matrix,x,y)
                if matrix[x][y] > raw_data:
                    print(matrix[x][y])
                    exit(0)
        else:
            for i in range(step):
                x -= 1
                matrix[x][y] = add_adjacent_values(matrix,x,y)
                if matrix[x][y] > raw_data:
                    print(matrix[x][y])
                    exit(0)
            for i in range(step):
                y += 1
                matrix[x][y] = add_adjacent_values(matrix,x,y)
                if matrix[x][y] > raw_data:
                    print(matrix[x][y])
                    exit(0)


if __name__ == "__main__":
    part_2()
