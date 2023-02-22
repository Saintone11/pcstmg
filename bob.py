import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtCore

form_class = uic.loadUiType("C:\\project2\\bob.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_View.clicked.connect(self.viewFunction)
        self.pushButton_manage.clicked.connect(self.manageFunction)
        self.pushButton_enroll.clicked.connect(self.enrollFunction)
        self.pushButton_history.clicked.connect(self.historyFunction)
        self.pushButton_info.clicked.connect(self.infoFunction)
    def viewFunction(self):
        print("test")

    def manageFunction(self):
        print("test")
        
    def enrollFunction(self):
        print("test")
        
    def historyFunction(self):
        print("test")

    def infoFunction(self):
        print("test")
        """
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveAsFunction.triggered.connect(self.saveAsFunction)
        self.action_close.triggered.connect(self.close)
        
        self.action_undo.triggered.connect(self.undoFunction)
        self.action_cut.triggered.connect(self.cutFunction)
        self.action_copy.triggered.connect(self.copyFunction)
        self.action_paste.triggered.connect(self.pasteFunction)

        self.action_find.triggered.connect(self.findFunction)

        self.opened_file_path = '제목 없음'
        self.opened = False

    def findFunction(self):
        findWindow(self)

    def undoFunction(self):
        self.plainTextEdit.undo()
    
    def cutFunction(self):
        self.plainTextEdit.cut()

    def copyFunction(self):
        self.plainTextEdit.copy()

    def pasteFunction(self):
        self.plainTextEdit.paste()

    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경 내용을 {}저장하시겠습니까?".format(self.opened_file_path))
        msgBox.addButton('저장', QMessageBox.YesRole)
        msgBox.addButton('저장 안 함', QMessageBox.NoRole)
        msgBox.addButton('취소', QMessageBox.RejectRole)
        ret = msgBox.exec_()
        return ret

    def closeEvent(self, event):
        ret = self.save_changed_data()
        if ret == 0:
            self.saveFunction()
        if ret == 2:
            event.ignore()
        

    def save_file(self, fname):
         data = self.plainTextEdit.toPlainText()
         with open(fname,'w', encoding='UTF8') as f:
            f.write(data)
         self.opened = True
         self.opened_file_path = fname

    
    def open_file(self, fname):
        with open(fname, encoding='UTF8') as f:
            data = f.read()
        self.plainTextEdit.setPlainText(data)
        self.opened = True
        self.opened_file_path = fname

    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:   
            self.open_file(fname[0])

    def saveFunction(self):
        if self.opened:
            self.save_file(self.opened_file_path)
        else:
            self.saveAsFunction()
    
    def saveAsFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0]:
            self.save_file(fname[0])
"""

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()