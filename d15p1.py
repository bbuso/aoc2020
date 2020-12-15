import re


def main():
    x = dataset[0]
    data = x.split(",")
    for i in range(len(data)):
        data[i] = int(data[i])
    last_number = data[-1]

    while len(data) < 50:
        # for x in range(10):
        last_number = data[-1]
        new_number = 0
        # if last_number in data[:-1]:
        try:
            # rdata = data[:-1][-1::-1].index(last_number)
            rdata = data[:-1][-1::-1]
            new_number = rdata.index(last_number) + 1
        except ValueError:
            new_number = 0
        data.append(new_number)
        print(new_number)
    print(data[-1])


def load_file():
    try:
        return [
            line.rstrip() for line in open("C:\\Users\\brbus\\git\\aoc2020\\input.txt")
        ]
    except:
        print("it's fucked mate")


dataset = load_file()

if __name__ == "__main__":
    main()
