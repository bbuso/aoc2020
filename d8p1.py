import sys
import re


def main():
    print(len(dataset))
    total_acc = 0
    row = 0
    completed_rows = []
    while True:
        if row in completed_rows:
            break
        else:
            completed_rows.append(row)

        command = dataset[row][0:3]
        if command == "acc":
            total_acc += int(dataset[row][4:])
            row += 1
        if command == "jmp":
            row += int(dataset[row][4:])
        if command == "nop":
            row += 1
    print(total_acc)


def load_file():
    try:
        return [line.rstrip() for line in open("d8.txt")]
    except:
        print("it's fucked mate")


dataset = load_file()
if __name__ == "__main__":
    main()
