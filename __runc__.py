#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import tkinter
import socket


def login():
    mainwindow = tkinter.Tk()
    mainwindow.title("登录到服务器 (Login to Server) - FastCS")
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