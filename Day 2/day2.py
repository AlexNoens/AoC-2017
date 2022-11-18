from aocd import get_data
raw_data = get_data(day=2, year=2017)

string1 = "5 1 9 5"
string2 = "7 5 3"
string3 = "2 4 6 8"

test_input = [string1.split(" "), string2.split(" "), string3.split(" ")]
data = [line.split("\t") for line in raw_data.split("\n")]
print(data)

sum = 0
for row in data:
    sum += int(max(row)) - int(min(row))

print(sum)
