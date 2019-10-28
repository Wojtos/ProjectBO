class StadiumOrder:
    def __init__(self, stadium_index, order):
        self._stadium_index = stadium_index
        self._order = order

    @property
    def stadium_index(self):
        return self._stadium_index

    @property
    def order(self):
        return self._order

    @stadium_index.setter
    def stadium_index(self, stadium_index):
        self._stadium_index = stadium_index

    @order.setter
    def order(self, order):
        self._order = order