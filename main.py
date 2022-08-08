import pyautogui as pg
import time

limit = input('Enter your limit: ')
msg = input('Enter the msg: ')

i=0

time.sleep(3)

while i<int(limit):
    pg.typewrite(msg)
    pg.press('Enter')

i=i+1
