from __future__ import print_function
import pyWinhook as pyHook
from pymouse import PyMouse
from pykeyboard import PyKeyboard

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
def OnKeyboardEvent(event):
  if event.Key == 'Tab':
    exit()
  if event.Key == 'Left':
    x,y = m.position()
    m.move(x-move_step, y)
  if event.Key == 'Right':
    x,y = m.position()
    m.move(x+move_step, y)

  if event.Key == 'Up':
    x,y = m.position()
    m.move(x, y-move_step)

  if event.Key == 'Down':
    x,y = m.position()
    m.move(x, y+move_step)
  if event.Key == 'Space':
    x,y = m.position()
    m.click(x, y)

  # 选择fes 临时测试（这个坐标位置emmm）
  # /
  if event.Key == 'Oem_2':
    m.click(1269L, 812L)
  # ;
  if event.Key == 'Oem_1':
    m.click(1054L, 577L)
  # ''
  if event.Key == 'Oem_7':
    m.click(1260L, 576L)

  if event.Key == '1':
    m.click(408L, 770L)
  if event.Key == '2':
    m.click(639L, 798L)
  if event.Key == '3':
    m.click(877L, 799L)  

  # 有一个bug? 不知道为什么点击裁判需要按键两次
  if event.Key == 'Q':
    m.click(82L, 271L)
  if event.Key == 'A':
    m.click(82L, 444L)
  if event.Key == 'Z':
    m.click(82L, 611L) 
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

# create the hook mananger
hm = pyHook.HookManager()
# register two callbacks
# hm.MouseAllButtonsDown = OnMouseEvent
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
# hm.HookMouse()
hm.HookKeyboard()

if __name__ == '__main__':
  import pythoncom
  pythoncom.PumpMessages()