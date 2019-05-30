# pyqtDownloader
---
## 概述
#### pyqt实现的一个多线/进/协程的桌面版下载器
---
## 开发环境
### 工具
#### 1. pycharm
#### 2. Qt Creator - 用于设计界面得到到pyqt_downloader.ui文件
### 主要用到的第三方python模块：
#### 1. PyQt5
#### 2. requests 
---
### 关于项目一些说明：
#### 1. 界面的设计使用QtCreator设计得到并生成ui文件
#### 2. pyqt并不能直接使用qt的ui文件, 须使用pyuic5工具转换成py文件，命令为：
#### >>>pyuic5 pyqt_downloader.ui -o pyqt_downloader_ui.py
