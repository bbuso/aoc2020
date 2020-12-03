import sys

def main():
    dataset = load_file()
    row = 0
    trees = 0
    right_iter = 3
    length = 31
    for x in dataset:
        string, _ = x.split('\n')
        position = row*right_iter + 1
        if string[(position%length)-1] == "#":
            trees += 1
        
        row += 1
    print(trees)


def load_file():
    try: 
        input_file = open( "garbage.txt", "r")
        output_list = input_file.readlines()
        input_file.close()
        return output_list

if __name__ == "__main__":
    main()
