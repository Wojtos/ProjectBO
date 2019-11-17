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

def ekstraklasa_stadiums():
    distance_matrix = np.array([
        [0.00, 278.56, 0.90, 241.56, 85.67, 335.81, 252.69, 90.82, 149.71, 192.50, 301.67, 102.18, 501.95, 489.34,
         528.03, 405.90],
        [278.56, 0.00, 279.25, 245.96, 260.13, 192.43, 99.71, 260.27, 134.72, 92.39, 270.94, 200.12, 228.10, 214.94,
         359.37, 240.76],
        [0.90, 279.25, 0.00, 242.42, 86.47, 336.71, 253.13, 91.61, 150.49, 193.27, 302.54, 102.45, 502.71, 490.09,
         528.93, 406.12],
        [241.56, 245.96, 242.42, 0.00, 159.19, 139.99, 307.18, 154.49, 171.74, 180.76, 60.15, 259.71, 388.09, 379.24,
         304.18, 476.95],
        [85.67, 260.13, 86.47, 159.19, 0.00, 268.90, 266.40, 5.16, 126.73, 167.74, 219.18, 145.67, 467.47, 455.80,
         455.29, 434.88],
        [335.81, 192.43, 336.71, 139.99, 268.90, 0.00, 285.31, 265.49, 208.01, 185.10, 118.50, 311.37, 258.28, 251.33,
         195.00, 431.00],
        [252.69, 99.71, 253.13, 307.18, 266.40, 285.31, 0.00, 268.44, 148.58, 126.55, 345.04, 153.99, 302.96, 289.53,
         458.88, 173.13],
        [90.82, 260.27, 91.61, 154.49, 5.16, 265.49, 268.44, 0.00, 127.45, 167.92, 214.42, 149.71, 466.18, 454.59,
         451.29, 437.44],
        [149.71, 134.72, 150.49, 171.74, 126.73, 208.01, 148.58, 127.45, 0.00, 43.55, 221.25, 103.40, 352.76, 340.30,
         402.66, 321.56],
        [192.50, 92.39, 193.27, 180.76, 167.74, 185.10, 126.55, 167.92, 43.55, 0.00, 221.64, 133.21, 309.52, 297.00,
         376.57, 298.05],
        [301.67, 270.94, 302.54, 60.15, 219.18, 118.50, 345.04, 214.42, 221.25, 221.64, 0.00, 315.19, 376.74, 369.57,
         252.34, 509.42],
        [102.18, 200.12, 102.45, 259.71, 145.67, 311.37, 153.99, 149.71, 103.40, 133.21, 315.19, 0.00, 428.22, 415.04,
         505.82, 303.89],
        [501.95, 228.10, 502.71, 388.09, 467.47, 258.28, 302.96, 466.18, 352.76, 309.52, 376.74, 428.22, 0.00, 13.45,
         287.83, 340.55],
        [489.34, 214.94, 490.09, 379.24, 455.80, 251.33, 289.53, 454.59, 340.30, 297.00, 369.57, 415.04, 13.45, 0.00,
         290.23, 329.41],
        [528.03, 359.37, 528.93, 304.18, 455.29, 195.00, 458.88, 451.29, 402.66, 376.57, 252.34, 505.82, 287.83, 290.23,
         0.00, 575.37],
        [405.90, 240.76, 406.12, 476.95, 434.88, 431.00, 173.13, 437.44, 321.56, 298.05, 509.42, 303.89, 340.55, 329.41,
         575.37, 0.00]
    ])

    stadium_names = ['WislaKrakw', 'WislaPlock', 'Cracovia', 'Slask', 'Gornik', 'Lech', 'Legia', 'Piast', 'Rakow', 'LKS', 'Zaglebie' , 'Korona', 'Arka', 'Lechia',	'Pogon', 'Jagiellonia']
    visit_order_constraints = [StadiumOrder(2, 0), StadiumOrder(14, 1), StadiumOrder(0, 2)]
    skip_order_constraints = [StadiumOrder(15, 15)]
    task_requirements = TaskRequirements(distance_matrix, visit_order_constraints, skip_order_constraints)
    ant_algoritm = AntAlgoritm(task_requirements)
    solution = ant_algoritm.solve()
    if solution is None:
        print('NOT FOUND')
    else:
        solution.print_with_names(stadium_names)
    print()

if __name__ == "__main__":
    #example1()
    # example2()
    ekstraklasa_stadiums()

