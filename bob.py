import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtCore
from PyQt5 import QtGui

form_class = uic.loadUiType("C:\\project2\\bob.ui")[0]

class manage(QDialog):
    def __init__(self, parent):
        super(manage, self).__init__(parent)
        uic.loadUi("C:\\project2\\delete.ui", self)
        self.show()
        self.pushButton_dsearch.clicked.connect(self.dsearchFunction)
        
        

    def inFunction(self):
        name = self.lineEdit.text()
        num = self.lineEdit_4.text()
        data = pd.read_csv("test.csv", encoding = 'euc-kr')
        data.loc[data["품명"]==name,"현재 수량"] = int(data.loc[data["품명"]==name,"현재 수량"]) + int(num)
        data.to_csv("test.csv", encoding = 'euc-kr',index=False)
        self.close()

    def outFunction(self):
        name = self.lineEdit.text()
        num = self.lineEdit_5.text()
        data = pd.read_csv("test.csv", encoding = 'euc-kr')
        data.loc[data["품명"]==name,"현재 수량"] = int(data.loc[data["품명"]==name,"현재 수량"]) - int(num)
        data.to_csv("test.csv", encoding = 'euc-kr',index=False)
        self.close()

    def dsearchFunction(self):
        name = self.lineEdit.text()
        data = pd.read_csv("test.csv", encoding = 'euc-kr')
        searched_data = data.loc[data['품명'] == name]
        if searched_data.empty == False:
            current = searched_data['현재 수량'].values[0]
            degree = searched_data['단위'].values[0]
            self.lineEdit_2.setText(str(current)) 
            self.lineEdit_3.setText(degree)
            self.pushButton_in.setEnabled(True)
            self.pushButton_out.setEnabled(True)
            self.pushButton_fdelete.setEnabled(True)
            self.pushButton_in.clicked.connect(self.inFunction)
            self.pushButton_out.clicked.connect(self.outFunction)
            self.pushButton_fdelete.clicked.connect(self.fdeleteFunction)

    def fdeleteFunction(self):
        text = self.lineEdit.text()
        data = pd.read_csv("test.csv", encoding = 'euc-kr')
        data.drop(data[data['품명'] == text].index,inplace=True)
        data.to_csv("test.csv", encoding = 'euc-kr',index=False)
        self.close()

class enroll(QDialog):
    def __init__(self, parent):
        super(enroll,self).__init__(parent)
        uic.loadUi("C:\\project2\\enroll.ui", self)
        self.show()
        self.parent = parent
        self.pushButton_finalenroll.clicked.connect(self.finalenrollFunction)
        self.pushButton_cancle.clicked.connect(self.close)

    def finalenrollFunction(self):
        data = pd.read_csv("test.csv", encoding = 'euc-kr')
        data.loc[data.shape[0]] = [self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),self.lineEdit_6.text()]
        data.to_csv("test.csv", encoding = 'euc-kr',index=False)
        self.close()

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_View.clicked.connect(self.viewFunction)
        self.pushButton_manage.clicked.connect(self.manageFunction)
        self.pushButton_enroll.clicked.connect(self.enrollFunction)
        self.pushButton_info.clicked.connect(self.infoFunction)
        self.pushButton_Search.clicked.connect(self.searchFunction)

    def searchFunction(self):
        column_headers = ['품명', '현재 수량', '기준 수량','단위','분류','판매처','부족수량']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        text = self.lineEdit_Search.text()
        data = pd.read_csv("test.csv", encoding = 'euc-kr')
        searched_data = data[data[self.comboBox.currentText()].str.contains(text)]
        row = searched_data.shape[0]
        col = searched_data.shape[1]
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col+1)
        self.setTableWidgetData(searched_data, row, col)

    def viewFunction(self):
        column_headers = ['품명', '현재 수량', '기준 수량','단위','분류','판매처','부족수량']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        data = pd.read_csv("test.csv", encoding = 'euc-kr')
        row = data.shape[0]
        col = data.shape[1]
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col+1)
        self.setTableWidgetData(data, row, col)

    def setTableWidgetData(self,data,row,col):
        for i in range (0, row):
            for j in range (0,col):
               if j == 1 or j == 2:
                   self.tableWidget.setItem(i, j, QTableWidgetItem(str(data.iloc[i][j])))
               else:
                   self.tableWidget.setItem(i, j, QTableWidgetItem(data.iloc[i][j]))
        for i in range (0, row):
            self.tableWidget.setItem(i,6,QTableWidgetItem(str(int(self.tableWidget.item(i,2).text())-int(self.tableWidget.item(i,1).text()))))
            if int(self.tableWidget.item(i,6).text()) != 0:
                self.tableWidget.item(i, 6).setBackground(QtGui.QColor(200,0,0))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def manageFunction(self):
        manage(self)
        
    def enrollFunction(self):
        enroll(self)

    def infoFunction(self):
        print("test")
        
app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()