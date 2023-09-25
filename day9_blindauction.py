from replit import clear
from art import logo
import random

print(logo)
print("Welcome To The Secret Blind Auction")

items_list = ["painting", "car", "computer", "house", "motorcycle"]
item = random.choice(items_list)

print(f"Today, the first item will be auctioning off is a {item}. ")
print("Let's start the bidding now!")

names_list = []
bids_list = []

def blind_auction():
  more_bids = True
  while more_bids == True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    next_bidder = input(f"Thank you {name}. Is there another bidder?: ").lower()

    names_list.append(name)
    bids_list.append(bid)

    if next_bidder == "no":
      more_bids = False
    elif next_bidder == "yes":
      clear()

blind_auction()
# ----------------------------------------------------

auction_dictionary = {}

x = 0
for name in names_list:
    auction_dictionary[name] = bids_list[x]
    x += 1

winning_bidder = max(auction_dictionary, key = auction_dictionary.get)
winning_bid = auction_dictionary[winning_bidder]

print(f"Congratulations, {winning_bidder}, you won the auction with a bid of {winning_bid} dollars. ")