function checkInput (numberOfDigits: number, numberOfletters: number) {
    isValid = true
    if (numberOfDigits < 2 || (numberOfletters < 4 || numberOfDigits + numberOfletters < 8)) {
        isValid = false
    }
    return isValid
}
function getNumber () {
    return randint(0, 9)
}
input.onButtonPressed(Button.A, function () {
    letters += 1
    basic.showNumber(letters)
})
function getLetter () {
    if (Math.randomBoolean()) {
        return String.fromCharCode(randint(65, 90))
    } else {
        return String.fromCharCode(randint(97, 122))
    }
}
input.onButtonPressed(Button.AB, function () {
    if (checkInput(digits, letters)) {
        basic.showString("" + (showOutput()))
    } else {
        basic.showIcon(IconNames.Sad)
        music.playTone(131, music.beat(BeatFraction.Double))
    }
})
function showOutput () {
    output = 0
    return output
}
input.onButtonPressed(Button.B, function () {
    digits += 1
    basic.showNumber(digits)
})
let output = 0
let isValid = false
let digits = 0
let letters = 0
letters = 0
digits = 0
