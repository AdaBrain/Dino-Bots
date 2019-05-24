import pyautogui

prv_pos = 0
cur_pos = 0

while True:
    cur_pos = pyautogui.position()
    if cur_pos != prv_pos:
        prv_pos = cur_pos
        print(cur_pos)
