#Instructions:
#10 cards with numbers 1-100 will be drawn
#Each round one card will be revealed and you need to make a market on the sum of the 10 cards 
#You are competing against other market makers for an external trader to accept your bids/asks
#Pass 1 or 2 into the startGame function to set the intelligence of the opponnents
#Passing 1 means opponents will quote random spreads, passing 2 means they will try to play optimally

import random

def startGame(opponent_intelligence):
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
        
        #generating opponent spreads
        bids = []
        asks = []
        opp_bid_asks = []
        for i in range(6):
            #spreads for unintelligent opponents
            if opponent_intelligence == 1:
                opp_ask = round(random.randint(1,1000),-1)
                opp_bid = round(opp_ask - random.randint(1,opp_ask),-1)
                while (opp_ask == opp_bid):
                    opp_ask = round(random.randint(1,1000),-1)
                    opp_bid = round(opp_ask - random.randint(1,opp_ask),-1)
            #spreads for more aware opponents
            elif opponent_intelligence == 2:
                opp_guess = int(454.5 + cards[0] + random.randint(-50,50))
                opp_bid = round(opp_guess - random.randint(1,opp_guess),-1)
                opp_ask = min(1000,round(opp_guess + (opp_guess - opp_bid),-1))
    
            opp_bid_asks.append((opp_bid,opp_ask))
            bids.append(opp_bid)
            asks.append(opp_ask)
        
        lowest_ask = min(asks)
        highest_bid = max(bids)
            
        #prompting user to enter bid ask spread
        print("Enter your bid ask spread (eg:5,10)")
        while True:
            try:
                bid_ask = input()
                bid_ask = bid_ask.split(",")
                bid = int(bid_ask[0])
                ask = int(bid_ask[1])
                break
            except:
                print("Invalid Input - Enter your spread in the form : bid,ask")
        
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
