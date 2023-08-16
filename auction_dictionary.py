import os
os.system('cls')
auction_list = {}
decision = True
while(decision == True):
    name = input("Enter your name  :")
    bid_amount = int(input("your bid amount :"))
    auction_list[name] = bid_amount
    decision = input("Is there anyone else who want to participate in the bidding, type yes or no    :")
    if(decision == "yes"):
        decision = True
    else:
        decision = False
    os.system('cls')

winner = ''
max_bid = 0
for key in auction_list:
    if (auction_list[key] > max_bid):
        max_bid = auction_list[key]
        winner = key

print(f"The winner of the bid is........\n {winner},and the amount is {auction_list[winner]}")

