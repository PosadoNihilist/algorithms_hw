import sys

first_line = input()
first_list = first_line.lstrip("\t").split("\t")
trash_list = []
stores_list = []
for i in range(len(first_list)):
    trash_list.append([])
complete_dict = dict(zip(first_list, trash_list))
stores_dict = {}
for line in sys.stdin:
    if line == "\n":
        best_store = (min(stores_dict, key=stores_dict.get))
        index = stores_list.index(best_store)
        print(best_store)
        for key, value in complete_dict.items():
            price_in_store = value[index]
            print(str(key) + " " + str(price_in_store))
    line_list = line.split("\t")
    store_name = line_list.pop(0)
    stores_list.append(store_name)
    total_price = 0
    for count, price in enumerate(line_list):
        price = int(price)
        total_price+=price
        book = first_list[count]
        complete_dict[book].append(price)
    stores_dict.update({store_name: total_price})
    