class Player:

    def __init__(self):
        self.points = 0

    def add_points(self):
        self.points += 1

    def make_move(self, move):
        self.move = move