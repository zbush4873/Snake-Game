from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
with open("data.txt") as file:
    data = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.high_score = data
        self.show_score()

    def show_score(self):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            # with open("data.txt", mode="w") as h_s:
            #     h_s.write(str(self.high_score))
            # with open("data.txt", mode="r") as data:
            #     high = data.read()
            # self.high_score = high
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
    #     self.goto(x=0, y=-40)
    #     self.write(f"Final score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()
