def on_received_number(receivedNumber):
    global nbLeds, range2
    nbLeds = receivedNumber
    range2.clear()
    range2 = strip.range(25, receivedNumber)
radio.on_received_number(on_received_number)

nbLeds = 0
range2: neopixel.Strip = None
strip: neopixel.Strip = None
radio.set_group(79)
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
range2 = strip.range(0, 1)

def on_forever():
    range2.show_color(neopixel.rgb(40 * (0 - (25 - nbLeds)), 0, 200))
    range2.show()
basic.forever(on_forever)
