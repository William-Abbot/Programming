#!python3

import subprocess, pyautogui, time

subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

time.sleep(1)

pyautogui.typewrite("yo")
for i in range(4):
    pyautogui.typewrite('\n')
time.sleep(1)
pyautogui.typewrite("I'm stupid")
