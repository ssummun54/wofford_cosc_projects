# deck.py
# This program creates, shuffles, and deals cards from a deck to two players
# Sergio Sum
# 5/12/17

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
        elif self.rank == 1:
            return 11
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
        # create a list of cards
        self.listOfCards = []
        # generate the list of cards
        for rank in range(1,14):
            for suit in ['c', 's', 'h', 'd']:
                self.listOfCards.append( Card(rank, suit) )

    def shuffle(self):
        random.shuffle(self.listOfCards)

    def dealCard(self):
        return self.listOfCards.pop()

    def cardsLeft(self):
        return len(self.listOfCards)

def main():
    print("Creating the deck of cards...")
    myDeck = Deck()
    print("Shuffling the deck of cards...")
    myDeck.shuffle()

    #asks for number of cards to be dealt
    dealing = eval(input("How many cards should be dealt to each player: "))

    player1 = []

    # gets cards from deck
    for i in range (dealing):
        player1.append(myDeck.dealCard())
    print("Player 1 was dealt: ")
    # printing each card from the list
    for card in player1:
        print(card)

    player2 = []
    for i in range (dealing):
        player2.append(myDeck.dealCard())


    print()

    print("Player 2 was dealt:")
    for card in player1:
        print(card)

if __name__ == '__main__':
    main()
