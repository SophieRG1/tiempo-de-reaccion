let corriendo = false
let inicio_incorrecto = false
input.onPinPressed(TouchPin.P0, function () {
    corriendo = false
    inicio_incorrecto = false
    basic.clearScreen()
    basic.showNumber(3)
    basic.showNumber(2)
    basic.showNumber(1)
    basic.clearScreen()
    basic.pause(1000 + randint(0, 4000))
    if (inicio_incorrecto == false && corriendo == false) {
        corriendo = true
        led.stopAnimation()
        basic.clearScreen()
        basic.showLeds(`
            . # . # .
            . . . . .
            . . # . .
            # . . . #
            . # # # .
            `)
    }
})
input.onPinPressed(TouchPin.P2, function () {
    if (inicio_incorrecto == false && corriendo == true) {
        corriendo = false
        basic.showLeds(`
            . . # # .
            . . . # #
            # # # # #
            . . . # #
            . . # # .
            `)
        basic.pause(1000)
    } else {
        inicio_incorrecto = true
        basic.showLeds(`
            . . # . #
            . . . # .
            . . # . #
            . . . . .
            . . . . .
            `)
        basic.pause(500)
    }
})
input.onPinPressed(TouchPin.P1, function () {
    if (inicio_incorrecto == false && corriendo == true) {
        corriendo = false
        basic.showLeds(`
            . # # . .
            # # . . .
            # # # # #
            # # . . .
            . # # . .
            `)
        basic.pause(1000)
    } else {
        inicio_incorrecto = true
        basic.showLeds(`
            # . # . .
            . # . . .
            # . # . .
            . . . . .
            . . . . .
            `)
        basic.pause(500)
    }
})
