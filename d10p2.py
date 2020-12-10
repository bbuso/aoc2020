import math


def main():
    permutations = 1
    row = 0
    while row < len(dataset):
        rows_ahead = 1
        if row + rows_ahead == len(dataset):
            break
        while dataset[row + rows_ahead] - dataset[row] == rows_ahead:
            rows_ahead += 1
            if row + rows_ahead == len(dataset):
                break
        permutations *= math.comb(rows_ahead - 1, 2) + 1
        row += rows_ahead
    print(permutations)


def load_file():
    try:
        return [line.rstrip() for line in open("input.txt")]
    except:
        print("it's fucked mate")


old_dataset = load_file()
for i in range(0, len(old_dataset)):
    old_dataset[i] = int(old_dataset[i])
dataset = sorted(old_dataset)
if __name__ == "__main__":
    main()
