from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # screen size on x axis starts from -300 to 300
        random_y = random.randint(-280, 280)  # screen size on y axis starts from -300 to 300
        self.goto(random_x, random_y)
