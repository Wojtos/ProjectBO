import numpy as np

class TaskRequirements:
    def __init__(self, time_matrix, visit_order_constraints, skip_order_constraints):
        self.time_matrix = time_matrix
        self._visit_order_constraints = visit_order_constraints
        self._skip_order_constraints = skip_order_constraints


    def size(self):
        return self.time_matrix.shape[0]

    def get_journey_time(self, start, end):
        return self.time_matrix[start][end]

    @property
    def visit_order_constraints(self):
        return self._visit_order_constraints

    @property
    def skip_order_constraints(self):
        return self._skip_order_constraints