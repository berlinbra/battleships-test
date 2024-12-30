class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.positions = []
        self.hits = 0

    def is_sunk(self):
        return self.hits >= self.length