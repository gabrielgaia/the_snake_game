from turtle import Screen
from time import sleep
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game!')
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.075)
    snake.move()
    if snake.head.distance(food) < 15:
        food.move()
        snake.new_segment()
        scoreboard.add()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
