import sys
import re

def main():
    dataset = load_file()
    group_data = []
    answers = 0
    for x in dataset:
        if x  == "":
            answers += handle_data( group_data )
            group_data = []
            continue
        else:
            group_data.append(x)
    print( answers )

def handle_data( data ):

    
    final_list = []
    for i in data:
        temp_list = set([char for char in i])
        final_list.append( temp_list )

    if len( final_list) > 0:
        resp = final_list[0].intersection(*final_list)
    else: 
        return 0

    return len(resp)



def load_file():
    try: 
        return [line.rstrip() for line in open('d6.txt')]
    except:
        print( "it's fucked mate")

if __name__ == "__main__":
    main()
