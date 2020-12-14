import re


def main():
    mask = ""
    mem = {}
    for x in dataset:
        if x[0:4] == "mask":
            mask = x[7:]
        else:
            _, value_in_dec_str = x.split("= ")
            mem_address_re = re.search("\\[(\\d+)\\]", x)
            mem_address = mem_address_re.group(1)
            value_in_dec = int(value_in_dec_str)
            value_in_bin = bin(value_in_dec)[2:]
            while len(value_in_bin) < len(mask):
                value_in_bin = "0" + value_in_bin
            mem[mem_address] = mask_bits(mask, value_in_bin)
    total_sum = 0
    for x in mem.values():
        total_sum += int(x, 2)
    print(total_sum)


def mask_bits(mask, value):
    newVal = ""
    for x in range(len(mask)):
        if mask[x] != "X":
            newVal += mask[x]
        else:
            newVal += value[x]
    return newVal


def load_file():
    try:
        return [line.rstrip() for line in open("input.txt")]
    except:
        print("it's fucked mate")


dataset = load_file()

if __name__ == "__main__":
    main()
