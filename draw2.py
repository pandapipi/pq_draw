
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from PyQt5 import uic, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
import array

class graph_votage:
    app = pg.mkQApp()  # 建立app
    win = pg.GraphicsWindow()  # 建立窗口
    win.setWindowTitle(u'pyqtgraph逐点画波形图')
    win.resize(800, 500)  # 小窗口大小

    data = array.array('d')  # 可动态改变数组的大小,double型数组
    historyLength = 100  # 横坐标长度
    p = win.addPlot()  # 把图p加入到窗口中
    p.showGrid(x=True, y=True)  # 把X和Y的表格打开
    p.setRange(xRange=[0, historyLength], yRange=[-1.2, 1.2], padding=0)
    p.setLabel(axis='left', text='y / V')  # 靠左
    p.setLabel(axis='bottom', text='x / point')
    p.setTitle('y = sin(x)')  # 表格的名字
    curve = p.plot()  # 绘制一个图形
    idx = 0
class MainWindow:
    u_id = ''
    u_passwd = ''
    idx = 0
    data = array.array('d')  # 可动态改变数组的大小,double型数组
    historyLength = 100  # 横坐标长度
    curve = None
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.win = None
        self.ui = uic.loadUi("draw_win.ui")
        self.ui.button_draw.clicked.connect(self.plotData())#lambda: self.draw_first(2))
        self.draw_first()

    def draw_first(self,mode = 1):

        self.win = pg.GraphicsWindow()  # 建立窗口
        self.win.setWindowTitle(u'pyqtgraph逐点画波形图')
        self.win.resize(800, 500)  # 小窗口大小
        #group add disable
        # if (self.win == None):
        self.ui.verticalLayout.addWidget(self.win)
        # self.data = array.array('d')  # 可动态改变数组的大小,double型数组
        self.yyRange = [0, 10]
        self.historyLength = 100  # 横坐标长度

        self.p = self.win.addPlot()  # 把图p加入到窗口中
        self.p.showGrid(x=True, y=True)  # 把X和Y的表格打开
        self.p.setRange(xRange=[0, self.historyLength], yRange=[-1.2, 1.2], padding=0)
        self.p.setLabel(axis='left', text='y / Votage')  # 靠左
        self.p.setLabel(axis='bottom', text='x / ms')
        self.p.setTitle('votage:10ms')  # 表格的名字
        if(mode == 1):
            yyRange = [0, 10]
        if (mode == 2):
            yyRange = [0, 80]
        if (mode == 3):
            yyRange = [0, 160]
        if (mode == 4):
            yyRange = [0, 320]
        self.p.setRange(xRange=[0, self.historyLength], yRange = yyRange, padding=0)
        self.curve = self.p.plot()  # 绘制一个图形

        pass
    def Draw(self):
        pass
    def plotData(self):
        #self. idx#内部作用域想改变外部域变量
        self.tmp = np.sin(np.pi / 50 * self.idx)
        print(f"tmp-------{self.data}")
        if len(self.data) < self.historyLength:
            self.data.append(self.tmp)
        else:
            print(self.data[:-1])
            print(self.data[1::])
            self.data[:-1] = self.data[1:] #前移
            self.data[-1] = self.tmp
        self.curve.setData(self.data)
        self.idx += 1
if __name__ == '__main__':

    app = QApplication([])
    main_window = MainWindow()
    main_window.ui.show()
    sys.exit(app.exec_())