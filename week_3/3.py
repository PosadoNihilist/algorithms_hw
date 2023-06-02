def reverse_odd_list(lst):
    new_lst = []
    for i in range(len(lst)):
        if (i % 2) != 0:
            new_lst.append(lst[-(i)])
        else:
            new_lst.append(i)
    return(new_lst)