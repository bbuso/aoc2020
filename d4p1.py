import sys
import re

def main():
    dataset = load_file()
    group_data = ""
    valid_passwords = 0
    for x in dataset:
        if x  == "":
            valid_passwords += handle_data( group_data )
            group_data = ""
            continue
        else:
            group_data += " " + x + " "
    print( valid_passwords )

def handle_data( data ):
    print( data )
    valid_fields = [
        "hgt:",
        "eyr:",
        "byr:",
        "iyr:",
        "hcl:",
        "ecl:",
        "pid:",
        ]

    for x in valid_fields:
        if not re.search( x, data ):
            return 0

    return 1


def load_file():
    try: 
        return [line.rstrip() for line in open('d4.txt')]
    except:
        print( "it's fucked mate")

if __name__ == "__main__":
    main()
