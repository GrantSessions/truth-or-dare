
basic.showString("Truth Or Dare!")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let number = randint(0, 1)
    if (number == 0) {
        basic.showString("Truth")
    } else if (number == 1) {
        basic.showString("Dare")
    }
    
})
input.onButtonPressed(Button.B, function b() {
    let number = randint(0, 3)
    if (number == 0) {
        basic.showArrow(ArrowNames.North)
    } else if (number == 1) {
        basic.showArrow(ArrowNames.South)
    } else if (number == 2) {
        basic.showArrow(ArrowNames.East)
    } else {
        basic.showArrow(ArrowNames.West)
    }
    
})
