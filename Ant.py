import random

from StadiumOrder import StadiumOrder


class Ant:
    def __init__(self, task_requirements):
        self.size = task_requirements.size()
        self.task_requirements = task_requirements
        self.clear()

    def clear(self):
        self.stadium_orders = [None] * self.size
        self.add_visit_order_constraints()

    def trail_length(self):
        length = 0
        for i in range(len(self.stadium_orders) - 1):
            length += self.task_requirements.get_journey_time(
                self.stadium_orders[i].stadium_index,
                self.stadium_orders[i + 1].stadium_index
            )
        return length

    def add(self, stadium_order):
        self.stadium_orders[stadium_order.order] = stadium_order

    def remove(self, stadium_order):
        self.stadium_orders[stadium_order.order] = None

    def get(self, order):
        return self.stadium_orders[order]

    def ended(self):
        return self.stadium_orders.count(None) == 0

    def get_free_stadiums_index(self):
        booked_stadiums_index = list(map(
            lambda x: x.stadium_index if x is not None else None,
            self.stadium_orders
        ))

        all_stadiums_index = range(self.size)
        return list(filter(
            lambda x: x not in booked_stadiums_index,
            all_stadiums_index
        ))

    def get_current_index(self):
        for i in range(self.size):
            if self.stadium_orders[i] is None:
                return i
        return None

    def get_current_stadium_index(self):
        previous_index = self.get_current_index() - 1
        return self.stadium_orders[previous_index].stadium_index

    def add_visit_order_constraints(self):
        for stadium_order in self.task_requirements.visit_order_constraints:
            self.add(stadium_order)

    def exclude_skip_order_constraints(self, current_index):
        excluded_statium_indexes = list(map(
            lambda x: x.stadium_index,
            filter(
                lambda x: x.order == current_index,
                self.task_requirements.skip_order_constraints
            )
        ))
        return list(filter(
            lambda x: x not in excluded_statium_indexes,
            self.get_free_stadiums_index()
        ))

    def generate_random(self):
        if self.ended():
            return self
        current_index = self.get_current_index()
        free_stadiums_index = self.exclude_skip_order_constraints(current_index)
        random.shuffle(free_stadiums_index)
        for stadium_index in free_stadiums_index:
            stadium_order = StadiumOrder(stadium_index, current_index)
            self.add(stadium_order)
            return self

    def print(self):
        for index, stadium_order in enumerate(self.stadium_orders):
            if stadium_order is None:
                continue
            print(
                'Order: {}. stadium index: {}'.format(
                    stadium_order.order,
                    stadium_order.stadium_index
                ))
        print('Total length: {}'.format(
            self.trail_length()
        ))

    def print_with_names(self, stadiums_names):
        for index, stadium_order in enumerate(self.stadium_orders):
            if stadium_order is None:
                continue
            print(
                'Order: {}. stadium index: {}, club: {}'.format(
                    stadium_order.order,
                    stadium_order.stadium_index,
                    stadiums_names[stadium_order.stadium_index]
                ))
        print('Total length: {}'.format(
            self.trail_length()
        ))

