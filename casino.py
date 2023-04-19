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
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop()
        return card


# TODO: make player the extension of a new class CPU
class Player():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, cards):
        # Use a for loop to deal 2 cards to the player
        for i in range(2):
            self.hand.append(cards.deal_card())

    def display_hand(self):
        # Print a message declaring the player's hand and display all cards
        print('\nPlayer\'s Hand:')

        for card in self.hand:
            card.display_card()

    def hit(self, cards):
        # Call the deck's deal_card() method to get a card
        card = cards.deal_card()
        self.hand.append(card)

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value

            if card.rank == 'A':
                ace_in_hand = True

        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10

        # print the total value of the hand
        print('Total value: {}'.format(self.hand_value))

    def update_hand(self, cards):
        if self.hand_value < 21:
            # get user input for if they would like to hit
            player_choice = user_yn_choice('Would you like to hit (y/n): ')

            if player_choice:
                self.hit(cards)
            else:
                self.playing_hand = False

        else:
            self.playing_hand = False


# TODO: make dealer the extension of a new class CPU
class Dealer():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = False

    def draw_hand(self, cards):
        # Use a for loop to deal 2 cards to the player
        for i in range(2):
            self.hand.append(cards.deal_card())

    def display_hand(self):
        # Prompt user to press enter to reveal dealer cards
        input('\nPress enter to reveal the dealer\'s hand.')

        for card in self.hand:
            card.display_card()

            # pausing for suspense from dealer
            time.sleep(2)

    def hit(self, cards):
        # the dealer must hit until they reach 17, then they must stop
        self.get_hand_value()

        while self.hand_value < 17:
            card = cards.deal_card()
            self.hand.append(card)
            self.get_hand_value()

        # Print how many cards are in the dealer's hand
        print('\nDealer is set with a total of {} cards.'.format(len(self.hand)))

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
            # get user input for their bet
            stake = int(input('How would you like to stake (minimum bet of $20): '))

            if stake > self.money:
                print('Sorry, you can not afford this bet.')
            elif stake >= self.bet:
                self.bet = stake
                self.money -= stake
                betting = False
            else:
                self.bet = 20
                self.money -= 20
                betting = False

    def scoring(self, player_hand_value, dealer_hand_value):
        if player_hand_value == 21:
            print('You got black jack, you win!')
            self.winner = 'p'
        elif dealer_hand_value == 21:
            print('The dealer got black jack, you lose!')
            self.winner = 'd'
        elif player_hand_value > 21:
            # print player went over 21
            print('You went over 21...you lose!')
            self.winner = 'd'
        elif dealer_hand_value > 21:
            print('Dealer went over 21. you win!')
            self.winner = 'p'
        else:
            if player_hand_value > dealer_hand_value:
                print('You\'re closer to black jack, you win!')
                self.winner = 'p'
            elif dealer_hand_value > player_hand_value:
                print('The dealer is closer to black jack, you lose!')
                self.winner = 'd'
            else:
                print('It is a tie')
                self.winner = 'tie'

    def payout(self):

        if self.winner == 'p':
            self.money += self.bet * 2
            print('player')
            print(self.money)
        elif self.winner == 'd':
            print('dealer')
            # self.money = self.money
            print(self.money)

    def display_money(self):
        print('\nCurrent Money ${}'.format(self.money))

    def display_money_and_bet(self):
        # Print how much money the current game object holds and the current bet
        print('\nCurrent Money: ${}\tCurrent Bet: ${}'.format(self.money, self.bet))


def user_yn_choice(word):
    user_input = input(word).lower().strip()

    if user_input == 'y':
        return True
    else:
        return False


# main code
print('Welcome to the Blackjack App.')

# TODO: Allow user to set minimum bet
print('The minimum bet at this table is $20\n')

user_money = int(input('How much money are you willing to play with today: '))
game = Game(user_money)

flag = True
while flag:
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    player = Player()
    dealer = Dealer()

    game.display_money()
    game.set_bet()

    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    game.display_money_and_bet()

    dealer.hand[0].display_card()

    while player.playing_hand:
        player.display_hand()

        player.get_hand_value()
        player.update_hand(game_deck)

    dealer.hit(game_deck)
    dealer.display_hand()

    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    if game.money < 20:
        flag = False
        print('Sorry, you ran out of money. Please play again.')
