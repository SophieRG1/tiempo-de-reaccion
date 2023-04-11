corriendo = False
inicio_incorrecto = False
apagado = 0

def on_pin_pressed_p0():
    global corriendo, inicio_incorrecto
    basic.show_number(3)
    basic.show_number(2)
    basic.show_number(1)
    basic.clear_screen()
    corriendo = False
    inicio_incorrecto = False
    basic.pause(1000 + randint(0, 2000))
    if inicio_incorrecto == False:
        corriendo = True
        led.stop_animation()
        basic.clear_screen()
        basic.show_leds("""
            . # # # .
                        # . . . #
                        # . # . #
                        # . . . #
                        . # # # .
        """)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p2():
    global corriendo, apagado, inicio_incorrecto
    if corriendo:
        corriendo = False
        apagado = input.running_time()
        basic.show_leds("""
            . . # # #
                        . . . . #
                        . . . . #
                        . . . . #
                        . . # # #
        """)
        basic.pause(1000)
    else:
        inicio_incorrecto = True
        basic.show_leds("""
            . . # . #
                        . . . # .
                        . . # . #
                        . . . . .
                        . . . . .
        """)
        basic.pause(500)
        basic.clear_screen()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    global corriendo, apagado, inicio_incorrecto
    if corriendo:
        corriendo = False
        apagado = input.running_time()
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # . . . .
                        # . . . .
                        # # # . .
        """)
        basic.pause(1000)
    else:
        inicio_incorrecto = True
        basic.show_leds("""
            # . # . .
                        . # . . .
                        # . # . .
                        . . . . .
                        . . . . .
        """)
        basic.pause(500)
        basic.clear_screen()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
