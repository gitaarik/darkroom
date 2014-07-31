class Player(object):

    def __init__(self):
        self._items = {}

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        self._items[item.name] = item

    def has_item(self, item_name):
        return item_name in self._items.keys()

player = Player()
