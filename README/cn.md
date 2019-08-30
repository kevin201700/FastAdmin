# FastAdmin

[TOC]

一个使用Python3开发的服务器管理软件。

 正在开发，欢迎大家一起开发。

建议使用Windows Server的开发者优化Windows版(放置在__run__WindowsServer.py文件中，函数放置在Module_WindowsServer文件夹中)；

使用Debian、Ubuntu、Deepin的开发者优化Debian、Ubuntu、Deepin版(放置在__run__.py文件中，函数放置在Module文件夹中)；

使用Red Hat Enterprise Linux、CentOS的开发者优化Red Hat Enterprise Linux版(放置在__run__RH.py文件中，函数放置在Module_RH文件夹中)。



# 功能

![设计图]()

远程Shell(我们设计，不用telnet或SSH)

Apache/Ngnix管理(我的电脑不能测试，因为我把Apache和Nginx的配置文件搞砸了)

文件管理(我们设计，不用带FTP字眼的、Webdav和Samba)

frp内网穿透管理(是可视化操作，不是直接改配置)

[frp]: https://github.com/fatedier/frp

FastAdmin管理 



## 客户端

(还未完成)

### 登录

#### 依赖

Tkinter

socket

#### 测试平台（我的电脑）

Deepin 15.11

内核 x86_64 Linux 4.15.0-30deepin-generic

Python 3.5.3 (default, Sep 27 2018, 17:25:39)  [GCC 6.3.0 20170516] on linux

非root

IDE IntelliJ IDEA

> IntelliJ IDEA 2019.1.4 (Ultimate Edition)
> Build #IU-191.8026.42, built on July 30, 2019
> Licensed to jetbrains js
> Subscription is active until November 27, 2019
> JRE: 1.8.0_212-release-1586-b4 amd64
> JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
> Linux 4.15.0-30deepin-generic



## 服务器

(还未开发)

