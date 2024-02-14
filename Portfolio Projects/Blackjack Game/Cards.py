# Author: Stefan DeWolfe
# Date: 4 / 2021
# Last Modified: 2 / 14 / 2024
# 

class Card(object):
    # https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
    NAME_TO_SYMBOL = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }
    CARD_VALUES = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Joker':0
    }
    CARD = """\
┌─────────┐
│{}       │
│         │
│         │
│    {}   │
│         │
│         │
│       {}│
└─────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

    HIDDEN_CARD = """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""
    def __init__(self, suit, rank, flipped=False):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.CARD_VALUES[rank]
        self.flipped=flipped
    def code(self): 
        rank = "T" if (self.rank=='10') else str(self.rank)[0]
        return f"{rank}{str(self.suit)[0]}"
    def __str__(self): 
        rank = "T" if (self.rank=='10') else str(self.rank)[0]
        return f"{rank}{str(self.suit)[0]}"
class PlayingCard(Card):
    def __init__(self, suit, rank, flipped=False):
        Card.__init__(self, suit=suit, rank=rank, flipped=flipped)
class StandardPlayingCards():
    def get_standard_playing_deck(include_jokers=False):
        suits=["Diamonds","Spades","Clubs","Hearts"]
        numbers=['Ace', '2',  '3', '4', '5',  '6', '7',  '8',  '9', '10', 'Jack', 'Queen', 'King']
        cards=[]
        for suit in suits:
            for number in numbers:
                cards.append(PlayingCard(suit, number))
        if include_jokers:
            cards.append(PlayingCard("Joker","Joker"))
            cards.append(PlayingCard("Joker","Joker"))
        return cards

class CardTestMain():
    @staticmethod
    def join_lines(strings):
        """
        Stack strings horizontally.
        This doesn't keep lines aligned unless the preceding lines have the same length.
        :param strings: Strings to stack
        :return: String consisting of the horizontally stacked input
        """
        liness = [string.splitlines() for string in strings]
        return '\n'.join(''.join(lines) for lines in zip(*liness))
    @staticmethod
    def ascii_version_of_card(*cards):
        """
        Instead of a boring text version of the card we render an ASCII image of the card.
        :param cards: One or more card objects
        :return: A string, the nice ascii version of cards
        """

        # we will use this to prints the appropriate icons for each card
        #
        def card_to_string(card):
            # 10 is the only card with a 2-char rank abbreviation
            rank = card.rank if card.rank == '10' else card.rank[0]

            if (card.flipped):
                return Card.HIDDEN_CARD.format(rank=rank, suit=Card.NAME_TO_SYMBOL[card.suit])
            else:
                # add the individual card on a line by line basis
                return Card.CARD.format(rank=rank, suit=Card.NAME_TO_SYMBOL[card.suit])
        #
        return CardTestMain.join_lines(map(card_to_string, cards))
    @staticmethod
    def ascii_version_of_hidden_card(*cards):
        return CardTestMain.join_lines((Card.HIDDEN_CARD, CardTestMain.ascii_version_of_card(*cards[1:])))
    @staticmethod
    def ascii_version_of_hidden_cards(num_flipped, *cards):
        if isinstance(num_flipped,Card): return CardTestMain.join_lines([Card.HIDDEN_CARD]*(len(cards)+1) )
        if (num_flipped <= 0): return CardTestMain.ascii_version_of_card(*cards)
        if (num_flipped >= len(cards)): return CardTestMain.join_lines([Card.HIDDEN_CARD]*(len(cards)) )
        return CardTestMain.join_lines(
            (
            CardTestMain.join_lines([Card.HIDDEN_CARD]*num_flipped), 
            CardTestMain.ascii_version_of_card(*cards[num_flipped:])
            )
        )
    # TEST CASES
    
    # print(ascii_version_of_hidden_card(test_card_1, test_card_2))
    @staticmethod
    def main():
        print ("===========================")
        deck = StandardPlayingCards.get_standard_playing_deck(True)
        for i in [0,1,2,3]:
            print(CardTestMain.ascii_version_of_card(deck[0+13*i],deck[1+13*i],deck[2+13*i],deck[3+13*i],deck[4+13*i],deck[5+13*i],deck[6+13*i]))
            print(CardTestMain.ascii_version_of_card(deck[7+13*i],deck[8+13*i],deck[9+13*i],deck[10+13*i],deck[11+13*i],deck[12+13*i]     ))
        print ("===========================")
        test_card_1 = Card('Diamonds', '4')
        test_card_2 = Card('Clubs', 'Ace')
        test_card_3 = Card('Spades', 'Jack')
        test_card_4 = Card('Hearts', '10')

        print(CardTestMain.ascii_version_of_card(test_card_1, test_card_2, test_card_3, test_card_4))
        #test_card_1.flipped=True
        #test_card_4.flipped=True
        #print(ascii_version_of_card(test_card_1, test_card_2, test_card_3, test_card_4))
        
        print(CardTestMain.ascii_version_of_hidden_card(test_card_1, test_card_2, test_card_3, test_card_4))

        print ("=======================================")
        print ("No num_hidden Param")
        print(CardTestMain.ascii_version_of_hidden_cards(test_card_1, test_card_2, test_card_3, test_card_4))

        print ("num_hidden Param = 0")
        print(CardTestMain.ascii_version_of_hidden_cards(0,test_card_1, test_card_2, test_card_3, test_card_4))

        print ("num_hidden Param within limit")
        print(CardTestMain.ascii_version_of_hidden_cards(1,test_card_1, test_card_2, test_card_3, test_card_4))
        print(CardTestMain.ascii_version_of_hidden_cards(2,test_card_1, test_card_2, test_card_3, test_card_4))
        print(CardTestMain.ascii_version_of_hidden_cards(3,test_card_1, test_card_2, test_card_3, test_card_4))

        print ("num_hidden Param @ limit")
        print(CardTestMain.ascii_version_of_hidden_cards(4,test_card_1, test_card_2, test_card_3, test_card_4))

        print ("num_hidden Param Beyond limit")
        print(CardTestMain.ascii_version_of_hidden_cards(5,test_card_1, test_card_2, test_card_3, test_card_4))

        print ("=======================================")
    

if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    CardTestMain.main()
