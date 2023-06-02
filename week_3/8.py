def discount_checker(threshold, *purchases):
    disct_list = []
    for i in range(len(purchases)):
        if purchases[i] >= threshold:
            disct_list.append(i+1)
    print(disct_list)
            
discount_checker(1000, 500, 1500, 800, 1200)