import pyautogui 
from time import sleep

pyautogui.press("win")
sleep(.2)
pyautogui.typewrite("default")
sleep(.1)
pyautogui.press("enter")
sleep(1.5)
if pyautogui.locateCenterOnScreen('mozilla.png'):
    x, y = pyautogui.locateCenterOnScreen('mozilla.png')
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    sleep(.7)
    x, y = pyautogui.locateCenterOnScreen('brave.png')
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    pyautogui.hotkey('alt', 'f4')
    print("Finished")
    quit()
else:
    quit()


