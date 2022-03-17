import pyautogui
import time
pyautogui.alert ("System Up2Date ")
pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(3)
pyautogui.write('sudo apt update')
pyautogui.press('enter')
time.sleep(60)
pyautogui.write('s')
pyautogui.press('enter')
time.sleep(40)
pyautogui.write('sudo apt upgrade')
pyautogui.press('enter')
pyautogui.write('s')
pyautogui.press('enter')





