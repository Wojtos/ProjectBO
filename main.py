import numpy as np

from AntAlgoritm import AntAlgoritm
from StadiumOrder import StadiumOrder
from TaskRequirements import TaskRequirements

def example1():
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
    else:
        solution.print()
    print()

def example2():
    time_matrix = np.array(
        [[1000, 2, 2, 4, 3, 1000, 1000, 1000],
         [2, 1000, 2, 1000, 1000, 1, 1, 1000],
         [2, 2, 1000, 1000, 2, 1, 1000, 1000],
         [4, 1000, 1000, 1000, 1000, 2, 1000, 3],
         [3, 1000, 2, 1000, 1000, 1000, 4, 5],
         [1000, 1, 1, 2, 1000, 1000, 2, 2],
         [1000, 1, 1000, 1000, 4, 2, 1000, 2],
         [1000, 1000, 1000, 3, 5, 2, 2, 1000]]
    )
    task_requirements = TaskRequirements(time_matrix, [], [])
    ant_algoritm = AntAlgoritm(task_requirements)
    solution = ant_algoritm.solve()
    if solution is None:
        print('NOT FOUND')
    else:
        solution.print()
    print()

if __name__ == "__main__":
    #example1()
    example2()

