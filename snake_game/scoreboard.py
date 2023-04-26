from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            content = file.read()
            self.high_score = int(content)
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 278)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
