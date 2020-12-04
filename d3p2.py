import sys

def main():
    dataset = load_file()
    iterants = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2],
    ]

    resp = 1
    for x in iterants:
        resp = resp*get_trees( x[0], x[1], dataset )
    
    print(resp)

def get_trees( x_coord, y_coord, dataset  ):
    row = 0
    trees = 0
    length = 31
    for x in dataset:
        if y_coord == 2 and row %2 == 1:
            row += 1
            continue
        position = row*x_coord
        if x[(position%length)] == "#":
            trees += 1
        
        row += 1
    return trees



def load_file():
    try: 
        return [line.rstrip() for line in open('d4.txt')]
    except:
        print( "it's fucked mate")

if __name__ == "__main__":
    main()
