def reverse_list(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[-(i+1)])
    return(new_lst)
