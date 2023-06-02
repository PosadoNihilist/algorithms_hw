def more_than_five(lst):
    new_lst = []
    for num in lst:
        if abs(num)>10:
            new_lst.append(num)
    return(new_lst)