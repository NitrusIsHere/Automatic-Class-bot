import pyautogui
from time import sleep
pyautogui.PAUSE = 1
sleep(5)

x,y=pyautogui.position()
print(x,y)

