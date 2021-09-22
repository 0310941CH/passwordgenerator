def checkInput(numberOfDigits: number, numberOfletters: number):
    global isValid
    isValid = True
    if numberOfDigits < 2 or (numberOfletters < 4 or numberOfDigits + numberOfletters < 8):
        isValid = False
    return isValid
def getNumber():
    return randint(0, 9)

def on_button_pressed_a():
    global letters
    letters += 1
    basic.show_number(letters)
input.on_button_pressed(Button.A, on_button_pressed_a)

def getLetter():
    if Math.random_boolean():
        return String.from_char_code(randint(65, 90))
    else:
        return String.from_char_code(randint(97, 122))

def on_button_pressed_ab():
    if checkInput(digits, letters):
        pass
    else:
        basic.show_icon(IconNames.SAD)
        music.play_tone(131, music.beat(BeatFraction.DOUBLE))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def showOutput():
    while checkInput(digits, letters) == True:
        pass

def on_button_pressed_b():
    global digits
    digits += 1
    basic.show_number(digits)
input.on_button_pressed(Button.B, on_button_pressed_b)

isValid = False
digits = 0
letters = 0
letters = 0
digits = 0