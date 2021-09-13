class Rocket():
    def __init__(self, x_loc, y_loc, height=200):
        self.height = height
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.rocket_velo = 10

    def move_up(self):
        self.y_loc -= self.rocket_velo



enemy_rockets = [Rocket() for i in range(10)]


for rocket in enemy_rockets:
    print(rocket)
