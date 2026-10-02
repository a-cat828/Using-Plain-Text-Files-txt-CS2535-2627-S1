with open("checksum_sample.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split("\n") for line in lines]
    print(lines)