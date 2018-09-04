#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-04 23:05:20
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : $Id$

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication

app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(300,300,300,200)
w.setWindowTitle('关闭窗口')
button = QPushButton('关闭窗口',w)
button.clicked.connect(QCoreApplication.instance().quit)
button.move(50,50)
w.show()
sys.exit(app.exec_())
