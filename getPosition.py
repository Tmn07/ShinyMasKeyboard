# coding=utf-8
# import pyautogui
from pymouse import PyMouse
import pyWinhook as pyHook

import time

# m = pyautogui
m = PyMouse()

step = 1

def OnKeyboardEvent(event):

  if event.Key == 'Escape':
    exit()

  if event.Key == 'Return':
    x,y = m.position()
    print(x, y)

  # 定位矫正使用
  if event.Key == 'Up':
    x,y = m.position()
    m.move(x, y-step)
  if event.Key == 'Down':
    x,y = m.position()
    m.move(x, y+step)
  if event.Key == 'Left':
    x,y = m.position()
    m.move(x-step, y)
  if event.Key == 'Right':
    x,y = m.position()
    m.move(x+step, y)
    

  # print('MessageName: %s' % event.MessageName)
  # print('Message: %s' % event.Message)
  # print('Time: %s' % event.Time)
  # print('Window: %s' % event.Window)
  # print('WindowName: %s' % event.WindowName)
  # print('Ascii: %s' %  event.Ascii, chr(event.Ascii))
  # print('Key: %s' %  event.Key)
  # print('KeyID: %s' %  event.KeyID)
  # print('ScanCode: %s' %  event.ScanCode)
  # print('Extended: %s' %  event.Extended)
  # print('Injected: %s' %  event.Injected)
  # print('Alt %s' %  event.Alt)
  # print('Transition %s' %  event.Transition)
  # print('---')

  # return True to pass the event to other handlers
  # return False to stop the event from propagating
  return True



if __name__ == '__main__':

  hm = pyHook.HookManager()

  hm.KeyDown = OnKeyboardEvent

  hm.HookKeyboard()

  import pythoncom
  pythoncom.PumpMessages()