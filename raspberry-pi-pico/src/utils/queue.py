class Queue:
    def __init__(self):
        self._items = []

    def put(self, item):
        self._items.append(item)

    def get(self):
        if self.empty():
            return None
        return self._items.pop(0)

    def empty(self):
        return len(self._items) == 0