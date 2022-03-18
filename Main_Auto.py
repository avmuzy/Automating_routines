import pyautogui

pyautogui.alert ("System Up2Date ")
pyautogui.hotkey('ctrl', 'alt', 't')# opens terminal
pyautogui.sleep(3)
pyautogui.write('sudo apt update')
pyautogui.press('enter')
pyautogui.sleep(60)
pyautogui.write('s')
pyautogui.press('enter')
pyautogui.sleep(40)
pyautogui.write('sudo apt upgrade')
pyautogui.press('enter')
pyautogui.write('s')
pyautogui.press('enter')
pyautogui.write('sudo apt autoremove')
pyautogui.press('enter')
pyautogui.write('s')
pyautogui.press('enter')
pyautogui.write('exit')
pyautogui.press('enter')




