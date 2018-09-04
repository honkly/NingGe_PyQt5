#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-02 17:22:02
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : $Id$

import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont

app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(300,300,300,200)
w.setWindowTitle('提示框')
QToolTip.setFont(QFont('SansSerif',20))
w.setToolTip('这是一个窗口\n设计者：honkly')
button = QPushButton('Button',w)
button.setToolTip('这是一个按钮、设计者：honkly')
button.resize(button.sizeHint())
button.move(50,50)
w.show()
sys.exit(app.exec_())