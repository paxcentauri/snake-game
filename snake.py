from turtle import Turtle
X_POSITIONS = [0, -20, -40]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]

    def create_snake(self):
        for x in range(3):
            self.add_segment(X_POSITIONS[x], 0)

    def add_segment(self, x_position, y_position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(x_position, y_position)
        self.segments.append(segment)

    def extend_snake(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        self.add_segment(x,y)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # note: index 0 will not be dealt with since the range does not include the endpoint, it always includes endpoint - 1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)
        # self.segments[0].left(90)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1039, 1038)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
