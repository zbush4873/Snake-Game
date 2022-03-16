from turtle import Turtle
import random
colors = ["red", "blue", "green", "orange", "yellow", "purple", "white"]


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        for _ in range(1):
            random_color = random.choice(colors)
            self.color(random_color)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
