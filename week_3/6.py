transactions_dict = {}


def get_transactions(t):
    if t == "print_it\n":
        for key, value in transactions_dict.items():
            print(str(len(value)) + " " + key + " "+ str(sum(value)))
    else:
        new = t.split("-")
        both = new[1].split(":")
        trans_type, amount = both[0], int(both[1])
        if trans_type not in transactions_dict:
            transactions_dict[trans_type] = [amount]
        else:
            transactions_dict[trans_type].append(amount)
    
import sys
for line in sys.stdin:
    get_transactions(line)