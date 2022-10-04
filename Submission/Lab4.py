from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
elp = (220, 220, 220)

def trinket_logo(G=green,Y=yellow,B=blue,O=nothing):

    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo(G=green,R=red,O=nothing):

    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus(W=white,O=nothing):

    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals(W=white,O=nothing):

    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart(P=pink,O=nothing):

    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
def elphant(o=nothing,c1=white,c2=elp):

    elephant = [
        o, o, c1, c1, o, o, o, o,
        o, c1, c1, c1, c1, c1, c1, o,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, c1, c1, c1, c1, c1, c1, c1,
        c1, c2, c2, c1, c1, c1, c1, c1,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, o, c1, c1, o, c1, c1, o,
        c1, o, c2, c1, o, c2, c1, o,
    ]
    return elephant

def getUserChoice():
    while True:
        print("""
        1.Logo
        2.Plus
        3.Equal
        4.Raspi
        5.Heart
        6.Elephant
        7.Exit
        """)
        while True:
            try:
                ans = int(input("\nEnter your Choice: "))
            except ValueError:
                print("Please enter a valid integer")
                continue
            else:
                break
        if ans == 1:
            s.set_pixels(trinket_logo())
        elif ans == 2:
            s.set_pixels(plus())
        elif ans == 3:
            s.set_pixels(equals())
        elif ans == 4:
            s.set_pixels(raspi_logo())
        elif ans == 5:
            s.set_pixels(heart())
        elif ans == 6:
            s.set_pixels(elphant())
        elif ans == 7:
            break
        else:
            print("\n Not Valid Choice Try again")

getUserChoice()
images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart,elphant]
count = 0
while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1