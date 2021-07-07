import cv2
import numpy as np
import mss
import time
import pyautogui
from rich import print
import keyboard


base = cv2.imread('base.png', cv2.IMREAD_UNCHANGED)
find = cv2.imread('1.png', cv2.IMREAD_UNCHANGED)
find2 = cv2.imread('2.png', cv2.IMREAD_UNCHANGED)
find3 = cv2.imread('3.png', cv2.IMREAD_UNCHANGED)
find4 = cv2.imread('dino_dead.png', cv2.IMREAD_UNCHANGED)

find5 = cv2.imread('enemi_jump.png', cv2.IMREAD_UNCHANGED)

sct = mss.mss()
dimensions_left = {
        'left': 640,
        'top': 436,
        'width': 150,
        'height': 250
    }

def jump(timed):
    pyautogui.keyDown('space')
    time.sleep(timed)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')
    time.sleep(0.05)
    pyautogui.keyUp('down')

print("[bold yellow]dinosaur t-rex game bot ai par DoctorWhoFr#0777 [/bold yellow]")

while True:
    _set = np.array(sct.grab(dimensions_left ))
    result = cv2.matchTemplate(_set, find, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(_set, find2, cv2.TM_CCOEFF_NORMED)
    result3 = cv2.matchTemplate(_set, find3, cv2.TM_CCOEFF_NORMED)
    result4 = cv2.matchTemplate(_set, find4, cv2.TM_CCOEFF_NORMED)
    result5 = cv2.matchTemplate(_set, find5, cv2.TM_CCOEFF_NORMED)


    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    _, max_val2, _, max_loc2 = cv2.minMaxLoc(result2)
    _, max_val3, _, max_loc3 = cv2.minMaxLoc(result3)
    _, max_val4, _, max_loc4 = cv2.minMaxLoc(result4)
    _, max_val5, _, max_loc5 = cv2.minMaxLoc(result5)



    if(max_val > 0.50):
        jump(0.02)
    elif(max_val2 > 0.50):
        jump(0.02)
    elif(max_val3 > 0.50):
        jump(0.2)
    elif(max_val5 > 0.50):
        jump(0.4)
        print(max_loc5)


    if keyboard.is_pressed('q'):
        break
    
    

# while True:
#     cv2.imshow('Farm', base)
#     cv2.waitKey()

#     cv2.imshow('Needle', find)
#     cv2.waitKey()

#     result = cv2.matchTemplate(base, find, cv2.TM_CCOEFF_NORMED)

#     cv2.imshow('Result', result)
#     cv2.waitKey()

#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#     w = find.shape[0]
#     h = find.shape[1]

#     cv2.rectangle(base, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
