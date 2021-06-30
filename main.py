import pyautogui 
from time import sleep

pyautogui.press("win")
sleep(.1)
pyautogui.typewrite("defaul")
pyautogui.press("enter")
sleep(1)
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.hotkey('alt', 'f4')
quit()

