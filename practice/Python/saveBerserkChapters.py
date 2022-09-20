import os,pyautogui,time


print("this is a bot that visits readberserk.com and saves all berserk chapters from a given starting point as pdf files so that you can read them without internet")
print("---------------------------------------")
chapter = input("At which chapter do you want the bot to start?: ")
#chapter = f"{int(chapter):03}"
chapterInt = int(chapter)
chapter = chapter.zfill(3)
os.system('cmd /c "explorer https://readberserk.com/chapter/berserk-chapter-{}"'.format(chapter))
time.sleep(1)

while chapterInt < 365:
    time.sleep(3)
    
    #this next part only works with opera browser because of the 'save as pdf' option
    pyautogui.moveTo(1330,400)
    pyautogui.click(button='right')
    pyautogui.moveTo(1400,646)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('enter')


    pyautogui.moveTo(1330, 450)
    pyautogui.click()
    print(chapterInt)
    chapterInt+=1
