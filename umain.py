import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QFileDialog, QGridLayout
import sys
from PyQt5 import uic, QtWidgets
#import draw_win
import numpy as np
from testplot2pyqt5 import Ui_Dialog

class MainWindow():
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("draw_win.ui")
        self.plot = pg.PlotWidget(enableAutoRange=True)
        self.ui.verticalLayout.addWidget(self.plot)
        self.curve = self.plot.plot()

        self.ui.button_draw.clicked.connect(self.draw_pic)#lambda: self.fig_init(10,20,30))
    def draw_pic(self):
        self.data[:-1] = self.data[1:]  # shift data in the array one sample left
        self.data[-1] = np.random.normal()
        # self.data[-1] = b[0]

        self.ptr1 += 1
        self.curve.setData(self.data)
        self.curve.setPos(self.ptr1, 0)
        #self.curve.setData(data)
        #self.curve.clear()