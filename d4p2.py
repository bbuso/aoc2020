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
        "hgt:(1([5-8][0-9]|9[0-3])cm|((59)|(6[0-9])|(7[0-6]))in) ",

        "eyr:20(30|2[0-9]) ",
        "byr:(19[2-9][0-9]|200[0-2]) ",
        "iyr:20(20|1[0-9]) ",
        "hcl:#[0-9a-f]{6} ",
        "ecl:(amb|blu|brn|gry|grn|hzl|oth) ",
        "pid:\\d{9} ",
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
