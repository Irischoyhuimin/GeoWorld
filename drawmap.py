import turtle

#list = [["name",20,40,"asd"],["name", 60,70,"dfs"], ["asfdas",213,35, "das"],['sada', 342,231,'sdas']]
def drawmap(alist):
    for i in range(len(alist)):
        x = alist[i].longtitude
        y = alist[i].latitude
        point = turtle.Turtle()
        point.hideturtle()
        point.penup()
        point.goto(x,y)
        point.dot()
    turtle.exitonclick()
