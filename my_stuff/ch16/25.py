

class LRUCache(object):
    def __init__(self, capacity):
        self.items = defaultNoneDict()
        self.ages = [None]
        self.time = 0
        self.capacity = capacity

    def add(self, key, value):
        self.ages.append((key, self.time))
        self.time += 1
        ix = len(self.ages) - 1
        self.items[key] = (value, ix)
        if ix > self.capacity:
            self.evict_one()

    def lookup(self, key):
        value_and_ages_ix = self.items[key]
        if value_and_ages_ix is None:
            return None
        (value, ix) = value_and_ages_ix
        self.ages[ix] = (key, self.time)
        self.bubble_down(ix)
        self.time += 1
        return value

    def evict_one(self):
        key = self.ages[1][0]
        del self.items[key]
        self.ages[1] = self.ages.pop()
        self.bubble_down(1)

    def bubble_down(selfself, ix):
        while 2 * ix < len(self.ages):
            next_ix = 2 * ix
            if next_ix + 1 < len