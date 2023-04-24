from random import randint, shuffle


class Simulation:
    """
    Controls the simulation and help facilitate in the spread of the disease.

    Attributes:
        day_number (int): current day of simulation
        population_size (int): total number of people
        infection_percent (float): percentage of people infect
        infection_probability (int): chances that a person can be infected
        infection_duration (int): how long the infection lasts
        mortality_rate (int): chances a person dies from the infection
        sim_days (int): number of days to simulate to
    """

    def __init__(self):
        self.day_number = 1

        print('To simulate an epidemic outbreak, we must know the population size.')
        self.population_size = int(input('---Enter the population size: '))

        print('\nWe must first start by infecting a portion of the population.')
        self.infection_percent = int(input('--Enter the percentage (0-100) of the population to initially infect: '))
        self.infection_percent = self.infection_percent / 100

        print('\nWe must know the risk a person has to contract the disease when exposed.')
        self.infection_probability = int(input('--Enter the probability (0-100) that a person gets infected '
                                               'when exposed to the disease: '))

        print('\nWe must know how long the infection will last when exposed.')
        self.infection_duration = int(input('--Enter the number of days to simulate: '))

        print('\nWe must know the mortality rate of those infected.')
        self.mortality_rate = int(input('--Enter the mortality rate of those infected: '))

        print('\nWe must know how long to run the simulation.')
        self.sim_days = int(input('--Enter the number of days to simulate: '))


class Person:
    """
    A model for an individual person in a population
    Attributes:
        is_infected (bool): True if this person becomes infected
        is_dead (bool): True if this person is dies from the infection
        days_infected (int): tracks the number of days this person is infected.
    """

    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, probability):
        """
        Infects the person based on simulation conditions
        :param int probability: the infection_probability of the simulation
        """
        chances = randint(0, 100)
        if chances < probability:
            self.is_infected = True

    def heal(self):
        """Heals this person from infection"""
        self.is_infected = True
        self.days_infected = 0

    def die(self):
        """Kills this person"""
        self.is_dead = True

    def update(self, rate, duration):
        """
        Controls if this person dies or gets healed
        :param int rate: the mortality rate of the simulation
        :param int duration: the infection duration of the simulation
        """
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1

                chances = randint(0, 100)
                if chances < rate:
                    self.die()
                elif self.days_infected == duration:
                    self.heal()


class Population:
    """
    A class to model a whole population of Person objects
    Attributes:
        sim (Simulation): the `Simulation` class
        population (list): list of `Person` class
    """

    def __init__(self, sim):
        """
        :param Simulation sim:
        """
        self.sim = sim

        self.population = []
        self.get_population()

    def get_population(self):
        """Fills in a random Person in the `population` attribute"""
        for i in range(self.sim.population_size):
            person = Person()
            self.population.append(person)

    def initial_infection(self):
        """Infect an initial portion of the population"""

        infected_count = round(self.sim.infection_percent * self.sim.population_size, 0)
        infected_count: int = int(infected_count)
        """people that must start infected based on user's simulation infection_percent"""

        for i in range(infected_count):
            person: Person = self.population[i]
            person.is_infected = True
            person.days_infected = 1

        shuffle(self.population)

    def spread_infection(self):
        """Spread the infection to all adjacent people in the list population."""
        for i in range(len(self.population)):

            if not self.population[i].is_dead:

                if i == 0 and self.population[i + 1].is_infected:
                    self.population[i].infect(self.sim.infection_probability)

                elif (
                        i < len(self.population) - 1 and
                        (self.population[i + 1].is_infected or
                         self.population[i - 1].is_infected)
                ):
                    self.population[i].infect(self.sim.infection_probability)

                elif i == len(self.population) - 1 and self.population[i - 1].is_infected:
                    self.population[i].infect(self.sim.infection_probability)

    def update(self):
        """Update the whole population by updating each individual person"""
        self.sim.day_number += 1

        for person in self.population:
            person.update(self.sim.mortality_rate, self.sim.infection_duration)

    def display_statistics(self):
        """Display the current statistics of the population"""
        total_infected_count = 0
        total_death_count = 0

        for person in self.population:
            if person.is_infected:
                total_infected_count += 1
                if person.is_dead:
                    total_death_count += 1

        infected_percent = total_infected_count * 100 / self.sim.population_size
        infected_percent = round(infected_percent, 4)

        death_percent = total_death_count * 100 / self.sim.population_size
        death_percent = round(death_percent, 4)

        # Statistics summary
        print('\n----Day # {}----'.format(self.sim.day_number))
        print('Percentage of Population Infected: {}%'.format(infected_percent))
        print('Percentage of Population Dead: {}%'.format(death_percent))
        print('Total People Infected: {}/{}'.format(total_infected_count, self.sim.population_size))
        print('Total Deaths: {}/{}'.format(total_death_count, self.sim.population_size))

    def graphics(self):
        """
        A graphical representation for a population. `O` is healthy,
        `I` is infected and `X` is dead.
        """
        status = []

        for person in self.population:
            if person.is_dead:
                char = 'X'
            else:
                if person.is_infected:
                    char = 'I'
                else:
                    char = 'O'
            status.append(char)

        for i in range(len(status)):
            char = status[i]

            if i % 30 == 0 and i > 0:
                print(char, end='\n')

            print(char, end='-')
        print('')  # For formatting purpose only


def simulate():
    """Simulate the infection by N number of days"""
    simulation = Simulation()
    population = Population(simulation)

    population.initial_infection()
    population.display_statistics()

    print('\n`O` represents a healthy person')
    print('`I` represents an infected person')
    print('`X` represents a dead person')
    population.graphics()
    # Prompt user to press enter to begin the simulation
    input('\nPress enter to begin the simulation')

    # Run simulation
    for day in range(1, simulation.sim_days):
        population.spread_infection()
        population.update()
        population.display_statistics()
        population.graphics()

        if day != simulation.sim_days - 1:
            input('\nPress enter to advance to the next day.')


simulate()
