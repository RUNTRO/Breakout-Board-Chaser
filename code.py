import time
import board
import digitalio

zero = digitalio.DigitalInOut(board.GP0)
zero.direction = digitalio.Direction.OUTPUT
first = digitalio.DigitalInOut(board.GP1)
first.direction = digitalio.Direction.OUTPUT
second = digitalio.DigitalInOut(board.GP2)
second.direction = digitalio.Direction.OUTPUT
third = digitalio.DigitalInOut(board.GP3)
third.direction = digitalio.Direction.OUTPUT
forth = digitalio.DigitalInOut(board.GP4)
forth.direction = digitalio.Direction.OUTPUT
five = digitalio.DigitalInOut(board.GP5)
five.direction = digitalio.Direction.OUTPUT
six = digitalio.DigitalInOut(board.GP6)
six.direction = digitalio.Direction.OUTPUT
seven = digitalio.DigitalInOut(board.GP7)
seven.direction = digitalio.Direction.OUTPUT
eight = digitalio.DigitalInOut(board.GP8)
eight.direction = digitalio.Direction.OUTPUT
nine = digitalio.DigitalInOut(board.GP9)
nine.direction = digitalio.Direction.OUTPUT
ten = digitalio.DigitalInOut(board.GP10)
ten.direction = digitalio.Direction.OUTPUT
eleven = digitalio.DigitalInOut(board.GP11)
eleven.direction = digitalio.Direction.OUTPUT
twelve = digitalio.DigitalInOut(board.GP12)
twelve.direction = digitalio.Direction.OUTPUT
thirteen = digitalio.DigitalInOut(board.GP13)
thirteen.direction = digitalio.Direction.OUTPUT
fourteen = digitalio.DigitalInOut(board.GP14)
fourteen.direction = digitalio.Direction.OUTPUT
fiveteen = digitalio.DigitalInOut(board.GP15)
fiveteen.direction = digitalio.Direction.OUTPUT
sixteen = digitalio.DigitalInOut(board.GP16)
sixteen.direction = digitalio.Direction.OUTPUT
seventeen = digitalio.DigitalInOut(board.GP17)
seventeen.direction = digitalio.Direction.OUTPUT
eighteen = digitalio.DigitalInOut(board.GP18)
eighteen.direction = digitalio.Direction.OUTPUT
nineteen = digitalio.DigitalInOut(board.GP19)
nineteen.direction = digitalio.Direction.OUTPUT
twenty = digitalio.DigitalInOut(board.GP20)
twenty.direction = digitalio.Direction.OUTPUT
twentyfirst = digitalio.DigitalInOut(board.GP21)
twentyfirst.direction = digitalio.Direction.OUTPUT
twentysecond = digitalio.DigitalInOut(board.GP22)
twentysecond.direction = digitalio.Direction.OUTPUT
twentysix = digitalio.DigitalInOut(board.GP26)
twentysix.direction = digitalio.Direction.OUTPUT
twentyseven = digitalio.DigitalInOut(board.GP27)
twentyseven.direction = digitalio.Direction.OUTPUT
twentyeight = digitalio.DigitalInOut(board.GP28)
twentyeight.direction = digitalio.Direction.OUTPUT

while True:
    zero.value = True
    time.sleep(.5)
    zero.value = False
    first.value = True
    time.sleep(.5)
    first.value = False
    second.value = True
    time.sleep(.5)
    second.value = False
    third.value = True
    time.sleep(.5)
    third.value = False
    forth.value = True
    time.sleep(.5)
    forth.value = False
    five.value = True
    time.sleep(.5)
    five.value = False
    six.value = True
    time.sleep(.5)
    six.value = False
    seven.value = True
    time.sleep(.5)
    seven.value = False
    eight.value = True
    time.sleep(.5)
    eight.value = False
    nine.value = True
    time.sleep(.5)
    nine.value = False
    ten.value = True
    time.sleep(.5)
    ten.value = False
    eleven.value = True
    time.sleep(.5)
    eleven.value = False
    twelve.value = True
    time.sleep(.5)
    twelve.value = False
    thirteen.value = True
    time.sleep(.5)
    thirteen.value = False
    fourteen.value = True
    time.sleep(.5)
    fourteen.value = False
    fiveteen.value = True
    time.sleep(.5)
    fiveteen.value = False
    sixteen.value = True
    time.sleep(.5)
    sixteen.value = False
    seventeen.value = True
    time.sleep(.5)
    seventeen.value = False
    eighteen.value = True
    time.sleep(.5)
    eighteen.value = False
    nineteen.value = True
    time.sleep(.5)
    nineteen.value = False
    twenty.value = True
    time.sleep(.5)
    twenty.value = False
    twentyfirst.value = True
    time.sleep(.5)
    twentyfirst.value = False
    twentysecond.value = True
    time.sleep(.5)
    twentysecond.value = False
    twentysix.value = True
    time.sleep(.5)
    twentysix.value = False
    twentyseven.value = True
    time.sleep(.5)
    twentyseven.value = False
    twentyeight.value = True
    time.sleep(.5)
    twentyeight.value = False
