import itertools

trash = input()

types = ["пик", "треф", "бубен", "червей"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет","дама","король","туз"]

index = types.index(trash)
types.pop(index)

answer = list(itertools.product(numbers, types))
for line in answer:
    print(line[0] + " " + line[1])
