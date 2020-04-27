# coding=utf-8
from __future__ import print_function
import pyWinhook as pyHook
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m = PyMouse()
k = PyKeyboard()


def OnMouseEvent(event):
  print('MessageName: %s' % event.MessageName)
  print('Message: %s' % event.Message)
  print('Time: %s' % event.Time)
  print('Window: %s' % event.Window)
  print('WindowName: %s' % event.WindowName)
  print('Position: (%d, %d)' % event.Position)
  print('Wheel: %s' % event.Wheel)
  print('Injected: %s' % event.Injected)
  print('---')

  # return True to pass the event to other handlers
  # return False to stop the event from propagating
  return True

move_step = 70

first = 1
scale = 1
LeftUp = (0, 102)
RightDown = (1366, 871)

def click(m, x, y):
  real_x = int(scale*x+LeftUp[0])
  real_y = int(scale*y+LeftUp[1])
  m.click(real_x, real_y)

# 部分按键会出现按键后无反应，需要再按一次。目前通过先移动到哪里sleep一下在click可以解决
def MoveAndClick(m, x, y):
  real_x = int(scale*x+LeftUp[0])
  real_y = int(scale*y+LeftUp[1])
  m.move(real_x, real_y)
  time.sleep(0.02)
  m.click(real_x, real_y)


def OnKeyboardEvent(event):

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

  if event.Key == 'Tab':
    exit()

  if event.Key == 'L':
    x,y = m.position()
    print(x,y)
    # print(scale)
    # print(LeftUp  , RightDown)

  if event.Key == 'Left':
    MoveAndClick(m, 395, 370)
    # move(m, 395, 370)
    # time.sleep(0.05)
    # click(m, 395, 370)
    # m.click(int(scale*395+LeftUp[0]), int(scale*370+LeftUp[1]))
  if event.Key == 'Right':
    MoveAndClick(m, 1238, 364)
    # move(m, 1238, 364)  
    # time.sleep(0.05)
    # click(m, 1238, 364)
    # m.click(int(scale*1238+LeftUp[0]), int(scale*364+LeftUp[1]))



  if event.Key == 'Return':
    click(m, 1274, 710)
  if event.Key == 'Oem_7':
    click(m, 1154, 709)

  if event.Key == 'Space':
    x,y = m.position()
    m.click(x, y)


  if event.Key == 'V':
    click(m, 408, 696)
  if event.Key == 'B':
    click(m, 639, 696)
  if event.Key == 'N':
    click(m, 877, 696)

  # 有一个bug? 不知道为什么点击裁判需要按键两次
  if event.Key == 'Q':
    MoveAndClick(m, 82, 210)
    # time.sleep(0.05)
    # click(m, 82, 250)

  if event.Key == 'A':
    MoveAndClick(m, 82, 342)
    # time.sleep(0.05)
    # click(m, 82, 342)

  if event.Key == 'Z':
    MoveAndClick(m, 82, 509)
    # time.sleep(0.05)
    # click(m, 82, 509)

  if event.Key == 'P':
    click(m, 1314, 49)

    # 323 362
    # 1038 380
  if event.Key == 'Y':
    click(m, 706, 119)
  if event.Key == 'T':
    click(m, 323, 260)
  if event.Key == 'U':
    click(m, 1038, 260)

  print('MessageName: %s' % event.MessageName)
  print('Message: %s' % event.Message)
  print('Time: %s' % event.Time)
  print('Window: %s' % event.Window)
  print('WindowName: %s' % event.WindowName)
  print('Ascii: %s' %  event.Ascii, chr(event.Ascii))
  print('Key: %s' %  event.Key)
  print('KeyID: %s' %  event.KeyID)
  print('ScanCode: %s' %  event.ScanCode)
  print('Extended: %s' %  event.Extended)
  print('Injected: %s' %  event.Injected)
  print('Alt %s' %  event.Alt)
  print('Transition %s' %  event.Transition)
  print('---')

  # return True to pass the event to other handlers
  # return False to stop the event from propagating
  return True



if __name__ == '__main__':
  print('you need to address your window')
  LeftUp = (0, 102)
  RightDown = (1366, 871)

  # create the hook mananger
  hm = pyHook.HookManager()
  # register two callbacks
  # hm.MouseAllButtonsDown = OnMouseEvent
  hm.KeyDown = OnKeyboardEvent
  # hook into the mouse and keyboard events
  # hm.HookMouse()
  hm.HookKeyboard()

  import pythoncom
  pythoncom.PumpMessages()