#Auto clicker program
import pyautogui as gui
import time

but=input("What button? (right/left): ")
intt=int(input("How much cps: "))
time.sleep(5)

while True:
    gui.click(clicks=intt,button=but)

