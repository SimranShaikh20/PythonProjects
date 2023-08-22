import os
def findBidder(bidderData):
    highestBid=0
    for bidder in bidderData:
        bidding_price=bidderDetails[bidder]
        if bidding_price>highestBid:
         highestBid=bidding_price
         win=bidder
    print(f'Winner {win} and price is{highestBid}')

bidderDetails={}
chc=False
while not chc:
    name=input("Enter name :")
    bid_price=int(input("Enter bid price : "))
    bidderDetails[name]=bid_price
    moreBidder=input("are more bidder ?")
    if moreBidder=='no':
        chc=True
        findBidder(bidderDetails)
    elif moreBidder=='yes':
        findBidder(bidderDetails)
        os.system('cls')    


 