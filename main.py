global number
basic.show_string("Truth Or Dare!")
def on_button_pressed_a():
    number = randint(0, 1)
    if number == 0:
        basic.show_string("Truth")
    elif number == 1:
        basic.show_string("Dare")
input.on_button_pressed(Button.A, on_button_pressed_a)

def b():
    number = randint(0, 3)
    if number == 0:
        basic.show_arrow(ArrowNames.NORTH)
    elif number == 1:
        basic.show_arrow(ArrowNames.SOUTH)
    elif number == 2:
        basic.show_arrow(ArrowNames.EAST)
    else:
        basic.show_arrow(ArrowNames.WEST)
input.on_button_pressed(Button.B, b)
