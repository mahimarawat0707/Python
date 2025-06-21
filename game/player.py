from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)  # face up

    def go_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)

    def go_left(self):
        if self.xcor() > -280:
            self.setx(self.xcor() - MOVE_DISTANCE)

    def go_right(self):
        if self.xcor() < 280:
            self.setx(self.xcor() + MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
