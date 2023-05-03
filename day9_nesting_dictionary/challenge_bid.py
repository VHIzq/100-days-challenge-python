import logo

print(logo.logo)
more_auctions = True
auction = {}

while more_auctions:
  name = input('Introduce yourn name: ')
  bid = int(input('What is your BID: $'))
  more_people = input('Are there any others bidders? Type "yes" or "no" ')
  auction[name] = bid

  if more_people == 'no':
    more_auctions = False
    
    win_bidder = max([i for i in auction.values()])
    win_name = max(auction, key=auction.get)
winner = f'THe winner is {win_name} with a BID of {win_bidder} '
print(winner)