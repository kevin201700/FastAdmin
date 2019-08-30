#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('如果程序运行错误，请检查是否安装有下列Module：PyQt5 Tkinter socket')

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import tkinter
import socket
import tkinter.messagebox


def aboutshow():
    mainwindow = tkinter.Tk()
    mainwindow.title("关于 (About) - FastAdmin")
    width = 480
    height = 360
    screenwidth = mainwindow.winfo_screenwidth()
    screenheight = mainwindow.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
    mainwindow.geometry(alignstr)
    AboutMessage = tkinter.Label(mainwindow, text="关于")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="Fastadmin 2019.0.01 分支：dev")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="项目地址：https://gthub.com/kevin201700/FastAdmin/tree/dev/")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="Tkinter python.org")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="PyQt5 qt.io")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="GitHub github.com")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="IntelliJ Idea jetbrains.com")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="socket python.org")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="Python3 python.org")
    AboutMessage.pack()
    AboutMessage = tkinter.Label(mainwindow, text="WordPress wordpress.org")
    AboutMessage.pack()
    def Namesshow():
        tkinter.messagebox.showinfo('开发者名单', '李铭昊(Kevin201700)\n')
    Name = tkinter.Button(mainwindow, text="开发者名单", command = Namesshow)
    Name.pack()
    mainwindow.mainloop()


def login():
    mainwindow = tkinter.Tk()
    mainwindow.title("登录到服务器 (Login to the Server) - FastAdmin")
    width = 480
    height = 360
    screenwidth = mainwindow.winfo_screenwidth()
    screenheight = mainwindow.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
    mainwindow.geometry(alignstr)
    Servernamedp = tkinter.Label(mainwindow, text="服务器地址 (Server Address)")
    Servernamedp.pack()#side=left)
    global Servername
    Servername = tkinter.Entry(mainwindow, bd=5)
    Servername.pack()#side=left)
    Usernamedp = tkinter.Label(mainwindow, text="用户名 (Username)")
    Usernamedp.pack()#side=left)
    global Username
    Username = tkinter.Entry(mainwindow, bd=5)
    Username.pack()#side=left)
    Passworddp = tkinter.Label(mainwindow, text='密码 (Password)')
    Passworddp.pack()
    global Password
    Password = tkinter.Entry(mainwindow)
    Password['show'] = '•'
    Password.pack()
    TPassworddp = tkinter.Label(mainwindow, text="预共享密钥 (Pre-shared key)")
    TPassworddp.pack()#side=left)
    global TPassword
    TPassword = tkinter.Entry(mainwindow)
    TPassword['show'] = '•'
    TPassword.pack()
    global isSSL
    isSSL = False
    def click_isSSL():
        global isSSL
        isSSL = not isSSL
    isSSLB = tkinter.Checkbutton(mainwindow,text='使用SSL/TLS安全登录 (Use the SSL/TLS to safe login)',command=click_isSSL)
    isSSLB.pack()
    Over = tkinter.Button(mainwindow, text ="登录 (Login)")#, command = helloCallBack)
    Over.pack()
    mainwindow.mainloop()


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('快速连接 - FastCS')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #ex = Example()
    #sys.exit(app.exec_())
    aboutshow()
    login()
    client = socket.socket()
    client.connect(Servername.get(), "16201")
    client.send(TPassword.get())
    tf = client.recv(1024)
    if tf == "False":exit()
    client.send(Username.get())
    tf = client.recv(1024)
    if tf == "False":exit()
    client.send(Password.get())
    tf = client.recv(1024)
    if tf == "False":exit()
    client.send(TPassword.get())
    tf = client.recv(1024)
    if tf == "False":exit()