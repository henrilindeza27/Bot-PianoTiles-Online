import pyautogui
import time
import keyboard
import win32api, win32con


#Esta função é mais rápida que a do pyautogui!
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed("esc") == False:
    if pyautogui.pixel(518,400)[0] == 0:
        click(518,400)
    if pyautogui.pixel(606,400)[0] == 0:
        click(606,400)
    if pyautogui.pixel(730,400)[0] == 0:
        click(730,400)
    if pyautogui.pixel(819,400)[0] == 0:
        click(819,400)
