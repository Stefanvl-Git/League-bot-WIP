from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


time.sleep(5)
def main():
    def click(x,y) :
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    def click2(x,y) :
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

    def startgame():
        main = pyautogui.locateCenterOnScreen("play.png", grayscale=False)
        pyautogui.locateOnScreen('play.png', confidence=0.8)
        time.sleep(1)
        pyautogui.moveTo(main)
        time.sleep(1)
        pyautogui.click(main)
        print("making lobby..")
        time.sleep(2)

        gamemode = pyautogui.locateCenterOnScreen("gamemode.png", grayscale=False)
        time.sleep(1)
        pyautogui.locateOnScreen('gamemode.png', confidence=0.8)
        time.sleep(1)
        pyautogui.moveTo(gamemode)
        time.sleep(1)
        pyautogui.click(gamemode)
        print("Selecting gamemode..")
        time.sleep(0.5)

        practice = pyautogui.locateCenterOnScreen("prac.png", grayscale=False)
        pyautogui.locateOnScreen('prac.png', confidence=0.8)
        time.sleep(1)
        pyautogui.moveTo(practice)
        time.sleep(1)
        pyautogui.click(practice)
        print("Selecting gamemode..")
        time.sleep(2)

        confirm = pyautogui.locateCenterOnScreen("confirm.png", grayscale=False)
        pyautogui.locateOnScreen('confirm.png', confidence=0.8)
        time.sleep(1)
        pyautogui.moveTo(confirm)
        time.sleep(1)
        pyautogui.click(confirm)
        print("Starting Queue..")
        time.sleep(2)

        start = pyautogui.locateCenterOnScreen("start.png", grayscale=False)
        pyautogui.locateOnScreen('start.png', confidence=0.8)
        time.sleep(1)
        pyautogui.moveTo(start)
        time.sleep(1)
        pyautogui.click(start)
        print("Starting champ select..")
        time.sleep(2)

        lux = pyautogui.locateCenterOnScreen("lux.png", grayscale=False)
        pyautogui.locateOnScreen('lux.png', confidence=0.8)
        time.sleep(1)
        pyautogui.moveTo(lux)
        time.sleep(1)
        pyautogui.click(lux)
        print("Picking champ..")
        time.sleep(2)

        lockin = pyautogui.locateCenterOnScreen("lockin.png", grayscale=False)
        pyautogui.locateOnScreen('lockin.png', confidence=0.8)
        time.sleep(1)
        pyautogui.moveTo(lockin)
        time.sleep(1)
        pyautogui.click(lockin)
        print("Locking in..")
        time.sleep(2)

    def ingame():
        if pyautogui.locateOnScreen('minion.png', confidence=.8):
            minion = pyautogui.locateCenterOnScreen("minion.png", confidence=.8, grayscale=False)
            pyautogui.click(minion)
            time.sleep(1)
            print("Attack Champion...")
        else:
            click(2000,450)
            time.sleep(1)

    startgame()

    while 2:
        if pyautogui.locateOnScreen('end.png', confidence=.8):
            main()
            break
        else:
            click(2000,450)
            time.sleep(1)

while 3: 
    if pyautogui.locateCenterOnScreen("client.png", confidence=0.8):
        print("Starting script...")
        main()
        break
    else:
        time.sleep(2)