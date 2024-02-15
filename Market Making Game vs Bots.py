#Instructions:
#10 cards with numbers 1-100 will be drawn
#Each round one card will be revealed and you need to make a market on the sum of the 10 cards 
#You are competing against other market makers for an external trader to accept your bids/asks
#To start the game run the startGame(n) function where n is the number of opponents

import random

def startGame(n):
    traderPnL = 0
    profit = 0
    
    #HashMap to store all opponents bids,asks and profit
    oppMap = {}
    for i in range(n):
        oppMap[i] = [0,0,0] #[bid,ask,profit]
    
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
        
        asks.append(ask)
        bids.append(bid)
        
        #Generating opponent bids and asks
        for j in range(n):
            opp_guess = int(454.5 + cards[0] + random.randint(-50,50))
            opp_bid = round(opp_guess - random.randint(1,opp_guess),-1)
            opp_ask = min(1000,round(opp_guess + (opp_guess - opp_bid),-1))
            while (opp_ask == opp_bid):
                opp_bid = round(opp_guess - random.randint(1,opp_guess),-1)
                opp_ask = min(1000,round(opp_guess + (opp_guess - opp_bid),-1))
            oppMap[j][0] = opp_bid
            oppMap[j][1] = opp_ask

            opp_bid_asks.append((opp_bid,opp_ask))
            bids.append(opp_bid)
            asks.append(opp_ask)
    
        lowest_ask = min(asks)
        highest_bid = max(bids)
        
        #Determining profit for opponents after round
        for k in range(n):
            if oppMap[k][0] == highest_bid:
                oppMap[k][2] += underlying - highest_bid
                traderPnL += highest_bid - underlying
            if oppMap[k][1] == lowest_ask:
                oppMap[k][2] += lowest_ask - underlying
                traderPnL += underlying - lowest_ask
        
        #Determining profit for player after round
        
        round_profit = 0
        ask_taken = False
        bid_taken = False
        
        if ask == lowest_ask:
            ask_taken = True
            round_profit += (ask - underlying)
            profit += (ask - underlying)
            traderPnL += underlying - lowest_ask
        
        if bid == highest_bid:
            bid_taken = True
            round_profit += (underlying - bid)
            profit += (underlying - bid)
            traderPnL += highest_bid - underlying
        
        #Printing scores and feedback
        print("\n")
        print("Underlying: ", underlying)
        print("Opponent Spreads: ", opp_bid_asks)
        
        if ask_taken:
            print("Lead trader has taken your ask of", ask)
        else:
            print("Lead trader has taken an opponents ask of", lowest_ask)
        if bid_taken:
            print("Lead trader has taken your bid of", bid)
        else:
            print("Lead trader has taken an opponents bid of", highest_bid)
        
        #print("Round Profit: ", round_profit)
        #print("Current Trader PnL:", traderPnL)
        print("\n")
        
        print("Players         |  Profit")
        print("-------------------------")
        print("You             | ",profit)
        for j in range(n):
            print("Market Maker ",j+1,"| ", oppMap[j][2])
        
        print("\n")
    
    print("Total Profit: ", profit)
    print("Trader PnL: ", traderPnL)

startGame(5)
