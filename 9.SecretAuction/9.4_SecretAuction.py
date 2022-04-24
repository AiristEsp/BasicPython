from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
bidding_finish = False

def secret_auction(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finish:
    name = input("What is your name?: ")
    price = int(input("What is your bid?:$ "))
    bids[name] = price
    any_other = input("Are there any other bidders? Type 'yes' or 'no': ")
    
    if any_other == "no":
        bidding_finish = True
        secret_auction(bids)
    elif any_other == "yes":
        clear()
