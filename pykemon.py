from random import randint


# class
class Pykemon:
    """
        A model of a generic Pykemon character

        Attributes:
            name (str): The Pykemon name.
            element (str): The Pykemon element type
            health (int): The Pykemon health bar
            speed (int): The Pykemon speed
    """

    def __init__(self, name, element, health, speed):
        """
        Args:
            name (str): name of the Pykemon
            element (str): element type of the Pykemon
            health (int): current health bar of the Pykemon
            speed (int): speed of the Pykemon over time
        """
        self.name = name.title()
        self.element = element
        self.speed = speed
        self.current_health = health
        self.max_health = health

        self.is_alive = True
        """Pykemon death status"""

        self.moves = []
        """List of Pykemon moves"""

    def light_attack(self, enemy):
        """
        A light attack guaranteed to do minimal damage.

        :param Pykemon enemy: The Pykemon subclass
        :return: None
        :raises TypeError: If the `enemy` is not <class 'type'>
        """

        show_pykemon_action(self.name, self.moves[0])

        damage = randint(15, 25)
        print('It dealt {} damage.'.format(damage))
        enemy.current_health -= damage

    def heavy_attack(self, enemy):
        """
        A heavy attack that could deal Massive or no damage at all.

        :param Pykemon enemy: The Pykemon subclass
        :return: None
        :raises TypeError: If the `enemy` is not <class 'type'>
        """
        show_pykemon_action(self.name, self.moves[1])

        damage = randint(0, 50)

        if damage < 10:
            print('The attack missed!!!')
        else:
            print('It dealt {} damage'.format(damage))
            enemy.current_health -= damage

    def restore(self):
        """A that healing move that will restore current health."""
        show_pykemon_action(self.name, self.moves[2])

        heal = randint(15, 25)
        print('It healed {} health points.'.format(heal))
        self.current_health += heal

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def special_attack(self, enemy):
        """
        Overriden in subclasses
        :param Pykemon enemy:
        :return:
        """
        pass

    def faint(self):
        """If you run out of health, you faint...hence defeated."""
        if self.current_health <= 0:
            self.is_alive = False
            print('Pykemon {} has fainted!'.format(self.name))
            input('Press enter to continue')

    def show_stats(self):
        """Prints formatted view of the Pykemon Attributes."""
        print('\nName: {}'.format(self.name))
        print('Element Type: {}'.format(self.element))
        print('Health: {}/{}'.format(self.current_health, self.max_health))
        print('Speed: {}'.format(self.speed))

    def move_info(self):
        """Display Pykemon move info."""

        if self.element == 'FIRE':
            damage_element = 'GRASS'
        elif self.element == 'WATER':
            damage_element = 'FIRE'
        else:
            damage_element = 'WATER'

        print('{} Moves:'.format(self.name))

        print('-- ' + self.moves[0] + ' --')
        print('  An efficient attack...\n  Guaranteed to do damage within the range of 15 to 25 damage points.')

        print('\n-- ' + self.moves[1] + ' --')
        print('  A risky attack...\n  Could deal up to 50 damage points or as little as 0 damage points.')

        print('\n-- ' + self.moves[2] + ' --')
        print('  A restorative move...\n  Guaranteed to heal your Pykemon 15 to 25 health points.')

        print('\n-- ' + self.moves[3] + ' --')
        print('  A powerful Fire based attack...\n  Guaranteed to deal MASSIVE damage to {} type Pykemon.'
              .format(damage_element))


class Fire(Pykemon):
    """
    Fire based Pykemon that is a subclass/child of Pykemon class.

    Note:
        See `Parent` class for __init__ and class doc
    """

    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)

        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast']

    def special_attack(self, enemy):
        """
        FIRE BLAST: an elemental fire move. Massive damage to Grass element,
        normal damage to Fire element and minimal damage to Water element.

        :param Pykemon enemy: The Pykemon subclass
        :raises TypeError: If the `enemy` is not <class 'type'>
        """

        show_pykemon_action(self.name, self.moves[3], '!')

        if enemy.element == 'GRASS':
            damage = randint(35, 50)
            print("It's SUPER effective!")
        elif enemy.element == 'WATER':
            damage = randint(5, 10)
            print("It's not very effective")
        else:
            damage = randint(10, 20)

        print('It dealt {} damage'.format(damage))
        enemy.current_health -= damage


class Water(Pykemon):
    """
    Water based Pykemon that is a subclass/child of Pykemon class.

    Note:
        See `Parent` class for __init__ and class doc
    """
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)

        self.moves = ['Bite', 'Splash', 'Dive', 'Water Cannon']

    def special_attack(self, enemy):
        """
        WATER CANNON: an elemental water move. Massive damage to Fire element,
        normal damage to Water element and minimal damage to Grass element.

        :param Pykemon enemy: The Pykemon subclass
        :raises TypeError: If the `enemy` is not <class 'type'>
        """

        show_pykemon_action(self.name, self.moves[3], '!')

        if enemy.element == 'FIRE':
            damage = randint(35, 50)
            print("It's SUPER effective!")
        elif enemy.element == 'GRASS':
            damage = randint(5, 10)
            print("It's not very effective")
        else:
            damage = randint(10, 20)

        print('It dealt {} damage'.format(damage))
        enemy.current_health -= damage


