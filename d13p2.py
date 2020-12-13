import re
from math import gcd


def main():

    baseTimes = dataset[1].split(",")
    solution = False
    intList = []
    for x in range(len(baseTimes)):
        if baseTimes[x] == "x":
            continue
        baseNo = int(baseTimes[x])
        if not solution:
            solution = baseNo
            intList.append(baseNo)
            continue
        lcm = get_lcm(intList)
        print(solution % baseNo)
        while (solution + x) % baseNo != 0:
            solution += lcm
        intList.append(baseNo)
    if check_answer(solution, baseTimes):
        print(solution)


def check_answer(solution, busTimes):
    for x in range(len(busTimes)):
        if busTimes[x] == "x":
            continue
        time = int(busTimes[x])
        if (solution + x) % time == 0:
            continue
        else:
            return False

    return True


def get_lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def load_file():
    try:
        return [line.rstrip() for line in open("input.txt")]
    except:
        print("it's fucked mate")


dataset = load_file()

if __name__ == "__main__":
    main()
