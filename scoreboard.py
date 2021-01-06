from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 0
        self.penup()
        self.goto(-5, 270)
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.__score}', align=ALIGNMENT, font=FONT)

    def add(self):
        self.__score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)
