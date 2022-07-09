#-*-coding:utf-8-*-
from PyQt5.QtGui import QIcon, QPen
from PyQt5.QtWidgets import QApplication, QFileDialog, QGridLayout
import sys
from PyQt5 import uic, QtWidgets
#import draw_win
import numpy as np
from testplot2pyqt5 import Ui_Dialog

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes0.plot(t, s)
    def plotcos(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

class MainWindow():
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("draw_win.ui")
        self.ui.button_draw.clicked.connect(lambda: self.fig_init(10,20,30))
        #第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=5, height=3, dpi=100)
        #self.F.plotsin()
        # self.plotcos()
        #第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.ui.gridlayout = QGridLayout(self.ui.groupBox)  # 继承容器groupBox
        self.ui.gridlayout.addWidget(self.F,0,1)

        #补充：另创建一个实例绘图并显示
        # self.plotother()
        self.usrplot()
    def fig_init(self,w,h,dp):
        self.F.axes.clear()
        # 实现刷新的条件
        self.F.fig.canvas.draw_idle()
        self.F = MyFigure(width=w, height=h, dpi=dp)
        t = np.arange(0.0, 5.0, 0.01)
        s = np.cos(2 * np.pi * t)
        self.F.axes.plot(t, s)

        self.F.draw()
        #self.F.canvas.flush_envents()
        self.F.fig.canvas.draw_idle()
        print('seted')
    def plotcos(self):
        t = np.arange(0.0, 5.0, 0.01)
        s = np.cos(2 * np.pi * t)
        self.F.axes.plot(t, s)
        self.F.fig.suptitle("cos")
    def usrplot(self):
        # F.axes1 = F.fig.add_subplot(111)
        x = np.arange(0, 5, 0.1)
        self.F.axes.plot(x, np.sin(x), x, np.cos(x))
        self.F.axes.set_title("sincos")
        # self.ui.gridlayout.addWidget(F1, 0, 0)
    def plotother(self):
        F1 = MyFigure(width=5, height=4, dpi=100)
        F1.fig.suptitle("Figuer_4")
        # F1.axes1 = F1.fig.add_subplot(221)
        # x = np.arange(0, 50)
        # y = np.random.rand(50)
        # F1.axes1.hist(y, bins=50)
        # F1.axes1.plot(x, y)
        # F1.axes1.bar(x, y)
        # F1.axes1.set_title("hist")
        # F1.axes2 = F1.fig.add_subplot(222)

        ## 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        # F1.axes2.plot(x, y)
        # F1.axes2.set_title("line")
        # # 散点图
        # F1.axes3 = F1.fig.add_subplot(223)
        # F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
        # F1.axes3.set_title("scatter")
        # 折线图
        F1.axes1 = F1.fig.add_subplot(111)
        x = np.arange(0, 5, 0.1)
        F1.axes1.plot(x, np.sin(x), x, np.cos(x))
        F1.axes1.set_title("sincos")
        self.ui.gridlayout.addWidget(F1, 0, 0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon("icon.ico"))
    main_window = MainWindow()
    main_window.ui.show()

    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
