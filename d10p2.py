import math


def main():
    permutations = 1
    x = 0
    y = 1
    while x < len(dataset):
        y = 1
        if x + y == len(dataset):
            break
        while dataset[x + y] - dataset[x] == y:
            y += 1
            if x + y == len(dataset):
                break
        permutations *= math.comb(y - 1, 2) + 1
        x += y
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
