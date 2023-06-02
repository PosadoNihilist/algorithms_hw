import sys
import math
ranges_dict = {}
ranges_list = []
for line in sys.stdin:
    if line == "\n":
        sorted_ranges = sorted(ranges_list)
        print(sorted_ranges)
        for elem in sorted_ranges:
            print(str(elem[0]) + " - " + str(elem[1]) + ": " + ", ".join(sorted(ranges_dict[elem])))
    else:
        line_list = line.split(" ")
        capital = line_list[0]
        population = int(line_list[2])
        minim = math.floor(population / 100000) * 100
        maxim = math.ceil(population / 100000) * 100
        minim_maxim = (minim, maxim)
        if minim_maxim not in ranges_list:
            ranges_list.append(minim_maxim)
            ranges_dict.update({minim_maxim: [capital]})
        else:
            ranges_dict[minim_maxim].append(capital)
