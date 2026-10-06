with open("checksum_sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

    total = 0
    lines = [line.strip() for line in lines]

    for line in lines:
        the_line = line.split(" ")
        print(the_line)
        amount = len(the_line)
        for i in range(amount):
            the_line[i] = int(the_line[i])
        biggest = max(the_line)
        smallest = min(the_line)
        total = total + int(biggest - smallest)
        print(int(biggest - smallest))

    print(total)



