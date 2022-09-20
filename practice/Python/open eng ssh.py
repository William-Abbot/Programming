import time, subprocess, pyautogui


passW = input("enter password to type in automatically<disable feature>:  ")

timeLeft = 3
while timeLeft > 0: 
     print(str(timeLeft) + "...\n")
     time.sleep(1) 
     timeLeft = timeLeft - 1

subprocess.Popen(['E:\\Program Files\\PuTTY\\putty.exe', '-ssh', 'wva0001@gate.eng.auburn.edu'])

#for testing:
#subprocess.Popen('C:\\Windows\\System32\\notepad.exe')


if(passW != ''):
    time.sleep(5)
    pyautogui.typewrite(passW)
    pyautogui.typewrite('\n')
    time.sleep(3)
    pyautogui.typewrite('\n')
    time.sleep(3)
    pyautogui.typewrite(passW)
    pyautogui.typewrite('\n')
    time.sleep(1)
    del passW
