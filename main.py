from replit import clear
from art import logo

print(logo)
bidding_finished = False
bids = {}


def find_highest_bidder(bidding_record):
    name = ""
    max = 0
    for key in bidding_record:
        bid_amount = bidding_record[key]
        if bid_amount > max:
            max = bid_amount
            name = key
    print(f"The winner is {name} with a bid of ${max}")


while not bidding_finished:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bids[bidder_name] = bid_amount
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

# my_dict ={"Java":100, "Python":112, "C":11}

# key_list = list(my_dict.keys())
# value_list = list(my_dict.values())
# position = value_list.index(112)
# key = key_list[position]
# print(position)
# print(key)