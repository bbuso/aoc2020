import re
import math


def main():
    wayX = 10
    wayY = 1
    xpos = 0
    ypos = 0
    for x in dataset:

        order = x[0]
        value = int(x[1:])
        if order == "N":
            wayY += value
        elif order == "S":
            wayY -= value
        elif order == "E":
            wayX += value
        elif order == "W":
            wayX -= value
        elif order == "F":
            xpos += wayX * value
            ypos += wayY * value
        elif order == "L":
            value = 360 - value
            wayX, wayY = rotate_waypoint(value, wayX, wayY)
        else:
            wayX, wayY = rotate_waypoint(value, wayX, wayY)
        print(x, xpos, ypos)
    print(abs(xpos) + abs(ypos))


def rotate_waypoint(degree, xpos, ypos):
    if degree == 180:
        return -1 * xpos, -1 * ypos
    elif degree == 90:
        newX = ypos
        newY = -1 * xpos
        return newX, newY
    elif degree == 270:
        newX = -1 * ypos
        newY = xpos
        return newX, newY


def load_file():
    try:
        return [line.rstrip() for line in open("input.txt")]
    except:
        print("it's fucked mate")


dataset = load_file()

if __name__ == "__main__":
    main()
