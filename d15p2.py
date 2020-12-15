import re


def main():
    x = dataset[0]
    s_data = x.split(",")
    data = {}
    for i in range(len(s_data)):
        data[int(s_data[i])] = i
    count = len(s_data) + 1
    if not (s_data[-1] in s_data[:-1]):
        current_number = 0
    else:
        rdata = s_data[:-1][-1::-1]
        current_number = rdata.index(data[-1]) + 1
    while count < 30000000:
        if current_number in data.keys():
            last_showed = data[current_number]
            difference = count - last_showed - 1
            data[current_number] = count - 1
            current_number = difference
        else:
            data[current_number] = count - 1
            current_number = 0
        count += 1

    print(current_number)


def load_file():
    try:
        return [line.rstrip() for line in open("input.txt", "r")]
    except:
        print("it's fucked mate")


dataset = load_file()

if __name__ == "__main__":
    main()
