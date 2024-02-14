# Author: Stefan DeWolfe
# Date: 4 / 2021
# Last Modified: 2 / 14 / 2024
# 
from Cards import Card, PlayingCard, StandardPlayingCards
import random
class CardDeck(object):
    def __init__(self):
        self.cards=[]
    def add_card(self,card, shuffles=0):
        self.cards.append(card)
        self.shuffle(shuffles)
    def is_empty(self): return len(self.cards) < 1
    def shuffle(self, times=10):
        for t in range(times):
            for i in range(len(self.cards)-1):
                j = random.randint(0,len(self.cards)-1)
                temp = self.cards[i]
                self.cards[i]=self.cards[j]
                self.cards[j]=temp
    def shuffles(self, times=10): shuffle(times)
    def draw(self,top=True):
        if(len(self.cards) > 0):
            index = 0 if top else len(self.cards)-1
            card = self.cards[index]
            self.cards.remove(card)
            return card
        return None
    def add_to_deck(self,card,shuffles=0):
        if (isinstance(card,Card)):
            self.cards.append(card)
            self.shuffle(shuffles)
    def show(self):
        text = "["
        new_line=True
        for card in self.cards:
            if self.cards.index(card) % 13 == 0:
                text +="\n"
                new_line=True
            text += ", " if not new_line else ""
            #print (card)
            text+=card.code()
            new_line=False
            
        return text+"]"

class CardDeckTestMain():
    @staticmethod
    def main():
        decklist = StandardPlayingCards.get_standard_playing_deck(False)
        deck = CardDeck()
        discard = CardDeck()
        discardlist = []
        print ("===========================")
        for card in decklist:
            deck.add_card(card, shuffles=0)
            #decklist.remove
        print(deck.show())
        print(discard.show())
        print ("===========================")
        deck.shuffle(20)
        print(deck.show())
        print(discard.show())
        print ("===========================")
        while(not deck.is_empty()):
            card = deck.draw()
            discard.add_card(card)
        print(deck.show())
        print(discard.show())
        print ("===========================")
        while(not discard.is_empty()):
            card = discard.draw()
            deck.add_card(card)
        print(deck.show())
        print(discard.show())
        print ("===========================")

if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    CardDeckTestMain.main()
