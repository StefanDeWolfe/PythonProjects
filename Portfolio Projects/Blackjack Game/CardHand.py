# Author: Stefan DeWolfe
# Date: 4 / 2021
# Last Modified: 2 / 14 / 2024
# 
from Cards import Card, PlayingCard, StandardPlayingCards
class CardHand(object):
    def __init__(self,max_hand_size=-1):
        self.cards=[]
        self.max_size=max_hand_size
    def has_max_hand_size(self): return self.max_size >= 1
    def show(self): print(self.ascii_version_of_card())
    def hide_hand(self):
        for card in self.cards:
            card.flipped=True
    def reveal_hand(self):
        for card in self.cards:
            card.flipped=False
    def hide_hand_by_indexes(self, indexes=[]):
        for index in indexes:
            card = self.get_card_from_index(index)
            if (card):
                card.flipped=True
    def reveal_hand_by_indexes(self, indexes=[]):
        for index in indexes:
            card = self.get_card_from_index(index)
            if (card):
                card.flipped=False
    def get_card_from_index(self, index):
        if(0 <= index and index < len(self.cards)):
            return self.cards[index]
        return None
    def draw(self,card, force=False): return self.add_card_to_hand(card)
    def add_card_to_hand(self,card, force=False):
        if(self.has_max_hand_size() and len(self.cards) < self.max_size and not force):
            self.cards.append(card)
            return True
        elif(self.has_max_hand_size() and len(self.cards) >= self.max_size and not force):
            return False
        self.cards.append(card)
        return True
    def discard_by_index(self, index): 
        return self.discard(self.get_card_from_index(index))
    def discard(self, card):
        if (card in self.cards):
            self.cards.remove(card)
            return True
        return False
    def num_cards_to_discard(self):
        if(self.has_max_hand_size() and len(self.cards) >= self.max_size):
            return len(self.cards) - self.max_size
        else:
            return 0
    @staticmethod
    def join_lines(strings):
        liness = [string.splitlines() for string in strings]
        return '\n'.join(''.join(lines) for lines in zip(*liness))
    def ascii_version_of_card(self):
        def card_to_string(card):
            # 10 is the only card with a 2-char rank abbreviation
            rank = card.rank if card.rank == '10' else str(card.rank)[0] # get first character of suit string
            if (card.flipped):
                return Card.HIDDEN_CARD.format(rank=rank, suit=Card.NAME_TO_SYMBOL[card.suit])
            else:
                return Card.CARD.format(rank=rank, suit=Card.NAME_TO_SYMBOL[card.suit])
        return CardHand.join_lines(map(card_to_string, self.cards))
    def is_empty(self): return len(self.cards) < 1

class CardHandTestMain():
    @staticmethod
    def main():
        deck = StandardPlayingCards.get_standard_playing_deck(True)
        hand = CardHand(hand=[], max_hand_size=5)
        print ("===========================")
        for i in range(4):
            hand.add_card_to_hand(deck[0])
            deck.remove(deck[0])
        hand.show()
        hand.hide_hand()
        hand.show()
        hand.reveal_hand_by_indexes([1,2])
        hand.show()
        hand.reveal_hand()
        hand.show()
        hand.hide_hand_by_indexes([1,2])
        hand.show()
        print ("===========================")
        for i in range(4):
            res = hand.add_card_to_hand(deck[0])
            if (res):
                deck.remove(deck[0])
                print (f"Card Added: {len(hand.cards)}/{hand.max_size}")
            else:
                print (f"Card Not Added: {len(hand.cards)}/{hand.max_size}")
        hand.reveal_hand()
        hand.show()
        print ("===========================")
        for i in range(3):
            res = hand.add_card_to_hand(deck[0],True)
            if (res):
                deck.remove(deck[0])
                print (f"Card Added: {len(hand.cards)}/{hand.max_size}")
            else:
                print (f"Card Not Added: {len(hand.cards)}/{hand.max_size}")
        hand.reveal_hand()
        hand.show()

        print (f"Before Discard: {len(hand.cards)}/{hand.max_size}")
        for i in range(hand.num_cards_to_discard()):
            card = hand.get_card_from_index(0)
            print(f"Discarding {card.code()}")
            hand.discard(card)
        print (f"After Discard: {len(hand.cards)}/{hand.max_size}")
        hand.reveal_hand()
        hand.show()
    

if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    CardHandTestMain.main()
