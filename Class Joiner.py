import pyautogui
import time

pyautogui.press('win', interval = 0.5)
time.sleep(4)

pyautogui.typewrite('chrome' , interval = 0.5)
time.sleep(4)

pyautogui.press('enter' , interval = 0.5)
time.sleep(10)
#longer period so that if it takes time loading!

pyautogui.typewrite("your google meet class link", interval = 0.05)
time.sleep(5)

#Mute Turn off video and join button clickers!

#Mute button
pyautogui.click('coordinates of mute button')
time.sleep(2)

#Turn video off button
pyautogui.click('coordinates of video off button')
time.sleep(3)

#Ask to Join button
pyautogui.click('coordinates of the Join button')
time.sleep(3)

print("""Congratulations you have successfully completed the process of joining the class using the bot!
thank you for using the bot!""")
