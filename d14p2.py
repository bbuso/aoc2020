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
            mem_address_int = int(mem_address)
            mem_address_bin = bin(mem_address_int)[2:]
            value_in_dec = int(value_in_dec_str)
            while len(mem_address_bin) < len(mask):
                mem_address_bin = "0" + mem_address_bin
            masked_address = mask_bits(mask, mem_address_bin)
            decoded_addresses = decode_addresses(masked_address)
            for y in decoded_addresses:
                mem[y] = value_in_dec
    total_sum = 0
    for x in mem.values():
        total_sum += x
    print(total_sum)


def decode_addresses(address_to_decode):
    addresses = [""]
    for x in range(len(address_to_decode)):
        if address_to_decode[x] != "X":
            for y in range(len(addresses)):
                addresses[y] += address_to_decode[x]
        else:
            temp_address = []
            for y in addresses:
                old_str = y
                zero_str = old_str + "0"
                one_str = old_str + "1"
                temp_address.append(zero_str)
                temp_address.append(one_str)
            addresses = temp_address

    return addresses


def mask_bits(mask, value):
    newVal = ""
    for x in range(len(mask)):
        if mask[x] == "X":
            newVal += "X"
        elif mask[x] == "1":
            newVal += "1"
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
