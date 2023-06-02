import random

with open("lines.txt", encoding="UTF-8") as file_in:
    line = next(file_in)
    for num, aline in enumerate(file_in, 2):
        if random.randrange(num):
            continue
        line = aline
    print(line)