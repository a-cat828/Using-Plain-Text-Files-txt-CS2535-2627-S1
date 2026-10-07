with open("checksum_input.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    total_line = [0] * len(lines)
    total = 0
    lines = [line.strip() for line in lines]
    line_num = -1
    for line in lines:
        line_num += 1
        the_line = line.split(" ")
        print(the_line)
        amount = len(the_line)
        for i in range(amount):
            the_line[i] = int(the_line[i])
        biggest = max(the_line)
        smallest = min(the_line)
        total = total + int(biggest - smallest)
        print(int(biggest - smallest))
        total_line[line_num] = int(biggest - smallest)

    print(total)
with open("checksum_results.txt", "w") as file:
    for i in range(line_num+1):
        file.write(f"{str(total_line[i])}\n")
    file.write(f"{str(total)}\n")


