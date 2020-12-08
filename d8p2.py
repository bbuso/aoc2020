import sys
import re


def main():
    total_acc = 0
    row = 0
    completed_rows = []
    eliminated_rows = []
    while True:
        if not (row in completed_rows):
            completed_rows.append(row)
        else:
            break
        command = dataset[row][0:3]
        if command == "acc":
            total_acc += int(dataset[row][4:])
            row += 1
        if command == "jmp":
            row += int(dataset[row][4:])
        if command == "nop":
            row += 1
    for x in completed_rows:
        eliminated_rows.append(run_skip(x))


def run_skip(row_to_skip):
    total_acc = 0
    row = 0
    completed_rows = []
    while True:

        if not (row in completed_rows):
            completed_rows.append(row)
        else:
            break
        if row > len(dataset) - 1:
            print("the correct row is: " + str(row_to_skip))
            print(total_acc)
            break
        command = dataset[row][0:3]
        if row_to_skip == row:
            if command == "jmp":
                command = "nop"
            elif command == "nop":
                command = "jmp"
            else:
                break
        if command == "acc":
            total_acc += int(dataset[row][4:])
            row += 1
        if command == "jmp":
            row += int(dataset[row][4:])
        if command == "nop":
            row += 1

    return row_to_skip


def load_file():
    try:
        return [line.rstrip() for line in open("d8.txt")]
    except:
        print("it's fucked mate")


dataset = load_file()
if __name__ == "__main__":
    main()
