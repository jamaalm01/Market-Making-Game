# Market Making Game vs Bots
## How to Play:
10 cards are chosen from numbers 1-100. Each round one cards is revealed. Your aim is make a market on the sum of the 10 cards. 
<br> Watch out as you are competing against other market makers for an external trader to take your bids/asks.
<br> To run the game simply clone the repo and run the startGame() function 


# Market Taking Game Tool
This tool is an automated decision maker for the market taking game on tradermath
<br> which can be found at https://www.tradermath.org/market-games/dashboard. I have also included my own version of this game in this repository with custom inputs. 
<br>
<br> It works by taking in the inputs - number of cards, given card value (0 if no card is given) and bid-ask spread
<br> It will output BUY or SELL with VOLUME to be traded (1,5 or 10) as well as the probability and expected value of profit/edge .
<br> Currently the tool doesn't have a feature to handle market events but that is something that is being implemented
