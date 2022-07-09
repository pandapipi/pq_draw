#coding:utf-8
import os
import sys
from PyQt5.QtGui import QIcon, QPen
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5 import uic, QtWidgets

# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
import matplotlib.pyplot as plt
import numpy as np


class MainWindow:
    u_id = ''
    u_passwd = ''
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("draw_win.ui")

        # 几个QWidgets
        self.ui.figure = plt.figure(facecolor='#FFD7C4') #可选参数,facecolor为背景颜色
        self.ui.canvas = FigureCanvas(self.figure)
        self.ui.button_draw = QPushButton("绘图")
        # 连接事件
        self.ui.button_draw.clicked.connect(self.Draw)

        def Draw(self):
            AgeList = ['10', '21', '12', '14', '25']
            NameList = ['Tom', 'Jon', 'Alice', 'Mike', 'Mary']

            # 将AgeList中的数据转化为int类型
            AgeList = list(map(int, AgeList))

            # 将x,y轴转化为矩阵式
            self.x = np.arange(len(NameList)) + 1
            self.y = np.array(AgeList)

            # tick_label后边跟x轴上的值，（可选选项：color后面跟柱型的颜色，width后边跟柱体的宽度）
            plt.bar(range(len(NameList)), AgeList, tick_label=NameList, color='green', width=0.5)

            # 在柱体上显示数据
            for a, b in zip(self.x, self.y):
                plt.text(a - 1, b, '%d' % b, ha='center', va='bottom')

            # 设置标题
            plt.title("Demo")

            # 画图
            self.ui.canvas.draw()
            # 保存画出来的图片
            plt.savefig('1.jpg')


if __name__ == '__main__':

    app = QApplication([])
    #app.setWindowIcon(QIcon("icon.ico"))
    main_window = MainWindow()
    main_window.ui.show()

    sys.exit(app.exec_())