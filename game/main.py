import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

class TurtleCrossingGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Turtle Crossing Game")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        self.buttons = []
        self.score_display = None

        self.player = None
        self.car_manager = None
        self.scoreboard = None

        self.show_start_menu()

        self.screen.mainloop()

    def create_button(self, x, y, label, callback):
        button = Turtle()
        button.shape("square")
        button.shapesize(stretch_wid=1.5, stretch_len=5)
        button.fillcolor("lightblue")
        button.penup()
        button.goto(x, y)
        button.onclick(callback)
        button.showturtle()

        label_turtle = Turtle()
        label_turtle.hideturtle()
        label_turtle.penup()
        label_turtle.goto(x, y - 10)
        label_turtle.write(label, align="center", font=("Arial", 12, "bold"))

        self.buttons.append(button)
        self.buttons.append(label_turtle)

    def clear_buttons(self):
        for b in self.buttons:
            b.clear()
            b.hideturtle()
        self.buttons.clear()

    def clear_score_display(self):
        if self.score_display:
            self.score_display.clear()
            self.score_display.hideturtle()
            self.score_display = None

    def handle_quit(self, x=None, y=None):
        self.screen.bye()

    def handle_scoreboard(self, x=None, y=None):
        self.clear_score_display()
        self.score_display = Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.goto(0, -50)
        self.score_display.write(
            "Scoreboard functionality is under development.",
            align="center",
            font=("Arial", 14, "bold")
        )

    def handle_start_game(self, x=None, y=None):
        self.clear_buttons()
        self.clear_score_display()
        self.start_game()

    def handle_restart(self, x=None, y=None):
        self.clear_buttons()
        self.clear_score_display()
        self.screen.bgcolor("white")
        self.start_game()

    def show_start_menu(self):
        self.screen.clear()
        self.screen.bgcolor("white")
        self.screen.update()
        self.create_button(-200, 0, "Start Game", self.handle_start_game)
        self.create_button(0, 0, "Quit", self.handle_quit)
        self.create_button(200, 0, "Scorecard", self.handle_scoreboard)

    def show_game_over_buttons(self):
        self.screen.clear()
        self.screen.bgcolor("white")
        self.screen.update()
        self.create_button(-200, 0, "Restart", self.handle_restart)
        self.create_button(0, 0, "Quit", self.handle_quit)
        self.create_button(200, 0, "Score", self.handle_scoreboard)

    def start_game(self):
        self.screen.clear()
        self.screen.bgcolor("white")
        self.screen.tracer(0)

        self.player = Player()
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkey(self.player.go_up, "Up")
        self.screen.onkey(self.player.go_down, "Down")
        self.screen.onkey(self.player.go_left, "Left")
        self.screen.onkey(self.player.go_right, "Right")

        game_is_on = True
        while game_is_on:
            time.sleep(0.1)
            self.screen.update()

            self.car_manager.create_car()
            self.car_manager.move_cars()

            for car in self.car_manager.all_cars:
                if car.distance(self.player) < 20:
                    game_is_on = False
                    self.scoreboard.game_over()
                    self.screen.update()
                    self.show_game_over_buttons()
                    break

            if self.player.is_at_finish_line():
                self.player.go_to_start()
                self.car_manager.level_up()
                self.scoreboard.increase_level()


if __name__ == "__main__":
    TurtleCrossingGame()
