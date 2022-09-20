#William Abbot
#python 3.8.5
import sys
import os
from pynput import keyboard

os.system('color')

current_string = ''
parent_string = input("enter a string: ")
color_str = ''
counter = 0
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class bcolor:
    red = '\033[91m'
    green = '\033[92m'

def read_input(listener):
    listener.start()
    listener.join()

def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()
    
def update_display(string1, string2, color):
    restart_line()
    if color == 'red':
        str = f'{bcolor.red}'+string2+' -------> '+string1
        sys.stdout.write(str)
        sys.stdout.flush()
    else:
        str = f'{bcolor.green}'+string2+' -------> '+string1
        sys.stdout.write(str)
        sys.stdout.flush()
    #time.sleep(1)
    return

def in_parent_string(substring, parent):
    if substring in parent:
        return True
    return False

def on_press(key):
    global current_string
    
    if key == keyboard.Key.esc:
        current_string = 'esc'
        return False  # stop listener
    if key == keyboard.Key.backspace:
        current_string = current_string[:-1]
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['1', '0', 'esc', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        current_string += k
        if(not in_parent_string(current_string, parent_string)):
            color_str ='red'
        else:
            color_str ='green'
        update_display(parent_string, current_string, color_str)
        #return False   stop listener; remove this if want more keys



listener = keyboard.Listener(on_press=on_press)

read_input(listener)

