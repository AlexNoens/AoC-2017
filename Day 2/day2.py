from aocd import get_data

raw_data = get_data(day=2, year=2017)


def Part_1():
    string1 = "5 9 2 8"
    string2 = "9 4 7 3"
    string3 = "3 8 6 5"

    test_input = [string1.split(" "), string2.split(" "), string3.split(" ")]
    data = [line.split("\t") for line in raw_data.split("\n")]

    print(data)

    sum = 0
    for row in data:
        int_row = [int(value) for value in row]
        sum += max(int_row) - min(int_row)

    print(sum)


def part_2():
    string1 = "5 9 2 8"
    string2 = "9 4 7 3"
    string3 = "3 8 6 5"

    test_input = [string1.split(" "), string2.split(" "), string3.split(" ")]
    data = [line.split("\t") for line in raw_data.split("\n")]

    print(data)

    sum = 0
    for row in data:
        int_row = [int(value) for value in row]
        for i in range(0, len(int_row)):
            for y in range(i + 1, len(int_row)):
                if max(int_row[y], int_row[i]) % min(int_row[y], int_row[i]) == 0:
                    sum += max(int_row[y], int_row[i]) / min(int_row[y], int_row[i])

    print(sum)


if __name__ == "__main__":
    part_2()
