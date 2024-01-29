import turtle

shapeInput = input("circle and square, what is your favorite shape?: ")

if shapeInput == "circle" or shapeInput == "square":
    colorInput = input ("What color will it be?, yellow, red or blue?: ")
    
    if colorInput == "yellow" or colorInput == "red" or colorInput == "blue":
        wn = turtle.Screen()
        wn.bgcolor ("#f9ebc2")
        wn.title("Your shape")

        displayShape = turtle.Turtle()
        displayShape.shape(shapeInput)
        displayShape.color(colorInput)

        turtle.done()

    else:
        print("Sorry, I don't have this collor :(")

else: 
    print("Sorry, I don't have this shape :(")