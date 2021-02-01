# coding=utf-8

from pyWinhook import HookManager
import pyautogui

from time import sleep
from sys import exit

# m = PyMouse()
# k = PyKeyboard()

m = pyautogui

def click(m, x, y):
  real_x = int(scale*x+LeftUp[0])
  real_y = int(scale*y+LeftUp[1])
  m.click(real_x, real_y)

# 部分按键会出现按键后无反应，需要再按一次。目前通过先移动到哪里sleep一下在click可以解决
def MoveAndClick(m, x, y):
  real_x = int(scale*x+LeftUp[0])
  real_y = int(scale*y+LeftUp[1])
  m.moveTo(real_x, real_y)
  sleep(0.02)
  m.click(real_x, real_y)


# import os
# def stop():
#   # x = raw_input()
#   os.system("pause")

def OnKeyboardEvent(event):

  if event.Key == 'Escape':
    exit()

  # pause program
  global stop
  if stop == 1:
    if event.Key == 'Tab':
      stop = 0
    return True

  if event.Key == 'Tab':
    stop = 1
    print('stop....')

  # get position
  if event.Key == 'Oem_3':
    global first
    global LeftUp
    global RightDown
    global scale
    if first == 1:
      first = 0
      x,y = m.position()
      LeftUp = (x,y)
    else:
      x,y = m.position()
      RightDown = (x,y)
      scale = (RightDown[0]-LeftUp[0]) / 1366.0
      first = 1


  if event.Key == 'Space':
    x,y = m.position()
    m.click(x, y)


  # enter
  if event.Key == 'Return':
    click(m, 1274, 710)
  # 4x
  if event.Key == 'Oem_7':
    click(m, 1154, 709)

  # appeal
  if event.Key == 'V':
    click(m, 408, 696)
  if event.Key == 'B':
    click(m, 639, 696)
  if event.Key == 'N':
    click(m, 877, 696)

  # skip
  if event.Key == 'P':
    click(m, 1314, 49)

  # selection
  if event.Key == 'Y':
    click(m, 706, 119)
  if event.Key == 'T':
    click(m, 323, 260)
  if event.Key == 'U':
    click(m, 1038, 260)

  # 有一个bug? 不知道为什么点击裁判需要按键两次
  # 左右
  if event.Key == 'Left':
    MoveAndClick(m, 395, 370)
  if event.Key == 'Right':
    MoveAndClick(m, 1238, 364)

  # 裁判与produce选项
  if event.Key == 'Q':
    MoveAndClick(m, 82, 210)
  if event.Key == 'A':
    MoveAndClick(m, 82, 342)
  if event.Key == 'Z':
    MoveAndClick(m, 82, 509)

  print('Key: %s' %  event.Key)

  # test
  # if event.Key == 'L':
  #   x,y = m.position()
  #   print(x,y)

  return True


if __name__ == '__main__':
  print('Esc: stop program')
  print('Tab: pause program')
  print("press ` on window's Upper left corner and Lower right corner")

  first = 1
  scale = 1
  stop = 0
  # 默认size
  LeftUp = (0, 102)
  RightDown = (1366, 871)

  # create the hook mananger
  hm = HookManager()
  hm.KeyDown = OnKeyboardEvent
  # hook into the mouse and keyboard events
  hm.HookKeyboard()

  # register two callbacks
  # hm.MouseAllButtonsDown = OnMouseEvent
  # hm.HookMouse()

  from pythoncom import PumpMessages
  PumpMessages()