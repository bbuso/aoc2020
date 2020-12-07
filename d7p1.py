import sys
import re


def main():
    dataset = load_file()
    valid_bags = ["shiny gold"]
    while True:
        last_count = len(set(valid_bags))
        for x in dataset:
            resp = handle_data(x, valid_bags)
            if resp != None:
                valid_bags.append(resp)
        if len(set(valid_bags)) == last_count:
            print(len(set(valid_bags))
            break
        else:
            print("last count: " + str(last_count))
            print("current count: " + str(len(valid_bags)))


def handle_data(data, valid_bags):
    """
    load data
    """
    valid_bags
    valid_string = "(" + "|".join(valid_bags) + ")"
    if re.search("contain (\d* \w* \w* bags?, )*(\d " + valid_string + ")", data):
        get_new = re.search("(\\w* \\w* )bags contain \d+ ", data)
        try:
            return get_new.group(1)
        except:
            print("eof")


def load_file():
    try:
        return [line.rstrip() for line in open("d7.txt")]
    except:
        print("it's fucked mate")


if __name__ == "__main__":
    main()
