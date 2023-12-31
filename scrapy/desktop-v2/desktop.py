# -*- coding: utf-8 -*-
import sys
import time

# Form implementation generated from reading ui file 'desktop.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget
import requests
import wallpaper



# 通过pyuic5工具将我们的ui文件转换成我们的py文件
class Ui_Form(object):
    # 初始化我们的界面
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(363, 238)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 60, 121, 111))
        self.pushButton.setObjectName("pushButton")
        #信号(事件)与槽(函数)
        #发生什么事件 触发什么函数
        #触发什么信号 槽函数就会相应产生反应
        #当前xx控件发生click的信号链接一个槽函数
        self.pushButton.clicked.connect(self.btn_click)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "随机壁纸工具"))
        self.pushButton.setText(_translate("Form", "获取图片"))
    def btn_click(self):
        self.downloadTask=DownLoadWallPaperWork()
        self.downloadTask.start()

        #新建一个子线程
        #调用子线程的start方法 让我们子线程启动起来




#引入一个新的知识点  子线程  QThread  子线程类
#以后我们想要发起网络请求  我们必须得把我们的请求封装到我们子线程中去操作
#重写这个QThread类的Run的方法  Run方法里面用来分身的具体的操作
class  DownLoadWallPaperWork(QThread):
    def __init__(self):
        #先要实例化我们的父对象
        super(DownLoadWallPaperWork,self).__init__()
    def run(self):
        #pass  这里就写我们具体的操作
        # 需求向我们远程发起一个网络请求
        # 安装我们第三方的模块 pip install requests
        print('子线程开始')
        # 发起我们的网络请求
        response = requests.get("https://api.vvhan.com/api/acgimg?type=json")
        # 获取到我们的返回数据
        json = response.json()
        # 从我们所有返回的数据中获取到壁纸的网络地址
        imgurl = json['imgurl']
        # 下载这个壁纸到本地的电脑 我们现在设置一下，壁纸下载的位置在F盘的download文件夹下
        # 发起二次请求  下载图片 将图片保存到本地F://download
        response_img = requests.get(imgurl)
        # 获取到我们的图片的二进制数据
        img_byte = response_img.content
        # 将我们的图片保存到本地
        f = open("~/Downloads/1.jpg", "wb")
        # 将我们的图片的二进制数据写入到我们的文件中
        f.write(img_byte)
        # 关闭我们的文件
        f.close()
        # 将我们桌面设置为我们下载的壁纸
        # 延迟操作 休眠
        time.sleep(3);
        # 设置我们的壁纸
        wallpaper.set_img_as_wallpaper("~/Downloads/1.jpg")
        print('子线程结束')
        print('壁纸处理完毕')

class TestExtend(QThread):

    def run(self):
        super().run()


if __name__ == '__main__':
    # 创建一个应用程序对象
    app=QApplication(sys.argv)
    # 创建一个窗口
    window=QWidget()
    # 创建一个界面对象
    ui=Ui_Form()
    # 向我们的窗口中添加我们的控件
    ui.setupUi(window)
    # 显示我们的窗口
    window.show()
    # 让我们的应用程序进入到我们的消息循环中
    sys.exit(app.exec_())