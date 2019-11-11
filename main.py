import numpy as np

from AntAlgoritm import AntAlgoritm
from StadiumOrder import StadiumOrder
from TaskRequirements import TaskRequirements

if __name__ == "__main__":
    time_matrix = np.array([
        [0, 50, 90, 40],
        [50, 0, 100, 30],
        [90, 100, 0, 70],
        [40, 30, 70, 0]
    ])
    visit_order_constraints = [StadiumOrder(2, 3)]
    skip_order_constraints = [StadiumOrder(0, 0)]
    task_requirements = TaskRequirements(time_matrix, visit_order_constraints, skip_order_constraints)
    ant_algoritm = AntAlgoritm(task_requirements)
    solution = ant_algoritm.solve()
    if solution is None:
        print('NOT FOUND')
    else :
        solution.print()
    print()
