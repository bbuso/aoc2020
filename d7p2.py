import sys
import re


def main():
    dataset = load_file()
    total_bags = get_contained_bags("shiny gold", dataset)
    print(total_bags)


def get_contained_bags(bag_string, data):
    final_query = bag_string + " bags contain no other bags"
    sub_query = bag_string + " bags contain (.*)"
    for x in data:
        if re.search(final_query, x):
            return 1
        if (bags := re.search(sub_query, x)) :
            contained_bags = bags.group(1)
            bag_array = contained_bags.split(", ")
            returned_bags = 1
            for y in bag_array:
                base_bags = int(y[0])
                bag_rex = re.search("(\\w* \\w*) bags?", y)
                bag_type = bag_rex.group(1)
                returned_bags += base_bags * get_contained_bags(bag_type, data)
            return returned_bags


def load_file():
    try:
        return [line.rstrip() for line in open("d7.txt")]
    except:
        print("it's fucked mate")


if __name__ == "__main__":
    main()
