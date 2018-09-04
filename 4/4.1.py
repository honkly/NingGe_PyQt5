#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-01 22:58:07
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : $Id$

import sys
from PyQt5.QtWidgets import QApplication,QWidget
app = QApplication(sys.argv)
# 创建一个窗口
w = QWidget()
# 设置窗口的宽度和高度
w.resize(250,150)
w.move(300,300)
w.setWindowTitle('first')
w.show()
sys.exit(app.exec_())
