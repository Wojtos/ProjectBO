class Ant:
    def __init__(self, size):
        self.size = size
        self.clear()

    def clear(self):
        self.stadium_orders = [None] * self.size

    def visited(self, index):
        return self.visited[index]

    def trail_length(self, task_requirements):
        length = 0
        for i in range(len(self.trail) - 1):
            length += task_requirements.get_journey_time(self.trail[i], self.trail[i + 1])
        return length

    def add(self, stadium_order):
        self.stadium_orders[stadium_order.order] = stadium_order

    def remove(self, stadium_order):
        self.stadium_orders[stadium_order.order] = None

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

    def print(self):
        for index, stadium_order in enumerate(self.stadium_orders):
            if stadium_order is None:
                continue
            print(
                'Order: {}. stadium index: {}'.format(
                    stadium_order.order,
                    stadium_order.stadium_index
                ))

