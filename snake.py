from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.__segments = []
        self.create_snake()
        self.__head = self.__segments[0]

    @property
    def head(self):
        return self.__head

    @property
    def segments(self):
        return self.__segments

    def add_segment(self, position):
        square = Turtle(shape='square')
        square.penup()
        square.color('white')
        square.goto(position)
        self.__segments.append(square)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def new_segment(self):
        last_square_position = self.__segments[-1].position()
        self.add_segment(last_square_position)

    def move(self):
        for square_number in range(len(self.__segments) - 1, 0, -1):
            new_position = self.__segments[square_number - 1].position()
            self.__segments[square_number].goto(new_position)
        self.__head.forward(MOVE_DISTANCE)

    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)

    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)
