import random

def startGame():
    profit = 0
    for i in range(10):
        
        print("ROUND ", i+1)
        
        #generating 10 random cards and finding the value of the sum
        cards = []
        for i in range(10):
            cards.append(random.randint(1,100))
        
        underlying = sum(cards)
        
        #Revealing One Card
        print("[",cards[0],"] [] [] [] [] [] [] [] [] []")
        
        #generating opponent scores
        players = []
        bids = []
        asks = []
        opp_bid_asks = []
        for i in range(4):
            opp_ask = round(random.randint(1,1000),-1)
            opp_bid = round(opp_ask - random.randint(1,opp_ask),-1)
            while (opp_ask == opp_bid):
                opp_ask = round(random.randint(1,1000),-1)
                opp_bid = round(opp_ask - random.randint(1,opp_ask),-1)
    
            opp_bid_asks.append((opp_bid,opp_ask))
            bids.append(opp_bid)
            asks.append(opp_ask)
        
        lowest_ask = min(asks)
        highest_bid = max(bids)
            
        #prompting user to enter bid ask spread
        print("Enter your bid ask spread (eg:5,10)")
        bid_ask = input()
        bid_ask = bid_ask.split(",")
        bid = int(bid_ask[0])
        ask = int(bid_ask[1])
        
        round_profit = 0
        ask_taken = False
        bid_taken = False
        
        if ask < lowest_ask:
            ask_taken = True
            round_profit += (ask - underlying)
            profit += (ask - underlying)
        
        if bid > highest_bid:
            bid_taken = True
            round_profit += (underlying - bid)
            profit += (underlying - bid)
        
        print("Underlying: ", underlying)
        print("Opponent Spreads: ", opp_bid_asks)
        
        if ask_taken:
            print("Lead trader has taken your ask of", ask)
        if bid_taken:
            print("Lead trader has taken your bid of", bid)
        
        print("Round Profit: ", round_profit)
        print("\n")
    
    print("Total Profit: ", profit)
