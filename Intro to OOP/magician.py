from card import Card


class Magician:
    def __init__(self):
        self.cards = []
        self.chosen_card_value = 0

    def create_cards(self):
        i = 2
        while i <= 10:
            self.cards.append(Card(i))
            i += 1
        else:
            for card in self.cards:
                print(card.value)

    def ask_pick_number (self):
        self.chosen_card_value = int(input("Pick a number between 2 and 10, but don't tell me what it is."))

    def locate_card(self):
        for card in self.cards:
            if card.value == self.chosen_card_value:
                print(f'Your card is the {card.value} of {card.suit}')
