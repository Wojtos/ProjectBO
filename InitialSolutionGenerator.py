import random

from Solution import Solution
from StadiumOrder import StadiumOrder


class InitialSolutionGenerator:
    def __init__(self, task_requirements):
        self.task_requirements = task_requirements
        self.solution = Solution(self.task_requirements.size())
        self.add_visit_order_constraints()

    def add_visit_order_constraints(self):
        for stadium_order in self.task_requirements.visit_order_constraints:
            self.solution.add(stadium_order)

    def generate(self, current_index):
        if self.solution.ended():
            return self.solution
        free_stadiums_index = self.solution.get_free_stadiums_index()
        free_stadiums_index = self.exclude_skip_order_constraints(current_index, free_stadiums_index)
        random.shuffle(free_stadiums_index)
        for stadium_index in free_stadiums_index:
            stadium_order = StadiumOrder(stadium_index, current_index)
            self.solution.add(stadium_order)
            return self.solution

        return None

    def add_visit_order_constraints(self):
        for stadium_order in self.task_requirements.visit_order_constraints:
            self.solution.add(stadium_order)

    def exclude_skip_order_constraints(self, current_index, free_stadiums_index):
        excluded_statium_indexes = list(map(
            lambda x: x.stadium_index,
            filter(
                lambda x: x.order == current_index,
                self.task_requirements.skip_order_constraints
            )
        ))
        return list(filter(
            lambda x: x not in excluded_statium_indexes,
            free_stadiums_index
        ))