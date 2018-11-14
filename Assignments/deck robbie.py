#Deck.py
#5/12/17
#Robert Gostel

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def blackJackValue(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank
    def __str__(self):

        ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        rankString = ranks[self.rank - 1]

        if self.suit == 'd':
            suitString = 'Diamonds'
        elif self.suit == 's':
            suitString = 'Spades'
        elif self.suit == 'h':
            suitString = 'Hearts'
        else:
            suitString = 'Clubs'

        return rankString + ' of ' + suitString
class Deck:
        def __init__(self):
            self.listofcards = []
        # create a list of cards

    # generate the list of cards
            for rank in range(1,14):
                for suit in ['c', 's', 'h', 'd']:
                    self.listofcards.append( Card(rank, suit) )

        def shuffle(self):
            random.shuffle(self.listofcards)

        def dealCard(self):
            return self.listofcards
        def cardsLeft(self):
            return len(self.listofcards)
        

def main():
    
    print("Creating the deck of cards")
    myCards = Deck()
    print("Shuffling the deck of cards")
    myCards.shuffle()
    z = eval(input("How many cards should be delt to each player"))
    player1hand = []
    for i in range(z):
         player1hand.append(myCards.dealCard)
    print("Player 1 was dealt:")
    for i in player1hand:
         print(i)
         

    player2hand = []
    for i in range(z):
         player2hand.append(myCards.dealCard)
    print("Player 2 was dealt:")
    for i in player2hand:
         print(i)
         

    
main()

 


    
