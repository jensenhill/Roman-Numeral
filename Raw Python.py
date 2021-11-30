def Input():
    while True:
        try:
            userInput = int(input("Enter the integer, which must be between 1-3999:"))
        except ValueError:
            print("ERROR: You must enter an integer between 1 and 3999.")
        else:
            if userInput < 1 or userInput > 3999:
                print("ERROR: You must enter an integer between 1 and 3999.")
            else:
                return userInput


def Convert(intInput):
    strInput = str(intInput)
    length = len(strInput)
    if length == 1:
        ones = int(strInput[0:1])
        firstChar = Ones(ones)
        numeral = firstChar
    if length == 2:
        tens = int(strInput[0:1])
        secondChar = Tens(tens)
        ones = int(strInput[1:2])
        firstChar = Ones(ones)
        numeral = secondChar + firstChar
    if length == 3:
        hundreds = int(strInput[0:1])
        thirdChar = Hundreds(hundreds)
        tens = int(strInput[1:2])
        secondChar = Tens(tens)
        ones = int(strInput[2:3])
        firstChar = Ones(ones)
        numeral = thirdChar + secondChar + firstChar
    if length == 4:
        thousands = int(strInput[0:1])
        fourthChar = Thousands(thousands)
        hundreds = int(strInput[1:2])
        thirdChar = Hundreds(hundreds)
        tens = int(strInput[2:3])
        secondChar = Tens(tens)
        ones = int(strInput[3:4])
        firstChar = Ones(ones)
        numeral = fourthChar + thirdChar + secondChar + firstChar
    return (numeral)


def Ones(index):
    characters = [[""], ["I"], ["II"], ["III"], ["IV"], ["V"], ["VI"], ["VII"], ["VIII"], ["IX"]]
    unit = characters[index][0]
    return (unit)


def Tens(index):
    characters = [[""], ["X"], ["XX"], ["XXX"], ["XL"], ["L"], ["LX"], ["LXX"], ["LXXX"], ["XC"]]
    unit = characters[index][0]
    return (unit)


def Hundreds(index):
    characters = [[""], ["C"], ["CC"], ["CCC"], ["CD"], ["D"], ["DC"], ["DCC"], ["DCCC"], ["CM"]]
    unit = characters[index][0]
    return (unit)


def Thousands(index):
    characters = [[""], ["M"], ["MM"], ["MMM"]]
    unit = characters[index][0]
    return (unit)


def Main():
    userInput = Input()
    numeral = Convert(userInput)
    print("Roman Numeral:", numeral)
    print("=============================================")


while True:
    Main()