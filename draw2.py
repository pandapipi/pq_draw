
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from PyQt5 import uic, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
import array


class MainWindow:
    u_id = ''
    u_passwd = ''
    idx = 0
    data = array.array('d')  # 可动态改变数组的大小,double型数组
    historyLength = 100  # 横坐标长度
    curve = pg.graphicsItems.PlotDataItem.PlotDataItem()
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.win = None
        self.ui = uic.loadUi("draw_win.ui")
        self.ui.button_draw.clicked.connect(lambda: self.draw_first(2))
        self.draw_first()

        self.button_size_x = 500
        self.button_size_y = 100
        self.button_size_w = 100
        self.button_size_h = 20

        self.pb1 = QtWidgets.QPushButton(self.win)
        self.pb1.setGeometry(QtCore.QRect( self.button_size_x, self.button_size_y, self.button_size_w, self.button_size_h ))
        self.pb1.setObjectName("pb_Syssetting")
        self.pb1.setText('系统设置')

        self.pb2 = QtWidgets.QPushButton(self.win)
        self.pb2.setGeometry(QtCore.QRect( self.button_size_x, self.button_size_y+30*1,  self.button_size_w, self.button_size_h ))
        self.pb2.setObjectName("pb_Coorsetting")
        self.pb2.setText('坐标设置')

        self.pb3 = QtWidgets.QPushButton(self.win)
        self.pb3.setGeometry(QtCore.QRect( self.button_size_x, self.button_size_y+30*2,  self.button_size_w, self.button_size_h ))
        self.pb3.setObjectName("pb_Machinesetting")
        self.pb3.setText('加工条件')

        self.pb4 = QtWidgets.QPushButton(self.win)
        self.pb4.setGeometry(QtCore.QRect( self.button_size_x, self.button_size_y+30*3,  self.button_size_w, self.button_size_h ))
        self.pb4.setObjectName("pb_PSsetting")
        self.pb4.setText('定位设置')

        self.pb5 = QtWidgets.QPushButton(self.win)
        self.pb5.setGeometry(QtCore.QRect( self.button_size_x, self.button_size_y+30*4,  self.button_size_w, self.button_size_h ))
        self.pb5.setObjectName("pb_Move")
        self.pb5.setText('移动')
        self.pb6 = QtWidgets.QPushButton(self.win)
        self.pb6.setGeometry(QtCore.QRect( self.button_size_x, self.button_size_y+30*5,  self.button_size_w, self.button_size_h ))
        self.pb6.setObjectName("pb_Sample")
        self.pb6.setText('采信设置')

    def draw_first(self,mode = 1):
        pg.setConfigOptions(leftButtonPan=False)
        # 修改背景颜色
        pg.setConfigOption('background', '#0FFFFF')
        pg.setConfigOption('foreground', 'k')
        self.win = pg.GraphicsWindow(size=(100,50))  # 建立窗口
        self.win.setWindowTitle(u'pyqtgraph逐点画波形图')
        #self.win.resize(100, 200)  # 小窗口大小
        self.win.clear()
        #group add disable

        # if (self.win == None):
        layitem = self.ui.verticalLayout.itemAt(0)
        if layitem:
            self.ui.verticalLayout.removeItem(layitem)
            if layitem.widget():
                layitem.widget().deleteLater()
        self.ui.verticalLayout.addWidget(self.win)

        # self.data = array.array('d')  # 可动态改变数组的大小,double型数组
        self.yyRange = [0, 10]
        self.historyLength = 40  # 横坐标长度

        self.p = self.win.addPlot()  # 把图p加入到窗口中
        self.p.showGrid(x=True, y=True)  # 把X和Y的表格打开
        # self.p.setRange(xRange=[0, self.historyLength], yRange=[-1.2, 1.2], padding=0)
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
            # 1

        self.p.setRange(xRange=[0, self.historyLength], yRange = yyRange, padding=0)
        self.curve = self.p.plot(pen='r', symbol='o')  # 绘制一个图形
        # print(type(self.curve))

        pass
    def Draw(self):
        pass
    def plotData(self):
        #self. idx#内部作用域想改变外部域变量
        # self.tmp = np.sin(np.pi / 50 * self.idx)
        # print(f"tmp-------{self.data}")
        if len(self.data) < self.historyLength:
            self.data.append(self.tmp)
        else:
            # print(self.data[:-1])
            # print(self.data[1::])
            self.data[:-1] = self.data[1:] #前移
            self.data[-1] = self.tmp
        self.curve.setData(self.data)
        self.idx += 1
if __name__ == '__main__':

    app = QApplication([])
    main_window = MainWindow()
    main_window.ui.show()
    sys.exit(app.exec_())