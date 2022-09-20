import os

os.system('color')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.FAIL}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
input()

x = ' yo '

import sys
import time

def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

sys.stdout.write(x)
sys.stdout.flush()
time.sleep(2) # wait 2 seconds...
restart_line()
sys.stdout.write('other different data')
sys.stdout.flush()
restart_line()

input()

from colorama import Fore
from colorama import Style
print()
print(f'this is {Fore.GREEN}color{Style.RESET_ALL}!')

input()

fullstring = "StackAbuse"
substring = "tack"

if (substring in fullstring):
    print("Found!")
else:
    print("Not found!")

print()
input()




from pynput import keyboard

def on_press(key):
    #print('{0} pressed'.format(
        #key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    check_key(key.char)


def check_key(key):
    if key in ['0', '1']: 
        print('YES')

# Collect events until released
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
keyboard.Listener.stop(listener)
listener.start()
listener.join()
print(listener)
input()