class Grass(Pykemon):
    """
    Grass based Pykemon that is a subclass/child of Pykemon class.

    Note:
        See `Parent` class for __init__ and class doc
    """
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)

        self.moves = ['Vine Whip', 'Wrap', 'Grow', 'Leaf Blade']

    def special_attack(self, enemy):
        """
        LEAF BLADE: an elemental Grass move. Massive damage to Water element,
        normal damage to Grass element and minimal damage to Fire element.

        :param Pykemon enemy: The Pykemon subclass
        :raises TypeError: If the `enemy` is not <class 'type'>
        """
        show_pykemon_action(self.name, self.moves[3], '!')

        if enemy.element == 'WATER':
            damage = randint(35, 50)
            print('It\'s SUPER effective!')
        elif enemy.element == 'FIRE':
            damage = randint(5, 10)
            print('It\'s not very effective')
        else:
            damage = randint(10, 20)

        print('It dealt {} damage'.format(damage))
        enemy.current_health -= damage


class Game:
    """A game object to control the creation and flow of Pykemon and simulate battle!"""

    def __init__(self):
        self.pykemon_elements = ['FIRE', 'WATER', 'GRASS']
        """List of pykemon moves"""

        self.pykemon_names = ['Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil', 'Jampot', 'Chewdie', 'Spatol',
                              'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur']
        """list of pykemon names"""

        self.battles_won = 0
        """Battles won by playing"""

    def create_pykemon(self):
        """
        Randomly generates a pykemon
        :return: a subclass of Pykemon based on element
        :rtype: Pykemon
        """
        health = randint(70, 100)
        speed = randint(1, 10)
        index = randint(0, len(self.pykemon_elements) - 1)
        element = self.pykemon_elements[index]
        index = randint(0, len(self.pykemon_names) - 1)
        name = self.pykemon_names[index]

        if element == 'FIRE':
            pykemon = Fire(name, element, health, speed)
        elif element == 'WATER':
            pykemon = Water(name, element, health, speed)
        else:
            pykemon = Grass(name, element, health, speed)

        return pykemon

    def choose_pykemon(self):
        """
        A method to simulate choosing a starting Pykemon similar to Pokemon
        :return: a subclass of Pykemon
        :rtype: Pykemon
        """

        starters = []
        """Holds 3 different elements of Pykemon for user to choose from"""

        while len(starters) < 3:
            pykemon = self.create_pykemon()
            valid_pykemon = True

            for starter in starters:
                if starter.name == pykemon.name or starter.element == pykemon.element:
                    valid_pykemon = False

            if valid_pykemon:
                starters.append(pykemon)

        for pykemon in starters:
            pykemon.show_stats()
            pykemon.move_info()

        print('\nProfessor George presents you with three Pykemon: ')
        for i in range(len(starters)):
            print('({}) - {}'.format(i + 1, starters[i].name))

        index = int(input('Which Pykemon would you like to choose: '))
        index -= 1

        pykemon = starters[index]

        return pykemon

    @staticmethod
    def get_attack(pykemon):
        """
        Get user attack choice
        :param Pykemon pykemon:
        :return: the index of the player move
        :rtype: int
        """
        print('\nWhat would you like to do...')
        for i in range(len(pykemon.moves)):
            print('({}) - {}'.format(i + 1, pykemon.moves[i]))

        index = int(input('Please enter your move choice: '))

        return index

    @staticmethod
    def attack_opps(move, attacker, defender):
        """
        Let's pykemon attack during battle
        :param int move:
        :param Pykemon attacker:
        :param Pykemon defender:
        """

        if move == 1:
            attacker.light_attack(defender)
        elif move == 2:
            attacker.heavy_attack(defender)
        elif move == 3:
            attacker.restore()
        elif move == 4:
            attacker.special_attack(defender)

        defender.faint()

    def battle(self, player, computer):
        """
        Simulate a battle round, faster Pykemon gets first attack..
        :param Pykemon player:
        :param Pykemon computer:
        """

        player_move = self.get_attack(player)
        computer_move = randint(1, 4)

        print('\n-------------------------------------------------------------')

        if player.speed >= computer.speed:
            self.attack_opps(player_move, player, computer)
            if computer.is_alive:
                self.attack_opps(computer_move, computer, player)
        else:
            self.attack_opps(computer_move, computer, player)
            if player.is_alive:
                self.attack_opps(player_move, player, computer)

        print('-------------------------------------------------------------')


# Functions
def show_pykemon_action(name: str, action: str, ex='.') -> None:
    print('Pykemon {} used {}{}'.format(name, action, ex))


def game_intro():
    """Prints intro messages/cutscene"""
    print('Welcome to Pykemon!')
    print('Can you become the worlds greatest Pykemon Trainer???\n')
    print("Don't worry! Prof George is here to help you on your quest.")
    print('He would like to gift you your first pykemon!')
    print('Here are three potential Pykemon partners.')
    input('Press enter to choose your Pykemon!')


def start_game():
    """Simulates game play"""
    game_intro()

    playing_main = True

    while playing_main:
        game = Game()
        player = game.choose_pykemon()
        player.show_stats()

        print('Congratulations Trainer, you have chosen {}'.format(player.name))
        input('\nYour journey with {} begins now...Press Enter'.format(player.name))

        while player.is_alive:
            cpu_pykemon = game.create_pykemon()

            print('\nOH NO! A wild {} has approached!'.format(cpu_pykemon.name))
            cpu_pykemon.show_stats()

            while cpu_pykemon.is_alive and player.is_alive:
                game.battle(player, cpu_pykemon)

                if cpu_pykemon.is_alive and player.is_alive:
                    player.show_stats()
                    cpu_pykemon.show_stats()
                    print('--------------------------------------------------------------------------------')

            if player.is_alive:
                game.battles_won += 1

        print('\nPoor {} has fainted...'.format(player.name))
        print('But not before defeating {} Pykemon!'.format(game.battles_won))

        user_input = input('would you like to play (y/n): ').lower().strip()

        if user_input != 'y':
            playing_main = False
            print('Thank you for playing Pykemon!')


start_game()
