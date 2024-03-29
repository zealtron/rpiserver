#!/usr/bin/python

from bootstrap import *

while True:
    #setup colors to loop through for fade

    colors = [
        (255.0,0.0,0.0),
        (0.0,255.0,0.0),
        (0.0,0.0,255.0),
        (255.0,255.0,255.0),
    ]
    step = 0.01
    for c in range(4):
        r, g, b = colors[c]
        level = 0.01
        dir = step
        while level >= 0.0:
            led.fill(Color(r, g, b, level))
            led.update()
            if(level >= 0.99):
                dir = -step
            level += dir
            #sleep(0.005)

    led.all_off()
    print 1

    #animations - each animation method moves the animation forward one step on each call
    #after each step, call update() to push it to the LED strip
    #sin wave animations
    anim = Wave(led, Color(255, 0,0), 2)
    for i in range(led.lastIndex):
        anim.step()
        led.update()
        #sleep(0.15)

    print 2
    anim = Wave(led, Color(0, 0, 100), 2)
    for i in range(led.lastIndex):
        anim.step()
        led.update()
        #sleep(0.15)


    print 3
    #rolling rainbow
    anim = Rainbow(led)
    for i in range(384):
        anim.step()
        led.update()

    led.fillOff()

    print 4
    #evenly distributed rainbow
    anim = RainbowCycle(led)
    for i in range(384*2):
        anim.step()
        led.update()

    led.fillOff()

    print 5
    #setup colors for wipe and chase
    colors = [
        Color(255, 0, 0),
        Color(0, 255, 0),
        Color(0, 0, 255),
        Color(255, 255, 255),
    ]


    for c in range(4):
        anim = ColorWipe(led, colors[c])

        for i in range(num):
            anim.step()
            led.update()
            #sleep(0.03)

    led.fillOff()

    print 6
    for c in range(4):
        anim = ColorChase(led, colors[c])

        for i in range(num):
            anim.step()
            led.update()
            #sleep(0.03)

    led.fillOff()

    print 7
    #scanner: single color and changing color
    anim = LarsonScanner(led, Color(255, 0, 0))
    for i in range(led.lastIndex*4):
        anim.step()
        led.update()
        #sleep(0.03)

    led.fillOff()

    print 8
    anim = LarsonRainbow(led, 2, 0.5)
    for i in range(led.lastIndex*4):
        anim.step()
        led.update()
        #sleep(0.03)

    led.all_off()


    print "done"

