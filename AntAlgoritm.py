import random

from Ant import Ant
from StadiumOrder import StadiumOrder


class AntAlgoritm:
    def __init__(self, task_requirements):
        self.alpha = 1
        self.betha = 5
        self.iterations_amount = 1000
        self.random_factor = 0.01
        self.evaporation = 0.5
        self.Q = 500
        self.task_requirements = task_requirements
        self.stadiums_amount = self.task_requirements.size()
        self.best_ant = None
        self.best_iteration = 0

    def solve(self):
        for i in range(self.iterations_amount):
            self.trails = [[1.0] * self.stadiums_amount] * self.stadiums_amount
            self.ants = [Ant(self.task_requirements) for i in range(self.stadiums_amount)]
            for ant in self.ants:
                ant.generate_random()
            try:
                self.move_ants()
                self.update_trails()
                self.update_best(i)
            except:
                pass
        return self.best_ant

    def move_ants(self):
            for ant in self.ants:
                while not ant.ended():
                    self.move_ant(ant)


    def move_ant(self, ant):
        if random.random() < self.random_factor:
            ant.generate_random()
        else:
            probabilites = self.calculate_probabilities(ant)
            stadium_index = self.cacluate_index(probabilites)
            current_index = ant.get_current_index()
            stadium_order = StadiumOrder(stadium_index, current_index)
            ant.add(stadium_order)




    def calculate_probabilities(self, ant):
        previous_stadium_index = ant.get_current_stadium_index()
        free_stadiums_index = ant.exclude_skip_order_constraints(ant.get_current_index())
        probabilites = [0] * self.stadiums_amount
        pheronome = 0.0

        for free_index in free_stadiums_index:
            pheronome += self.trails[previous_stadium_index][free_index] ** self.alpha * (1.0 / self.task_requirements.get_journey_time(previous_stadium_index, free_index)) ** self.betha
        for stadium_index in range(self.stadiums_amount):
            if stadium_index in free_stadiums_index:
                numerator = self.trails[previous_stadium_index][stadium_index] ** self.alpha * (1.0 / self.task_requirements.get_journey_time(previous_stadium_index, stadium_index)) ** self.betha
                probabilites[stadium_index] = numerator / pheronome
        return probabilites

    def cacluate_index(self, probabilites):
        sum_probabilites = sum(probabilites)
        random_double = random.uniform(0, sum_probabilites)
        current_sum = 0
        for stadium_index in range(self.stadiums_amount):
            current_sum += probabilites[stadium_index]
            if current_sum > random_double:
                return stadium_index
        raise Exception('Bad road!')

    def update_trails(self):
        for i in range(self.stadiums_amount):
            for j in range(self.stadiums_amount):
                self.trails[i][j] *= self.evaporation
        for ant in self.ants:
            contribution = self.Q / ant.trail_length()
            for i in range(self.stadiums_amount - 1):
                self.trails[ant.get(i).stadium_index][ant.get(i + 1).stadium_index] += contribution

    def update_best(self, iteration):
        if self.best_ant is None:
            self.best_ant = self.ants[0]

        for ant in self.ants:
            if ant.trail_length() < self.best_ant.trail_length():
                self.best_ant = ant
                self.best_iteration = iteration
                print(iteration)
