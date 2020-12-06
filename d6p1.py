import sys
import re

def main():
    dataset = load_file()
    group_data = ""
    answers = 0
    for x in dataset:
        if x  == "":
            answers += handle_data( group_data )
            group_data = ""
            continue
        else:
            group_data += "" + x + ""
    print( answers )

def handle_data( data ):
    listchars = [char for char in data]
    print( set(listchars) )
    print(len(set(listchars)))
    return len(set(listchars))



def load_file():
    try: 
        return [line.rstrip() for line in open('d6.txt')]
    except:
        print( "it's fucked mate")

if __name__ == "__main__":
    main()
