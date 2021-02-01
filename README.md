# shinymas键盘助手

想起来可以方便Pcup连点，减少鼠标移动花的时间，所以就又改动了一下。

图示：

![]( ./pic/sk1.jpg )

![]( ./pic/sk2.jpg )

## 使用说明

运行程序test.py，默认窗口大小是我电脑的全屏尺寸

定位：

运行程序后 鼠标移动到游戏窗口左上角按下 \` 按键 ，再移动到右下角 按下 \`（可多次定位，重新点击左上角和右下角即可）

按键说明：

T/Y/U：个人剧情，morning，约束上方三个选项

Q/A/Z：选择vo/da/vi裁判或lesson/工作/试镜

V/B/N：选择下面三把刀

Enter：回忆炸弹 / 一系列确定键

Space：点击当前位置，主要用于试镜中点条

P：skip

'：四倍速按键

Tab：暂停程序

Esc：结束程序

操作技巧：

各类事件过场通过长按进行连点，会快速过渡

休息与技能设定相关的按键，注意切换鼠标等设备

小心误操作

## 安装说明

```
pip install pyautogui pyWinhook
```

或者使用这里打包好的应用程序 [release页面](https://github.com/qq519043202/ShinyMasKeyboard/releases)

## 相关第三方库

鼠标(/键盘)操作：[pyautogui](https://github.com/asweigart/pyautogui)

键盘(/鼠标)监听：[pyWinhook](https://github.com/Tungsteno74/pyWinhook) [Demo](https://github.com/Tungsteno74/pyWinhook/blob/master/pyWinhook/example.py)

旧，已经停止维护的鼠标(/键盘)操作库：[PyUserInput](https://github.com/PyUserInput/PyUserInput)

## todo
- [x] 键盘监听
- [x] 鼠标操作
- [x] 打包发布
- [ ] 跨平台(Linux, MacOS?)

## 其他

shinykey.xlsx 为我全屏时各按键的坐标

keepbgm.txt 是参考插件代码，不通过插件实现离开游戏画面保持音乐播放的方式（没地方放就放这里了