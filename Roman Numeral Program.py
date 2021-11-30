import time
from tkinter import *
import tkinter.font as font

def Input():
    while True:
        global txt
        checkNum = txt
        global inputText
        global userInput
        global response
        userInput = 0
        try:
            #Pull text field input
            userInput = int(inputText.get())
        except ValueError:
            #ERROR MESSAGE
            response.destroy()
            response = Label(window, text="ERROR: You must enter an integer between 1 and 3999.")
            response.config(font=("Calibri Bold", 20),bg="red",foreground="black")
            response.pack(pady=180, padx=25, anchor='s')

            break
        else:
            #NOW TREATING INPUT AS INTEGER
            if userInput < 1 or userInput > 3999:
                #ERROR MESSAGE
                response.destroy()
                response = Label(window, text="ERROR: You must enter an integer between 1 and 3999.")
                response.config(font=("Calibri Bold", 20),bg="red",foreground="black")
                response.pack(pady=180, padx=25, anchor='s')
                break
            else:
                #CONVERT THE NUMBER
                Convert(userInput)
                break


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
    global response
    global background
    #CLEAR PREVIOUS TEXT (ERROR MESSAGE/NUMERAL)
    response.destroy()
    #DISPLAY NEW NUMERAL
    response = Label(window, text=numeral)
    textFont = font.Font(family='Tahoma', size=75, weight="bold")
    response.config(font=textFont,bg=background,foreground="green")
    response.pack(pady=100, padx=25, anchor='s')

#====NUMERAL CHARACTERS====#

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

#========================#

#TERMINATE PROGRAM UPON BUTTON CLICK
def Terminate():
    global run
    run = False
    window.destroy()


def Start():

    #WINDOW SETTINGS
    global background
    background = "#002456"
    window.attributes("-fullscreen", True)
    window.configure(background=background)

    #CLOSE [BUTTON]
    terminate = Button(window, text="❌", bg = "red", command=Terminate)
    terminate.config(font=("Courier",20))
    terminate.pack(pady = 25, padx = 25, anchor = 'ne')

    #"Roman Numerals" TEXT
    welcome = Label(window, text = "Roman Numerals")
    welcome.config(font =("Arial Bold", 50),foreground="#FFFFFF",bg=background)
    welcome.pack(pady = 200, padx = 0, anchor = 'c')

    #GUI VARIABLES
    global txt
    txt = ""
    global inputText
    global response
    response = Label()

    #TEXT FIELD
    inputText = Entry(window)
    textFont = font.Font(family='Tahoma', size=75, weight="bold")
    inputText = Entry(window, textvariable = txt, width = 10,font=textFont)
    inputText.place(relx=0.5, rely=0.45, anchor='c')
    inputText.focus_set()

    #START BUTTON
    buttonFont = font.Font(family='Tahoma', size=20, underline=1, weight="bold")
    btn = Button(window, text="Start", command=Input, width=20, font=buttonFont, bg="#408DAA")
    btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    #Loop GUI
    window.mainloop()

#==========MAIN=========#
run = True
while run == True:
    userInput = ""
    window = Tk()
    Start()
#=======================#