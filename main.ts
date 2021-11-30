radio.onReceivedNumber(function (receivedNumber) {
    nbLeds = receivedNumber
    range2.clear()
    range2 = strip.range(0, 30 - 5 * (30 - receivedNumber))
})
let nbLeds = 0
let range2: neopixel.Strip = null
let strip: neopixel.Strip = null
radio.setGroup(79)
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
range2 = strip.range(0, 1)
basic.forever(function () {
    range2.showColor(neopixel.rgb(40 * (0 - (25 - nbLeds)), 0, 200))
    range2.show()
})
