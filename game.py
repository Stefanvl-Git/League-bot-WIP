from pyautogui import *
import pyautogui
import pydirectinput
import time
import keyboard
import random
import win32api, win32con

def click(x,y) :
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while 1:
    if pyautogui.locateOnScreen('minion.png', confidence=.8):
        minion = pyautogui.locateCenterOnScreen("minion.png", confidence=.8, grayscale=False)
        pyautogui.click(minion)
        time.sleep(1)
        print("Attack Champion...")
       
    else:
        click(2000,450)
        time.sleep(1)
