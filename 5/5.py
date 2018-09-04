#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-01 23:15:07
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : $Id$

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(300,300,300,200)
w.setWindowTitle('窗口图标')
app.setWindowIcon(QIcon('python.jpg'))
w.show()
sys.exit(app.exec_())
