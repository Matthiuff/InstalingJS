import pyautogui
import pyperclip
import time
txt = open('code.txt', 'r').read()
pyperclip.copy(txt)

time.sleep(2)
pyautogui.hotkey('ctrl','shift','j')
time.sleep(2)
code = pyperclip.paste()
pyautogui.typewrite(code)
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)
while True:
    pyautogui.press('enter')

















