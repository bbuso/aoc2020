import re


def main():
    xpos = 0
    ypos = 0
    heading = "E"
    for x in dataset:

        order = x[0]
        value = int(x[1:])
        if order == "N":
            ypos += value
        elif order == "S":
            ypos -= value
        elif order == "E":
            xpos += value
        elif order == "W":
            xpos -= value
        elif order == "F":
            if heading == "N":
                ypos += value
            elif heading == "S":
                ypos -= value
            elif heading == "E":
                xpos += value
            else:
                xpos -= value
        elif order == "L":
            value = 360 - value
            heading = get_right_heading(heading, value)
        else:
            heading = get_right_heading(heading, value)
        print(x, heading, xpos, ypos)


def get_right_heading(heading, degree):
    if degree == 180:
        if heading == "N":
            return "S"
        elif heading == "S":
            return "N"
        elif heading == "E":
            return "W"
        elif heading == "W":
            return "E"
    elif degree == 90:
        if heading == "N":
            return "E"
        elif heading == "S":
            return "W"
        elif heading == "E":
            return "S"
        elif heading == "W":
            return "N"
    elif degree == 270:
        if heading == "N":
            return "W"
        elif heading == "S":
            return "E"
        elif heading == "E":
            return "N"
        elif heading == "W":
            return "S"


def load_file():
    try:
        return [line.rstrip() for line in open("input.txt")]
    except:
        print("it's fucked mate")


dataset = load_file()

if __name__ == "__main__":
    main()
