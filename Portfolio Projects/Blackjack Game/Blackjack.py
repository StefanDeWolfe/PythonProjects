# Author: Stefan DeWolfe
# Date: 4 / 2021
# Last Modified: 2 / 14 / 2024
# 
import os
from Cards import Card, PlayingCard, StandardPlayingCards
from CardHand import CardHand
from CardDeck import CardDeck
from Interface import Interface as interface

class BlackjackHand(CardHand):
    def __init__(self):
        CardHand.__init__(self,-1)
        self.score=0
    def draw(self,card, force=False): 
        if (card.points > 10):
            if (self.score > 10):
                self.score+=1
        self.score+=card.points
        return self.add_card_to_hand(card)
    def show(self):
        print(f"Hand Score: {self.score}")
        print(self.ascii_version_of_card())

class Main():
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    @staticmethod
    def main():
        Main.clear()
        wins = 0
        rounds = 0
        winnings=1000
        pot = 0
        bet=100
        playerHand=None
        dealerHand=None
        options = ["Hit","Stay"]
        opt=""
        while(True):
            rounds+=1
            winnings -= bet
            pot+=bet*2
            deck = CardDeck()
            decklist = StandardPlayingCards.get_standard_playing_deck(False)
            for card in decklist:
                deck.add_card(card, shuffles=0)
            deck.shuffle(20)
            playerHand=BlackjackHand()
            dealerHand=BlackjackHand()
            playerHand.draw(deck.draw())
            playerHand.draw(deck.draw())
            card = deck.draw()
            card.flipped=True
            dealerHand.draw(card)
            dealerHand.draw(deck.draw())
            opt=-1
            while(opt!=1 and playerHand.score < 21):
                Main.clear()
                print("")
                print ("Dealer")
                dealerHand.show()
                
                print (f"\nPot: {pot}\n")
                print (f"\nBet: {bet}\n")

                print ("Player")
                playerHand.show()
                opt = interface.chooseOption(options=options,prompt="Hit or Stay? ")
                if (opt==0):
                    playerHand.draw(deck.draw())
                    if (playerHand.score >= 21):
                        break

                else:
                    break
            #
            while(dealerHand.score < 16 and playerHand.score < 21):
                dealerHand.draw(deck.draw())
            #
            Main.clear()
            print ("Dealer")
            dealerHand.reveal_hand()
            dealerHand.show()
            print ("Player")
            playerHand.show()
            if (playerHand.score == 21):
                print("Player Blackjack!")
                wins+=1
                winnings+=pot+bet
                pot=0
            elif (dealerHand.score == 21):
                print("Dealer Blackjack!")
                pot=0
            elif (playerHand.score > 21):
                print("Player Bust!")
                pot=0
            elif(dealerHand.score > 21):
                print("Dealer Bust!")
                wins+=1
                winnings+=pot
                pot=0
            elif(dealerHand.score > playerHand.score):
                print("Dealer Wins!")
                pot=0
            elif(dealerHand.score < playerHand.score):
                print("Player Wins!")
                wins+=1
                winnings+=pot
                pot=0
            elif(dealerHand.score == playerHand.score):
                print("Draw!")
            print(f"Player Wins/Rounds: {wins}/{rounds}.  Winnings: {winnings}")
            print (f"\nPot: {pot}\n")
            print("Play Again?")
            if(winnings < 1 or not interface.confirm(prompt="")):
                break

    

if __name__ == "__main__":
    import os
    Main.main()
