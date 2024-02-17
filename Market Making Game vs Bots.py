#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Instructions:
#10 cards with numbers 1-100 will be drawn
#Each round one card will be revealed and you need to make a market on the sum of the 10 cards 
#You are competing against other market makers for an external trader to accept your bids/asks
#To start the game run the startGame(n) function where n is the number of opponents

import random

def startGame(n):
    print("There are 10 cards in total. We will reveal one card each round. Your goal is to quote a bid/ask spread")
    print("on the sum of the 10 cards")
    print(" ")
    traderPnL = 0
    profit = 0
    
    #HashMap to store all opponents bids,asks and profit
    oppMap = {}
    for i in range(n):
        oppMap[i] = [0,0,0,0,0] #[bid,ask,profit,bid_vol,ask_vol]
    
    for i in range(10):
        
        print("ROUND ", i+1)
        
        #generating 10 random cards and finding the value of the sum
        cards = []
        for i in range(10):
            cards.append(random.randint(1,100))
        
        underlying = sum(cards)
        
        #Revealing One Card
        print("Revealing One Card: [",cards[0],"]")
        
        #generating opponent spreads
        bids = []
        asks = []
        
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
                
        print("Enter your bid ask volume (eg:1,2)")
        while True:
            try:
                bid_ask_vol = input()
                bid_ask_vol = bid_ask_vol.split(",")
                bid_vol = int(bid_ask_vol[0])
                ask_vol = int(bid_ask_vol[1])
                break
            except:
                print("Invalid Input - Enter your volume in the form : bid volume,ask volume")
        
        asks.append(ask)
        bids.append(bid)
        
        #Generating opponent bids and asks and volume
        for j in range(n):
            opp_guess = int(454.5 + cards[0] + random.randint(-50,50))
            opp_bid = round(opp_guess - random.randint(1,opp_guess),-1)
            opp_ask = min(1000,round(opp_guess + (opp_guess - opp_bid),-1))
            while (opp_ask == opp_bid):
                opp_bid = round(opp_guess - random.randint(1,opp_guess),-1)
                opp_ask = min(1000,round(opp_guess + (opp_guess - opp_bid),-1))
                
            opp_bid_vol = random.randint(1,10) 
            opp_ask_vol = random.randint(1,10)
            
            oppMap[j][0] = opp_bid
            oppMap[j][1] = opp_ask
            oppMap[j][3] = opp_bid_vol
            oppMap[j][4] = opp_ask_vol

            bids.append(opp_bid)
            asks.append(opp_ask)
    
        lowest_ask = min(asks)
        highest_bid = max(bids)
        
        #Determining profit for opponents after round
        for k in range(n):
            if oppMap[k][0] == highest_bid:
                oppMap[k][2] += (underlying - highest_bid)*oppMap[k][3]
                traderPnL += (highest_bid - underlying)*oppMap[k][3]
            if oppMap[k][1] == lowest_ask:
                oppMap[k][2] += (lowest_ask - underlying)*oppMap[k][4]
                traderPnL += (underlying - lowest_ask)*oppMap[k][4]
        
        #Determining profit for player after round
        
        ask_taken = False
        bid_taken = False
        
        if ask == lowest_ask:
            ask_taken = True
            profit += (ask - underlying)*ask_vol
            traderPnL += (underlying - lowest_ask)*ask_vol
        
        if bid == highest_bid:
            bid_taken = True
            profit += (underlying - bid)*bid_vol
            traderPnL += (highest_bid - underlying)*bid_vol
        
        #Printing scores and feedback
        
        print("\n")
        print("Revealing All Cards: ")
        print("[",cards[0],"] [",cards[1],"] [",cards[2],"] [",cards[3],"] [",cards[4],"] [",cards[5],"] [",cards[6],"] [",cards[7],"] [",cards[8],"] [",cards[9],"]")
        print("Underlying: ", underlying)
        print("\n")

        if ask_taken:
            print("Lead trader has taken your ask of", ask)
        else:
            print("Lead trader has taken an opponents ask of", lowest_ask)
        if bid_taken:
            print("Lead trader has taken your bid of", bid)
        else:
            print("Lead trader has taken an opponents bid of", highest_bid)
        
        print("\n")
        
        print("Players         |  Total Profit and Current Market")
        print("--------------------------------------------------")
        print("You             | ",profit, "(",bid,"@",ask,") ",bid_vol,"by",ask_vol)
        for j in range(n):
            print("Market Maker ",j+1,"| ", oppMap[j][2], " (",oppMap[j][0],"@",oppMap[j][1],") ", oppMap[j][3],"by",oppMap[j][4])
        
        print("\n")
    
    print("Trader PnL: ", traderPnL)

