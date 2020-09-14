import pyautogui as pya
import time, sys

def setPosition():
    counter = 9
    print("Place your cursor where you would like to have the mouse click. Cursor position will be taken in 8 seconds:" )
    for i in range(1, counter):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d}".format(i)) 
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n")
    cursorPosition = pya.position()
    return cursorPosition

position = setPosition()
numOfClicks = int(input("Enter the number of times you would like this script to click: "))
secInterval = float(input("Enter how often(in seconds) you would like this script to click: "))
pya.click(position,clicks=numOfClicks,interval=secInterval,button="left")