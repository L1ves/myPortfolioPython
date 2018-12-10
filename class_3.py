class ball(object):
    def __init__(self):
        self.color = "red"
        self.shape = "round"
        self.place = "on the floor"
    def move(self):
        if self.place == "on the floor":
            self.place = "in your hands"
            print("You pick up the ball")
            return
        elif self.place == "in your hands":
            self.place = "on the floor"
            print("You set the ball down")
            return
    def bounce(self):
        if self.place == "in your hands":
            print("You bounce the ball")
            return
        else:
            print("You dont have the ball ")
            return
ball = ball()
print ball.color
print ball.shape
print ball.place
ball.move()
print ball.place
ball.bounce()
