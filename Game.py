class Game:

    def __init__(self):
        self.points_home = 0
        self.points_away = 0
        self.sets_home = 0
        self.sets_away = 0
        self.set_nr = 1
        self.reset = 0

    def get_max_points(self):
        if self.set_nr < 5:
            return 25
        else:
            return 15

    def score(self, team):

        if team == "H":
            self.points_home += 1

        if team == "A":
            self.points_away += 1

        if team == "R":
            self.points_home = 0
            self.points_away = 0
            self.sets_home = 0
            self.sets_away = 0

        if self.points_home >= self.get_max_points():
            if self.points_away < self.points_home - 1:
                self.points_home = 0
                self.points_away = 0
                self.sets_home += 1
                self.set_nr += 1

        if self.points_away >= self.get_max_points():
            if self.points_home < self.points_away - 1:
                self.points_home = 0
                self.points_away = 0
                self.sets_away += 1
                self.set_nr += 1

