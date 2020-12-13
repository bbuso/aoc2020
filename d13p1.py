import re


def main():
    depTime = int(dataset[0])
    baseTimes = dataset[1].split(",")
    finalTimes = {}
    for x in baseTimes:
        if x == "x":
            continue
        intTime = int(x)
        finalTimes[intTime - depTime % intTime] = x
    minKey = min(finalTimes.keys())

    print(int(finalTimes[minKey]) * int(minKey))


def load_file():
    try:
        return [line.rstrip() for line in open("input.txt")]
    except:
        print("it's fucked mate")


dataset = load_file()

if __name__ == "__main__":
    main()
