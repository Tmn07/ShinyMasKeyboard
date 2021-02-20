# coding=utf-8

import time
import ctypes
import inspect
import threading

from pyWinhook import HookManager
# import pyautogui
from pymouse import PyMouse
# from pykeyboard import PyKeyboard

from sys import exit
# from utils import *
from scripts import *

m = PyMouse()
# m = pyautogui


def click(k, position):
  if not position:
    clickHere()
    # x, y = m.position()
    # m.click(x, y)
  else:
    x = position[0]
    y = position[1]
    real_x = int(k.height*x+k.LeftUp[0])
    real_y = int(k.width*y+k.LeftUp[1])
    m.click(real_x, real_y)


# 部分按键会出现按键后无反应，需要再按一次。目前通过先移动到哪里sleep一下在click可以解决
def MoveAndClick(k, position):
  if not position:
    clickHere()
  else:
    x = position[0]
    y = position[1]
    real_x = int(k.height*x+k.LeftUp[0])
    real_y = int(k.width*y+k.LeftUp[1])
    # m.moveTo(real_x, real_y)
    m.move(real_x, real_y)
    time.sleep(0.02)
    m.click(real_x, real_y)



def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)



class KMaps():
  # def __init__(self, start, height, width):
  def __init__(self, LeftUp, RightDown):

    self.Maps = {}
    self.ScriptKeys = []
    self.EventKeys = []
    self.Keys = []
    self.LeftUp = LeftUp
    self.RightDown = RightDown
    self.updateHW()
    self.stop = 1
    self.onlythread = None


  def updateHW(self):
    self.height = self.RightDown[0]-self.LeftUp[0]
    self.width  = self.RightDown[1]-self.LeftUp[1]
    self.x1 = self.LeftUp[0]
    self.y1 = self.LeftUp[1]

  def run(self, key):
    if key in self.ScriptKeys:
      script = self.Maps[key]
      thread = MyThread(script)
      self.onlythread = thread
      thread.setDaemon(True)
      thread.start()
    elif key in self.EventKeys:
      event = self.Maps[key]
      event()
    else:
      # click(self, self.Maps[key])
      MoveAndClick(self, self.Maps[key])

  def registerKey(self, key, x, y):
    self.Maps[key] = [x, y]
    self.Keys.append(key)

  def location(self, scripts):
    new_scripts = []
    for opt in scripts:
      _int = isinstance(opt,int)
      _list = isinstance(opt,list)
      if _int:
        new_scripts.append(opt)
      if _list:
        x = int(self.x1+opt[0]*self.height)
        y = int(self.y1+opt[1]*self.width)
        new_scripts.append([x, y])
    return new_scripts

  def registerScript(self, key, script):
    self.Maps[key] = script
    self.Keys.append(key)
    self.ScriptKeys.append(key)

  def registerEvent(self, key, function):
    self.Maps[key] = function
    self.Keys.append(key)
    self.EventKeys.append(key)


class MyScript(object):
  def __init__(self, script_name, script, times):
    super(MyScript, self).__init__()
    self.script_name = script_name
    self.script = script
    self.times = times

  def location(self, k):
    new_script = k.location(self.script)
    self.script = new_script
    


class MyThread(threading.Thread):
    def __init__(self, myscript):
        super(MyThread, self).__init__(name = myscript.script_name)
        self.name = myscript.script_name
        self.times = myscript.times
        self.scripts = myscript.script

    # 重写run()方法
    def run(self):
        print("%s正在运行中......" % self.name)
        if self.times == 0:
          while 1:
            self.runScript()
        else:
          for i in range(self.times):
            self.runScript()
          print("%s运行结束" % self.name)

    def runScript(self):
      # todo: 如何只进行一次的脚本解析.
      for opt in self.scripts:
        _t = isinstance(opt,int) or isinstance(opt,float)
        _list = isinstance(opt,list)
        if _t:
          time.sleep(opt)
        if _list:
          # todo: 解耦..
          # click(k, opt)
          # print(opt)
          MoveAndClick(k, opt)




def pauseProgram():
  pass

def exitProgram():
  exit()

def setWindow():
  global first
  if first == 1:
    first = 0
    x,y = m.position()
    k.LeftUp = (x,y)
    print('接下来请移动至右下角点击`进行定位')
  else:
    x,y = m.position()
    k.RightDown = (x,y)
    k.updateHW()
    first = 1
    print('窗口定位完毕')

def clickHere():
  x, y = m.position()
  m.click(x, y)
  # print(x, y)

def stopScript():
  if k.onlythread and k.onlythread.is_alive():
    stop_thread(k.onlythread)
    print('自动脚本停止')



def OnKeyboardEvent(event):

  if event.Key == 'Escape':
    exit()

  global pause
  if pause == 1:
    if event.Key == 'Tab':
      pause = 0
    return True
  if event.Key == 'Tab':
    pause = 1
    print('程序已暂停')

  global k

  for key in k.Maps:
    if event.Key == key:
      k.run(key)

  return True




print('Esc: stop program')
print('Tab: pause program')
print("press ` on window's Upper left corner and Lower right corner")

first = 1
pause = 0

# todo: 读取上一次定位的结果？
# 默认size 
LeftUp = (0, 87)
RightDown = (1368, 856)

k = KMaps(LeftUp, RightDown)

# 坐标比例参考excel内记录
k.registerKey('Return', 0.926873857, 0.897402597)
k.registerKey('Oem_7', 0.851919561, 0.918181818)
k.registerKey('P', 0.952833638, 0.078571429)
k.registerKey('T', 0.179159049, 0.342207792)
k.registerKey('Y', 0.49360146,  0.17987013)
k.registerKey('U', 0.804387569, 0.342207792)
k.registerKey('V', 0.31809872 , 0.907142857)
k.registerKey('B', 0.500914077, 0.907142857)
k.registerKey('N', 0.676416819, 0.907142857)
k.registerKey('Q', 0.073126143, 0.264285714)
k.registerKey('A', 0.073126143, 0.491558442)
k.registerKey('Z', 0.073126143, 0.725324675)
k.registerKey('Left', 0.285191956, 0.488311688)
k.registerKey('Right', 0.910420475, 0.488311688)
k.registerKey('X', 0.311517367, 0.872077922)
k.registerKey('H', 0.578062157, 0.601948052)


myScript_8 = MyScript('八连休', Script_8, 0)
k.registerScript('8', myScript_8)
myScript_af = MyScript('autofes', Script_af, 5)
k.registerScript('5', myScript_af)
# todo:装载的脚本说明

k.registerEvent('Space', clickHere)
k.registerEvent('0', stopScript)
k.registerEvent('Oem_3', setWindow)
# todo: 暂停和关闭的优先级要提高..
# k.registerEvent('Escape', exitProgram)
# k.registerEvent('Tab', pauseProgram)


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