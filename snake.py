from turtle import Turtle, Screen
screen = Screen()
NUM_OF_SNAKES = 3
MOVEMENT_SPEED = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        super().__init__()
        self.x_pos = 20
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        self.x_pos -= 20
        new_snake = Turtle("square")
        new_snake.color("red")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def reset(self):
        for snake in self.snakes:
            snake.goto(999, 999)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for seg in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg - 1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.snakes[0].forward(MOVEMENT_SPEED)

        def snake_up():
            if self.snakes[0].heading() == 270:
                pass
            else:
                self.snakes[0].setheading(90)

        def snake_right():
            if self.snakes[0].heading() == 180:
                pass
            else:
                self.snakes[0].setheading(0)

        def snake_left():
            if self.snakes[0].heading() == 0:
                pass
            else:
                self.snakes[0].setheading(180)

        def snake_down():
            if self.snakes[0].heading() == 90:
                pass
            else:
                self.snakes[0].setheading(270)

        screen.listen()
        screen.onkeypress(key="d", fun=snake_right)
        screen.onkeypress(key="a", fun=snake_left)
        screen.onkeypress(key="w", fun=snake_up)
        screen.onkeypress(key="s", fun=snake_down)

        screen.onkeypress(key="Right", fun=snake_right)
        screen.onkeypress(key="Left", fun=snake_left)
        screen.onkeypress(key="Up", fun=snake_up)
        screen.onkeypress(key="Down", fun=snake_down)
