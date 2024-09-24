from turtle import Screen, Turtle


table_cursor = Turtle()
legs_cursor = Turtle()
cake_cursor = Turtle()
candle_cursor = Turtle()


def draw_table(width, height, color, table): #Draws a rectangular table

    
    table.color(color)
    table.fillcolor(color)
    table.penup()
    table.goto(-width / 2, -height / 2)  # Center the table vertically
    table.pendown()
    table.begin_fill()
    table.forward(width)
    table.left(90)
    table.forward(height)
    table.left(90)
    table.forward(width)
    table.left(90)
    table.forward(height)
    table.left(90)
    table.end_fill()
    table.hideturtle()



def draw_leg(x, y, width, height, color, legs): #Draws one leg of the table
    
    # Front of the leg
    legs.color(color) 
    legs.fillcolor(color)
    legs.penup()
    legs.goto(x, y)
    legs.pendown()
    legs.begin_fill()
    legs.forward(width)
    legs.right(90)
    legs.forward(height)
    legs.right(90)
    legs.forward(width)
    legs.right(90)
    legs.forward(height)
    legs.end_fill()
    legs.right(90)



def draw_cake(width, height, cake):
    """
    Draws a multi-layered cake using turtle library.

    Parameters:
    width(int): The width of the cake.
    height(int): The width of the cake.
    cake(Turtle): The turtle object responsible for drawing the cake.
    The for loop in this block of code is used so that the we don't have to manually repeate the same same block of code four times
    for each layer, the loop itrates through the colors list and fills the color in each layer in the same order and moves up to draw the next layer on top of the previous one.
    """
    
    colors = ["brown", "pink", "red", "yellow"]
    layer_height = height // len(colors)
    cake.penup()
    cake.goto(-width / 2, 0)

    for color in colors:
        cake.fillcolor(color)
        cake.pendown()
        cake.begin_fill()
        cake.forward(width)
        cake.left(90)
        cake.forward(layer_height)
        cake.left(90)
        cake.forward(width)
        cake.left(90)
        cake.forward(layer_height)
        cake.left(90)
        cake.end_fill()
        cake.penup()
        cake.goto(-width / 2, cake.ycor() + layer_height)

def draw_candle(x, y, candle_width, candle_height, candle):
    """
    Draws a candle on top of the cake using turtle library, including a flame.

    Parameters:
    x(int): The x-coordinate of the candle's base.
    y(int): The y-coordinate of the candle's base.
    candle_width(int): The width of the candle.
    candle_height(int): The height of the candle.
    candle(Turtle): Thhe turtle object responsible for tdrawing the candle.

    """
    candle.color("sky blue")
    candle.fillcolor("sky blue")
    candle.penup()
    candle.goto(x, y)
    candle.pendown()
    candle.begin_fill()
    candle.setheading(90)  # Face upwards
    candle.forward(candle_height)
    candle.right(90)
    candle.forward(candle_width)
    candle.right(90)
    candle.forward(candle_height)
    candle.right(90)
    candle.forward(candle_width)
    candle.end_fill()

    # Candle flame
    candle.fillcolor("orange")
    candle.begin_fill()
    candle.penup()
    candle.goto(x + candle_width / 2, y + candle_height)
    candle.pendown()
    candle.circle(7)  # Flame size
    candle.end_fill()
    candle.hideturtle()



# Get user inputs

table_width = int(input("Enter the table width: "))
table_height = int(input("Enter the table height: "))
table_color = input("Enter the table color: ")
cake_width = int(input("Enter the cake width: "))
cake_height = int(input("Enter the cake height: "))




# Draw the objects
draw_table(table_width, table_height, table_color, table_cursor)

draw_leg((-table_width/2), (table_height/2), (table_height/2), (table_width/2), table_color, legs_cursor)
draw_leg((-table_width/4), (table_height/2), (table_height/2), (table_width/2), table_color, legs_cursor)
draw_leg((table_width/4), (table_height/2), (table_height/2), (table_width/2), table_color, legs_cursor)
draw_leg((table_width/2), (table_height/2), (table_height/2), (table_width/2), table_color, legs_cursor)

draw_cake(cake_width, cake_height, cake_cursor)




candle_width = 10
candle_height = 50
draw_candle(20, cake_height, candle_width, candle_height, candle_cursor)  # Centered on the cake's top


print("Your cake is ready! Happy Birthday!")

input("press enter to exit")
