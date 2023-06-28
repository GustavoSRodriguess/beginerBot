from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('stickman.png', region=(100,250,250,500), grayscale=True, confidence=0.8) != None:
        print("consigo ver")
        time.sleep(0.5)
    else:
        print("nao consigo ver")
        time.sleep(0.5)




        
        
