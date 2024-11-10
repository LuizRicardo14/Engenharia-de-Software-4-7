import random
import pyautogui as pg
import time
troll = ('Vai Corinthians')
time.sleep(5)
for i in range(100):
    a=random.choice(troll)
    pg.write('Vai Corinthians')
    pg.press('enter')

