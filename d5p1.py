import re

def main():
    dataset = load_file()

    seats = {}

    for x in dataset:
        seatId = getSeatId( x )
        seats[seatId] = x
    highest = max(seats.keys())
    print( "max seat is " + str(highest) + " w / " + seats[highest])


def getSeatId( encoded_seat):
    encoded_seat = re.sub("(R|B)", "1", encoded_seat)
    encoded_seat = re.sub("(L|F)", "0", encoded_seat)
    row = encoded_seat[0:7]
    col = encoded_seat[7:10]
    colNum = int(col, 2)
    rowNum = int(row, 2)

    return(8*rowNum + colNum)
def load_file():
    try: 
        return [line.rstrip() for line in open('d5.txt')]
    except:
        print( "it's fucked mate")

if __name__ == "__main__":
    main()
