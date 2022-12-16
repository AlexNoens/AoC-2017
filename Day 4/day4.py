from aocd import get_data
import math

def part_1():
	raw_data = get_data(day=4, year=2017)

	data = [line.split(" ") for line in raw_data.split("\n")]
	num_valid = 0
	for line in data:
		count = {}
		for word in line:
			word = ''.join(sorted(word))
			print(word)
			if word in count:
				num_valid -= 1
				break

			count[word] = 1

		num_valid += 1

	print(num_valid)




if __name__ == "__main__":
	part_1()