from art import logo
print(logo)
auction = {}

def inputs():
    name = input("YOUR NAME HERE: \n")
    price = int(input("How much do you want to bid: \n"))
    auction[name] = price

inputs()

bid = input("Anyone else want to add a bid? ").lower()

while bid == "yes":
    inputs()
    bid = input("Anyone else want to add a bid? ").lower()

highest_bid = 0
winner = ""

for name in auction:
    if auction[name] > highest_bid:
        highest_bid = auction[name]
        winner = name

print(f"The winner is {winner} with a bid of ₹{highest_bid}")

