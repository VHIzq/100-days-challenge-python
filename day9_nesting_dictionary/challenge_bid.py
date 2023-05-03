import logo

print(logo.logo)
more_auctions = True
auction = {}

def find_highest_bid(bidding_record):
  hightest_bid = 0
  winner = ''
  
  for bidder in bidding_record:
    bidder_anmount = bidding_record[bidder]
    if bidder_anmount > hightest_bid:
      hightest_bid = bidder_anmount
      winner = bidder
  print(f'The winner is {winner} with a BID of {hightest_bid}.')

while more_auctions:
  name = input('Introduce yourn name: ')
  bid = int(input('What is your BID: $'))
  more_people = input('Are there any others bidders? Type "yes" or "no" ')
  auction[name] = bid

  if more_people == 'no':
    more_auctions = False
    find_highest_bid(auction)
    
    """ win_bidder = max([i for i in auction.values()])
    win_name = max(auction, key=auction.get)
winner = f'THe winner is {win_name} with a BID of {win_bidder} '
print(winner) """ 