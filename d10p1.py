import re


def main():
    dataset = sorted(old_dataset)
    ones = 1
    threes = 1
    for x in range(len(dataset) - 1):
        print(dataset[x], dataset[x + 1])
        if abs(dataset[x] - dataset[x + 1]) == 1:
            ones += 1
        if abs(dataset[x] - dataset[x + 1]) == 3:
            threes += 1
    print(threes * ones)


def load_file():
    try:
        return [line.rstrip() for line in open("input.txt")]
    except:
        print("it's fucked mate")


old_dataset = load_file()
for i in range(0, len(old_dataset)):
    old_dataset[i] = int(old_dataset[i])

if __name__ == "__main__":
    main()
