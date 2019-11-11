import numpy as np

from InitialSolutionGenerator import InitialSolutionGenerator
from StadiumOrder import StadiumOrder
from TaskRequirements import TaskRequirements

if __name__ == "__main__":
    time_matrix = np.array([
        [0, 50, 20, 40],
        [50, 0, 100, 30],
        [20, 100, 0, 70],
        [40, 30, 70, 0]
    ])
    visit_order_constraints = [StadiumOrder(2, 3)]
    skip_order_constraints = [StadiumOrder(0, 0)]
    task_requirements = TaskRequirements(time_matrix, visit_order_constraints, skip_order_constraints)
    initial_solution_generator = InitialSolutionGenerator(task_requirements)
    ants_amount = 4
    ants = []
    for i in range(ants_amount):
        initial_solution_generator = InitialSolutionGenerator(task_requirements)
        solution = initial_solution_generator.generate(0)

        if solution is None:
            print('NOT FOUND')
        else :
            solution.print()
        print()
