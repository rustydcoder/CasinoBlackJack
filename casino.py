import time
from random import shuffle


# Defining my class
class Card:
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        print('{} of {}'.format(self.rank, self.suit))


class Deck:
    def __init__(self):
        self.cards = []

    def build_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "K": 10,
            "Q": 10,
            "A": 11
        }

        for suit in suits:
            for k, v in ranks.items():
                card = Card(k, v, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop()
        return card


class Player:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, cards):
        # TODO: Use a for loop to deal 2 cards to the player
        for i in range(2):
            self.hand.append(cards.deal_card())

    def display_hand(self):
        # TODO: Print a message declaring the player's hand and call cards deal_card()
        print('')

        for card in self.hand:
            card.display_card()

    def hit(self, cards):
        # TODO: Call the deck's deal_card() method to get a card
        self.hand.append(cards.deal_card)

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value

            if card.rank == 'A':
                ace_in_hand = True

        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10

        # TODO: print the total value of the hand
        print('')

    def update_hand(self, cards):
        if self.hand_value < 21:
            # TODO: get user input for if they would like to hit
            player_choice = user_yn_choice('')

            if player_choice:
                self.hit(cards)
            else:
                self.playing_hand = False

        else:
            self.playing_hand = False


class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = False

    def draw_hand(self, cards):
        # TODO: Use a for loop to deal 2 cards to the player
        for i in range(2):
            self.hand.append(cards.deal_card())

    def display_hand(self):
        # TODO: Prompt user to press enter to reveal dealer cards
        input('(enter)')

        for card in self.hand:
            card.display_card()

            # pausing for suspense from dealer
            time.sleep(2)

    def hit(self, cards):
        # TODO: the dealer must hit until they reach 17, then they must stop
        self.get_hand_value()

        while self.hand_value < 17:
            card = cards.deal_card()
            self.hand.append(card)
            self.get_hand_value()

        # TODO: Print how many cards are in the dealer's hand
        print('')

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value

            if card.rank == 'A':
                ace_in_hand = True

            if self.hand_value > 21 and ace_in_hand:
                self.hand_value -= 10


class Game:
    def __init__(self, money):
        self.money = money
        self.bet = 20
        self.winner = ''

    def set_bet(self):
        betting = True

        while betting:
            # TODO: get user input for their bet
            stake = int(input(''))

            if stake < 20:
                self.bet = 20

            if self.bet > self.money:
                # TODO: inform user that they cannot afford the bet
                print('')
            else:
                self.bet = stake
                betting = False

    def scoring(self, player_hand_value, dealer_hand_value):
        if player_hand_value == 21:
            # TODO: print that they got black jack
            print('')
            self.winner = 'p'
        elif dealer_hand_value == 21:
            self.winner = 'd'
        elif player_hand_value > 21:
            # TODO: print player went over 21
            print('')
            self.winner = 'p'
        elif dealer_hand_value > 21:
            print('')
            self.winner = 'd'
        else:
            if player_hand_value > dealer_hand_value:
                # TODO: print a summary
                print('')
                self.winner = 'p'
            elif dealer_hand_value > player_hand_value:
                print('')
                self.winner = 'd'
            else:
                print('')
                self.winner = 'tie'

    def payout(self):
        if self.winner == 'p':
            self.money += self.bet
        else:
            self.money -= self.bet

    def display_money(self):
        # TODO: Print how much money the current game object holds
        print('')

    def display_money_and_bet(self):
        # TODO: Print how much money the current game object holds and the current bet
        print('')


def user_yn_choice(word):
    user_input = input(word).lower().strip()

    if user_input == 'y':
        return True
    else:
        return False


# main code
print('Welcome to the Blackjack App.')
