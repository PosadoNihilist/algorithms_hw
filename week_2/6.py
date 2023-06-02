import csv
longest_dict = {} 
perma_dict = {}
lumi_list = [100000]
curr_longest = 0
curr_length = 0
with open('alpha_oriona.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for log in list(reader):
        lumi = int(log["luminosity"])
        date = log["date"]
        time = log["time"]
        lumi_list.append(lumi)
        if lumi_list[-2] < lumi:
            longest_dict = {}
            curr_length = 0
        longest_dict.update({curr_length: [date, time]})
        curr_length += 1
        if curr_length > curr_longest:
            curr_longest = curr_length
            perma_dict = dict(longest_dict)
    print(len(perma_dict))
    print(str(list(perma_dict.values())[0][0]) +" "+  str(list(perma_dict.values())[0][1]))
