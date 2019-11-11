from Ant import Ant


class AntAlgoritm:
    def __init__(self, task_requirements):
        self.alpha = 1
        self.betha = 1
        self.task_requirements = task_requirements
        self.cities_amount = self.task_requirements.size()
        self.trails = self.clear_trails()
        self.ants = [Ant(self.cities_amount) for i in range(self.cities_amount)]

    def solve(self):
        pass

    def clear_trails(self):
        self.trails = [[1.0] * self.cities_amount] * self.cities_amount

        return self.trails
