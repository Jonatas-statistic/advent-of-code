import re


# Type of hand

FIVE_OF_A_KIND = '7'
FOUR_OF_A_KIND = '6'
FULL_HOUSE = '5'
THREE_OF_A_KIND = '4'
TWO_PAIR = '3'
ONE_PAIR = '2'
HIGH_CARD = '1'


class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self._type = self._get_type(hand)
        self._hand = self._get_hand(hand)

    def _get_hand(self, hand: str) -> str:
        return hand.replace(
            'T', 'L').replace(
            'J', 'M').replace(
            'Q', 'N').replace(
            'K', 'O').replace(
            'A', 'P')

    def _get_type(self, hand: str) -> str:
        repetions = []
        for character in hand:
            repetion = len(re.findall(f'{character}', hand))
            repetions.append(repetion)
        repetions = sorted(repetions, reverse=True)
        if repetions[0] == 5:
            return FIVE_OF_A_KIND
        elif repetions[0] == 4:
            return FOUR_OF_A_KIND
        elif repetions[0] == 3:
            if repetions[3] == 2:
                return FULL_HOUSE
            return THREE_OF_A_KIND
        elif repetions[0] == 2:
            if repetions[2] == 2:
                return TWO_PAIR
            return ONE_PAIR
        else:
            return HIGH_CARD    
   
    @property
    def type(self):
        return self._type

    @property
    def ordered_hand(self):
        return self._hand

    def __eq__(self, other):
        if isinstance(other, Hand):
            return (self.hand == other.hand) and (self.bid == self.bid)
        return False

    def __repr__(self):
        return f'{(self.ordered_hand)} Hand(hand = {self.hand}, bid = {self.bid})'
    
    def __str__(self):
        return self.__repr__(self)
    

# Part Two

class HandTwo(Hand):
    
    def _get_hand(self, hand: str) -> str:
        return hand.replace(
            'T', 'L').replace(
            'J', '1').replace(
            'Q', 'N').replace(
            'K', 'O').replace(
            'A', 'P')
    
    def _get_type(self, hand: str) -> str:
        repetions = []
        js = 0 # number of 'J's character
        for character in hand:
            if character == 'J':
                js = len(re.findall(f'{character}', hand))
                if js > 3:
                    return FIVE_OF_A_KIND
            else:
                repetion = len(re.findall(f'{character}', hand))
                repetions.append(repetion)
        repetions = sorted(repetions, reverse=True)
        if repetions[0] + js == 5 :
            return FIVE_OF_A_KIND
        elif repetions[0] + js == 4:
            return FOUR_OF_A_KIND
        elif repetions[0] + js == 3:
            if repetions[0] == 2:
                if repetions[2] == 2:
                    return FULL_HOUSE
            elif repetions[0] == 3:
                if repetions[3] == 2:
                    return FULL_HOUSE
            return THREE_OF_A_KIND    
        elif repetions[0] + js == 2:
            if repetions[0] == 2:
                if repetions[2] == 2:
                    return TWO_PAIR
            return ONE_PAIR
        else:
            return HIGH_CARD