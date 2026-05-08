"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    cards = ["K", "Q", "J"]
    if card in cards:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)
   

def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    elif value_one < value_two:
        return card_two
    else:
        return card_one,card_two
  


def value_of_ace(card_one, card_two):
    if "A" in [card_one, card_two]:
        return 1
    
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one + value_two + 11 > 21:
        return 1
    else:
        return 11
   

def is_blackjack(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    combined_value = value_one + value_two
    if "A" in [card_one,card_two]:
        combined_value +=  10
    return combined_value == 21
    



def can_split_pairs(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one == value_two:
        return True
    else:
        return False
  


def can_double_down(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    combined_value = value_one + value_two
    if 9 <=combined_value <=11:
        return True
    else:
        return False
    

