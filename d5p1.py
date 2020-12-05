import sys
import re

def main():
    dataset = load_file()

    seats = {}

    for x in dataset:
        seatId = getSeatId( x )
        seats[seatId] = x
    highest = max(seats.keys())
    print( "max seat is " + str(highest) + "w / " + seats[highest])


def getSeatId( encoded_seat):
    row = encoded_seat[0:7]
    col = encoded_seat[7:10]

    colNum = 0
    rowNum = 0
    for x in range(len(col)):
        if col[x]== "R":
            colNum += 2**(2-x)
    for x in range(len(row)):
        if row[x]== "B":
            rowNum += 2**(len(row)-x-1)

    return(8*rowNum + colNum)
def load_file():
    try: 
        return [line.rstrip() for line in open('d5.txt')]
    except:
        print( "it's fucked mate")

if __name__ == "__main__":
    main()
