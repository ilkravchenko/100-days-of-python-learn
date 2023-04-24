from turtle import Turtle

FONT = ("Courier", 80, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-100, 195)
        self.write(self.l_score, align='center', font=FONT)
        self.goto(100, 195)
        self.write(self.r_score, align='center', font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.write_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write_score()