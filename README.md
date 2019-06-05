# shinymas键盘助手

目的为了使用键盘来游玩shinymas（指P卡，打fes）

原本想做成浏览器插件（但是好像失败了。现在用python调用os api来进行

目前代码只是随便写的用作接口测试

## 相关第三方库

鼠标(/键盘)操作：[PyUserInput](https://github.com/PyUserInput/PyUserInput)

键盘(/鼠标)监听：[pyWinhook](https://github.com/Tungsteno74/pyWinhook) [Demo](https://github.com/Tungsteno74/pyWinhook/blob/master/pyWinhook/example.py)

## todo
- [x] 键盘监听
- [x] 鼠标操作
- [ ] 界面定位，识别
- [ ] 控制逻辑
- [ ] 跨平台(Linux, MacOS?)
- [ ] 打包发布?