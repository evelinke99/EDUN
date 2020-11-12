from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pyqtgraph import PlotWidget,mkPen
import numpy as np
import sympy as sym
import random
import re
import Class as cl
import os
import icons_rc

class Ui_MainWindow(object):
    "Főoldal"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 616)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setStyleSheet("background-image: url(:/images/images/fohatter.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 20, 131, 71))
        self.pushButton_5.setStyleSheet("background:rgb(143, 224, 166)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(710, 20, 131, 71))
        self.pushButton_6.setStyleSheet("background:rgb(143, 224, 166)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 131, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/fogomb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(128, 68))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 20, 131, 71))
        self.pushButton_3.setStyleSheet("background:rgb(143, 224, 166)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 20, 131, 71))
        self.pushButton_4.setStyleSheet("background:rgb(143, 224, 166)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 190, 391, 291))
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 20, 131, 71))
        self.pushButton_2.setStyleSheet("background:rgb(143, 224, 166)")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Főoldal"))
        self.pushButton_5.setText(_translate("MainWindow", "Osztás"))
        self.pushButton_6.setText(_translate("MainWindow", "Kaland"))
        self.pushButton_3.setText(_translate("MainWindow", "Összetett függvények"))
        self.pushButton_4.setText(_translate("MainWindow", "Szorzás"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#45be61;\">Üdvözöljük az EDUN főoldalán!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#45be61;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#005500;\">Az alkalmazás célja, hogy segítsen a deriválás alapjainak elsajátításában. Ezt a folyamatot próbálja színesíteni néhány látványosabb eszköz.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#005500;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#005500;\">Válaszd ki a gyakorolni kívánt feladattípust, és kezdődjön is a móka!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#005500;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#005500;\">Kellemes és hasznos időtöltést!  </span><img src=\":/images/images/wink.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#005500;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Alapderiváltak"))


class Ui_MainWindow2(object):
    "Alapderiváltak"
    rightSolvedExercises=[]
    def setupUi(self, MainWindow2):
        try:
            MainWindow2.setObjectName("MainWindow2")
            MainWindow2.resize(852, 616)
            MainWindow2.setFocusPolicy(QtCore.Qt.StrongFocus)
            MainWindow2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.centralwidget = QtWidgets.QWidget(MainWindow2)
            self.centralwidget.setObjectName("centralwidget")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(10, 20, 131, 71))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/images/images/fogomb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QtCore.QSize(128, 68))
            self.pushButton.setObjectName("pushButton")
            self.graphicsView = PlotWidget(self.centralwidget)
            self.graphicsView.setGeometry(QtCore.QRect(385, 111, 441, 451))
            self.graphicsView.setObjectName("graphicsView")
            self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
            self.textBrowser.setGeometry(QtCore.QRect(80, 110, 251, 71))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.textBrowser.setFont(font)
            self.textBrowser.setObjectName("textBrowser")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(10, 110, 81, 71))
            self.label.setObjectName("label")
            self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
            self.textEdit.setGeometry(QtCore.QRect(80, 240, 251, 71))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.textEdit.setFont(font)
            self.textEdit.setObjectName("textEdit")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(10, 240, 81, 71))
            self.label_2.setObjectName("label_2")
            self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox.setGeometry(QtCore.QRect(200, 190, 151, 20))
            self.checkBox.setObjectName("checkBox")
            self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox_2.setGeometry(QtCore.QRect(200, 320, 161, 20))
            self.checkBox_2.setObjectName("checkBox_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(150, 20, 671, 71))
            self.label_3.setStyleSheet("background: rgb(143, 224, 166);")
            self.label_3.setObjectName("label_3")
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(50, 390, 111, 41))
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(False)
            font.setWeight(50)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setStyleSheet("background-color: rgb(198, 249, 203);")
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(210, 390, 111, 41))
            self.pushButton_3.setStyleSheet("background-color: rgb(198, 249, 203);")
            self.pushButton_3.setObjectName("pushButton_3")
            self.iconlabel = QtWidgets.QLabel(self.centralwidget)
            self.iconlabel.setGeometry(QtCore.QRect(340, 250, 40, 51))
            self.iconlabel.setText("")
            self.iconlabel.setObjectName("iconlabel")
            self.label_2.raise_()
            self.label.raise_()
            self.pushButton.raise_()
            self.graphicsView.raise_()
            self.textBrowser.raise_()
            self.textEdit.raise_()
            self.checkBox.raise_()
            self.checkBox_2.raise_()
            self.label_3.raise_()
            self.pushButton_2.raise_()
            self.pushButton_3.raise_()
            self.iconlabel.raise_()
            MainWindow2.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow2)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
            self.menubar.setObjectName("menubar")
            MainWindow2.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow2)
            self.statusbar.setObjectName("statusbar")
            MainWindow2.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow2)
            QtCore.QMetaObject.connectSlotsByName(MainWindow2)

            Controller.loadAlapderivaltak()

            self.graphicsView.setBackground('w')
            pencolor=mkPen(color=(0,0,0),width=3)
            self.graphicsView.plotItem.getAxis('left').setPen(pencolor)
            self.graphicsView.plotItem.getAxis('bottom').setPen(pencolor)
            self.graphicsView.plotItem.getAxis('left').setTextPen(pencolor)
            self.graphicsView.plotItem.getAxis('bottom').setTextPen(pencolor)

            self.generated=self.basicrand()
            self.textBrowser.setText(str(self.generated[0]))
            self.solution=sym.diff(self.generated[0])

        except TypeError:
            pass

        self.pushButton_2.clicked.connect(self.checking)
        self.checkBox.stateChanged.connect(self.drawFuncBtn)
        self.pushButton_3.clicked.connect(self.next)
        self.checkBox_2.stateChanged.connect(self.checkBoxChecking)


    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Alapderiváltak"))
        self.label.setText(_translate("MainWindow2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f(x)=</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f</span><span style=\" font-size:14pt;\">\'</span><span style=\" font-size:12pt;\">(x)=</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow2", "Függvény kirajzolása"))
        self.checkBox_2.setText(_translate("MainWindow2", "Függvény kirajzolása"))
        self.label_3.setText(_translate("MainWindow2", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Alapderiváltak</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow2", "Ellenőriz"))
        self.pushButton_3.setText(_translate("MainWindow2", "Tovább"))


    def next(self):
        try:
            if self.checking() and len(self.rightSolvedExercises)!=self.generated[2]:
                self.default()
            elif self.checking() and len(self.rightSolvedExercises)==self.generated[2]:
                Controller.openedalapderivaltak=False
                raise cl.FinishedChallange('alapderiváltak')
            else:
                raise cl.MissingAnswer()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()


        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnAlapderivaltak)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton1)
            msg.exec()

    def checking(self):
        try:
            exercise = self.textBrowser.toPlainText()
            solution = self.textEdit.toPlainText()

            new = cl.Exercises(exercise, solution)

            feladat = new.getExercise()
            realsol = sym.diff(feladat)

            if solution=="":
                raise cl.MissingAnswer
            else:
                if realsol.equals(solution):
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/greentickmark.png"))
                    if str(self.generated[1]) not in self.rightSolvedExercises:
                        self.rightSolvedExercises.append(str(self.generated[1]))
                    return True
                else:
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/redcross.png"))
                    return False

        except cl.MissingAnswer:
            pass


    def default(self):
        self.generated=self.basicrand()
        self.textBrowser.setText(str(self.generated[0]))
        self.solution = sym.diff(self.generated[0])
        self.textEdit.clear()
        self.iconlabel.clear()
        self.textEdit.setStyleSheet("")
        self.graphicsView.clear()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)


    def checkBoxChecking(self):
        try:
            if self.checkBox_2.checkState() and (self.checking() == False or self.textEdit.toPlainText() == ""):
                raise cl.MissingAnswer()
            else:
                self.drawDiffFuncBtn()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()


    def drawFuncBtn(self):
        self.drawFunc(self.getXvalues(self.generated[0]))

    def drawDiffFuncBtn(self):
        self.drawDiffFunc(self.getXvalues(self.solution))


    def basicrand(self):
        "kigenerál egy random függvénytípust -->feladatot (egy futtatáskor csak egyszer)"
        "visszaadja még a feladattípusát és a típusok db számát is ami később lényeges"
        try:
            x = sym.symbols('x')
            k = sym.symbols('k', integer=True)

            types = [k*x ** k, sym.sin(x),sym.tan(x),sym.cos(x),sym.asin(x), sym.acot(x), sym.exp(x), k ** x, sym.atan(x),k, x ** k,sym.ln(x), sym.cot(x), sym.acos(x)]

            if len(self.rightSolvedExercises)==len(types):
                Controller.openedalapderivaltak=False
                raise cl.FinishedChallange('alapderiváltak')

            while len(self.rightSolvedExercises) != len(types):
                exerciseType = random.choice(types)
                if str(exerciseType) not in self.rightSolvedExercises:
                    exercise = exerciseType.replace(k, random.randint(1, 10))
                    return exercise, exerciseType,len(types)
                if str(exerciseType) in self.rightSolvedExercises:
                     return self.basicrand()

        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn=msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnAlapderivaltak())
            againBtn=msg.addButton('Újra',msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton1)
            msg.exec()


    def getXvalues(self,function):
        "visszatér az adott függvény értelmezési tartományával"
        x = sym.symbols('x')

        if function == sym.ln(x) or function==1/x :
            return np.arange(0.1, 20, 0.1)

        elif function == sym.cot(x) or function==sym.diff(sym.cot(x)):
            return np.arange(0.1,6,0.1)

        elif function == sym.exp(x)  or function == sym.sin(x) or function == sym.cos(x) or function == sym.acot(x):
            return np.arange(-10, 10, 0.1)

        elif function == sym.asin(x) or function == sym.acos(x) or function==sym.diff(sym.asin(x)) or function==sym.diff(sym.acos(x)):
            return np.arange(-1, 1, 0.1)
        elif function == sym.tan(x) or function==sym.diff(sym.tan(x)):
            return np.arange(-3,3,0.1)
        else:
            return np.arange(-10, 10, 0.1)


    def drawing(self,exercise,pen,name,xValues):
        "Függvény x és y tengelyértékeinek tömbbé alakítása és kirajzolása"
        x=Controller.values(exercise,xValues)[0]
        y=Controller.values(exercise,xValues)[1]

        x=np.array(x,dtype='float')
        y=np.array(y,dtype='float')

        self.graphicsView.plot(x,y,pen=pen,name=name)


    def drawFunc(self,xValues):
        "alapfüggvény kirajzolását végzi ha a checkbox be van pipálva illetve törlését ha nincs bepipálva"
        color1=mkPen(color=(0,0,128),width=3)
        color2=mkPen(color=(153,0,76),width=3)
        if self.checkBox.isChecked():
            self.drawing(self.generated[0], color1, "f(x)",xValues)
        else:
            if self.checkBox_2.isChecked() and self.checking()== True:
                self.graphicsView.clear()
                self.drawing(self.solution, color2, "f'(x)",xValues)
            else:
                self.graphicsView.clear()


    def drawDiffFunc(self,xValues):
        "derivált függvény kirajzolását végzi ha a checkbox be van pipálva illetve törlését ha nincs bepipálva"
        color1 = mkPen(color=(0, 0, 128), width=3)
        color2 = mkPen(color=(153, 0, 76), width=3)
        if self.checkBox_2.isChecked():
            self.drawing(self.solution, color2, "f'(x)",xValues)
        else:
            if self.checkBox.isChecked():
                self.graphicsView.clear()
                self.drawing(self.generated[0], color1, "f(x)",xValues)
            else:
                self.graphicsView.clear()


class Ui_MainWindow3(object):
    rightSolvedExercises=[]
    def setupUi(self, MainWindow3):
        try:
            MainWindow3.setObjectName("MainWindow3")
            MainWindow3.resize(852, 616)
            MainWindow3.setFocusPolicy(QtCore.Qt.StrongFocus)
            MainWindow3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.centralwidget = QtWidgets.QWidget(MainWindow3)
            self.centralwidget.setObjectName("centralwidget")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(10, 20, 131, 71))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/images/images/fogomb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QtCore.QSize(128, 68))
            self.pushButton.setObjectName("pushButton")
            self.graphicsView = PlotWidget(self.centralwidget)
            self.graphicsView.setGeometry(QtCore.QRect(385, 111, 441, 451))
            self.graphicsView.setObjectName("graphicsView")
            self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
            self.textBrowser.setGeometry(QtCore.QRect(80, 110, 251, 71))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textBrowser.setFont(font)
            self.textBrowser.setObjectName("textBrowser")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(10, 110, 81, 71))
            self.label.setObjectName("label")
            self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
            self.textEdit.setGeometry(QtCore.QRect(80, 240, 251, 71))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textEdit.setFont(font)
            self.textEdit.setObjectName("textEdit")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(10, 240, 81, 71))
            self.label_2.setObjectName("label_2")
            self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox.setGeometry(QtCore.QRect(200, 190, 151, 20))
            self.checkBox.setObjectName("checkBox")
            self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox_2.setGeometry(QtCore.QRect(200, 320, 161, 20))
            self.checkBox_2.setObjectName("checkBox_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(150, 20, 671, 71))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("background: rgb(143, 224, 166);")
            self.label_3.setObjectName("label_3")
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(50, 390, 111, 41))
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(False)
            font.setWeight(50)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setStyleSheet("background-color: rgb(198, 249, 203);")
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(210, 390, 111, 41))
            self.pushButton_3.setStyleSheet("background-color: rgb(198, 249, 203);")
            self.pushButton_3.setObjectName("pushButton_3")
            self.iconlabel = QtWidgets.QLabel(self.centralwidget)
            self.iconlabel.setGeometry(QtCore.QRect(340, 250, 40, 51))
            self.iconlabel.setText("")
            self.iconlabel.setObjectName("iconlabel")
            self.label_2.raise_()
            self.label.raise_()
            self.pushButton.raise_()
            self.graphicsView.raise_()
            self.textBrowser.raise_()
            self.textEdit.raise_()
            self.checkBox.raise_()
            self.checkBox_2.raise_()
            self.label_3.raise_()
            self.pushButton_2.raise_()
            self.pushButton_3.raise_()
            self.iconlabel.raise_()
            MainWindow3.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow3)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
            self.menubar.setObjectName("menubar")
            MainWindow3.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow3)
            self.statusbar.setObjectName("statusbar")
            MainWindow3.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow3)
            QtCore.QMetaObject.connectSlotsByName(MainWindow3)

            Controller.loadOsszetett()

            self.graphicsView.setBackground('w')
            pencolor = mkPen(color=(0, 0, 0), width=3)
            self.graphicsView.plotItem.getAxis('left').setPen(pencolor)
            self.graphicsView.plotItem.getAxis('bottom').setPen(pencolor)
            self.graphicsView.plotItem.getAxis('left').setTextPen(pencolor)
            self.graphicsView.plotItem.getAxis('bottom').setTextPen(pencolor)

            self.generated = self.randomComplexFunction()
            self.textBrowser.setText(str(self.generated[0]))
            self.solution = sym.diff(self.generated[0])

        except TypeError:
            pass

        self.pushButton_2.clicked.connect(self.checking)
        self.checkBox.stateChanged.connect(self.drawFuncBtn)
        self.pushButton_3.clicked.connect(self.next)
        self.checkBox_2.stateChanged.connect(self.checkBoxChecking)


    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "Összetett függvények"))
        self.label.setText(_translate("MainWindow3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f(x)=</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f</span><span style=\" font-size:14pt;\">\'</span><span style=\" font-size:12pt;\">(x)=</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow3", "Függvény kirajzolása"))
        self.checkBox_2.setText(_translate("MainWindow3", "Függvény kirajzolása"))
        self.label_3.setText(_translate("MainWindow3", "<html><head/><body><p align=\"center\">Összetett függvények</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow3", "Ellenőriz"))
        self.pushButton_3.setText(_translate("MainWindow3", "Tovább"))


    def randomComplexFunction(self):
        "kigenerál egy random függvénytípust -->feladatot (egy futtatáskor csak egyszer)"
        "visszaadja még a feladattípusát és a típusok db számát is ami később lényeges"
        try:
            x = sym.symbols('x')
            k = sym.symbols('k', integer=True)

            types = [sym.sin(x**k),sym.tan(sym.sin(k*x)**k),sym.cos(k-x**k+k),sym.cos(sym.ln(x**k)),sym.ln(k*x+sym.sin(x)-x**k),sym.exp(k+k*x-k),k**sym.sin(x)]

            if len(self.rightSolvedExercises)==len(types):
                Controller.openedalapderivaltak=False
                raise cl.FinishedChallange('összetett függvények')

            while len(self.rightSolvedExercises) != len(types):
                exerciseType = random.choice(types)
                if str(exerciseType) not in self.rightSolvedExercises:
                    exercise = exerciseType.replace(k, random.randint(1, 10))
                    return exercise, exerciseType,len(types)
                if str(exerciseType) in self.rightSolvedExercises:
                     return self.randomComplexFunction()


        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnOsszetett)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton2)
            msg.exec()

    def checking(self):
        try:
            exercise = self.textBrowser.toPlainText()
            solution = self.textEdit.toPlainText()

            new = cl.Exercises(exercise, solution)

            feladat = new.getExercise()
            realsol = sym.diff(feladat)

            if solution=="":
                raise cl.MissingAnswer
            else:
                if realsol.equals(solution):
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/greentickmark.png"))
                    if str(self.generated[1]) not in self.rightSolvedExercises:
                        self.rightSolvedExercises.append(str(self.generated[1]))
                    return True
                else:
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/redcross.png"))
                    return False

        except cl.MissingAnswer:
            pass


    def next(self):
        try:
            if self.checking() and len(self.rightSolvedExercises)!=self.generated[2]:
                self.default()
            elif self.checking() and len(self.rightSolvedExercises)==self.generated[2]:
                Controller.openedosszetett=False
                raise cl.FinishedChallange('összetett függvények')
            else:
                raise cl.MissingAnswer()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()


        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnOsszetett)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton2)
            msg.exec()


    def default(self):
        self.generated=self.randomComplexFunction()
        self.textBrowser.setText(str(self.generated[0]))
        self.solution = sym.diff(self.generated[0])
        self.textEdit.clear()
        self.iconlabel.clear()
        self.textEdit.setStyleSheet("")
        self.graphicsView.clear()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)


    def getXvalues(self,function):
        "visszaadja az adott függvény értelmezési tartományát"
        x = sym.symbols('x')

        if re.search(".*tan.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search(".*tan.*",str(self.generated[0])) != None ):
            return np.arange(-3, 3, 0.1)

        elif (re.search(".*sin.x.",str(function)) != None and len(str(function))==len(re.search(".*sin.x.",str(function))[0])) or (function==sym.diff(self.generated[0]) and re.search(".*sin.x.",str(self.generated[0])) != None ):
            return np.arange(-5,5,0.1)

        elif re.search(".*cos.*log.*x*.",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search(".*cos.*log.*x*.",str(self.generated[0])) != None ):
            return np.arange(0.1, 10, 0.1)

        elif function==sym.simplify(sym.ln(1 * sym.sin(x) - x ** 1)): #ennek felül kell lennie
            return np.arange(-4,-0.1,0.1)

        elif re.search(".*log.*x.*sin.x.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search(".*log.*x.*sin.x.*",str(self.generated[0])) != None ):
            return np.arange(0.1, 1.4, 0.1)

        elif re.search("exp(.*x.*)",str(self.generated[0])) != None or (function==sym.diff(self.generated[0]) and re.search("exp(.*x.*)",str(self.generated[0])) != None ):
            return np.arange(-4, 3, 0.1)
        else:
            return np.arange(-4, 4, 0.1)


    def drawing(self,exercise,pen,name,xValues):
        x=Controller.values(exercise,xValues)[0]
        y=Controller.values(exercise,xValues)[1]

        x=np.array(x,dtype='float')
        y=np.array(y,dtype='float')

        self.graphicsView.plot(x,y,pen=pen,name=name)


    def drawFunc(self,xValues):
        "alapfüggvény kirajzolását végzi ha a checkbox be van pipálva illetve törlését ha nincs bepipálva"
        color1=mkPen(color=(0,0,128),width=3)
        color2=mkPen(color=(153,0,76),width=3)
        if self.checkBox.isChecked():
            self.drawing(self.generated[0], color1, "f(x)",xValues)
        else:
            if self.checkBox_2.isChecked() and self.checking()== True:
                self.graphicsView.clear()
                self.drawing(self.solution, color2, "f'(x)",xValues)
            else:
                self.graphicsView.clear()


    def drawDiffFunc(self,xValues):
        "derivált függvény kirajzolását végzi ha a checkbox be van pipálva illetve törlését ha nincs bepipálva"
        color1 = mkPen(color=(0, 0, 128), width=3)
        color2 = mkPen(color=(153, 0, 76), width=3)
        if self.checkBox_2.isChecked():
            self.drawing(self.solution, color2, "f'(x)",xValues)
        else:
            if self.checkBox.isChecked():
                self.graphicsView.clear()
                self.drawing(self.generated[0], color1, "f(x)",xValues)
            else:
                self.graphicsView.clear()


    def drawFuncBtn(self):
        self.drawFunc(self.getXvalues(self.generated[0]))
        #self.drawFunc(np.arange(-10, 10, 0.1))

    def drawDiffFuncBtn(self):
        self.drawDiffFunc(self.getXvalues(self.solution))
        #self.drawDiffFunc(np.arange(-10, 10, 0.1))


    def checkBoxChecking(self):
        try:
            if self.checkBox_2.checkState() and (self.checking() == False or self.textEdit.toPlainText() == ""):
                raise cl.MissingAnswer()
            else:
                self.drawDiffFuncBtn()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()


class Ui_MainWindow4(object):
    rightSolvedExercises=[]
    def setupUi(self, MainWindow4):
        try:
            MainWindow4.setObjectName("MainWindow4")
            MainWindow4.resize(852, 616)
            MainWindow4.setFocusPolicy(QtCore.Qt.StrongFocus)
            MainWindow4.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.centralwidget = QtWidgets.QWidget(MainWindow4)
            self.centralwidget.setObjectName("centralwidget")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(10, 20, 131, 71))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/images/images/fogomb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QtCore.QSize(128, 68))
            self.pushButton.setObjectName("pushButton")
            self.graphicsView = PlotWidget(self.centralwidget)
            self.graphicsView.setGeometry(QtCore.QRect(385, 111, 441, 451))
            self.graphicsView.setObjectName("graphicsView")
            self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
            self.textBrowser.setGeometry(QtCore.QRect(80, 110, 251, 71))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.textBrowser.setFont(font)
            self.textBrowser.setObjectName("textBrowser")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(10, 110, 81, 71))
            self.label.setObjectName("label")
            self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
            self.textEdit.setGeometry(QtCore.QRect(80, 240, 251, 71))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.textEdit.setFont(font)
            self.textEdit.setObjectName("textEdit")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(10, 240, 81, 71))
            self.label_2.setObjectName("label_2")
            self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox.setGeometry(QtCore.QRect(200, 190, 151, 20))
            self.checkBox.setObjectName("checkBox")
            self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox_2.setGeometry(QtCore.QRect(200, 320, 161, 20))
            self.checkBox_2.setObjectName("checkBox_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(150, 20, 671, 71))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("background: rgb(143, 224, 166);")
            self.label_3.setObjectName("label_3")
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(50, 390, 111, 41))
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(False)
            font.setWeight(50)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setStyleSheet("background-color: rgb(198, 249, 203);")
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(210, 390, 111, 41))
            self.pushButton_3.setStyleSheet("background-color: rgb(198, 249, 203);")
            self.pushButton_3.setObjectName("pushButton_3")
            self.iconlabel = QtWidgets.QLabel(self.centralwidget)
            self.iconlabel.setGeometry(QtCore.QRect(340, 250, 40, 51))
            self.iconlabel.setText("")
            self.iconlabel.setObjectName("iconlabel")
            self.label_2.raise_()
            self.label.raise_()
            self.pushButton.raise_()
            self.graphicsView.raise_()
            self.textBrowser.raise_()
            self.textEdit.raise_()
            self.checkBox.raise_()
            self.checkBox_2.raise_()
            self.label_3.raise_()
            self.pushButton_2.raise_()
            self.pushButton_3.raise_()
            self.iconlabel.raise_()
            MainWindow4.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow4)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
            self.menubar.setObjectName("menubar")
            MainWindow4.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow4)
            self.statusbar.setObjectName("statusbar")
            MainWindow4.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow4)
            QtCore.QMetaObject.connectSlotsByName(MainWindow4)

            Controller.loadSzorzas()

            self.graphicsView.setBackground('w')
            pencolor = mkPen(color=(0, 0, 0), width=3)
            self.graphicsView.plotItem.getAxis('left').setPen(pencolor)
            self.graphicsView.plotItem.getAxis('bottom').setPen(pencolor)
            self.graphicsView.plotItem.getAxis('left').setTextPen(pencolor)
            self.graphicsView.plotItem.getAxis('bottom').setTextPen(pencolor)

            self.generated = self.randomMultiplicationFunction()
            self.textBrowser.setText(str(self.generated[0]))
            self.solution = sym.diff(self.generated[0])

        except TypeError:
            pass


        self.pushButton_2.clicked.connect(self.checking)
        self.checkBox.stateChanged.connect(self.drawFuncBtn)
        self.pushButton_3.clicked.connect(self.next)
        self.checkBox_2.stateChanged.connect(self.checkBoxChecking)


    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow4", "Szorzás"))
        self.label.setText(_translate("MainWindow4", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f(x)=</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow4", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f</span><span style=\" font-size:14pt;\">\'</span><span style=\" font-size:12pt;\">(x)=</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow4", "Függvény kirajzolása"))
        self.checkBox_2.setText(_translate("MainWindow4", "Függvény kirajzolása"))
        self.label_3.setText(_translate("MainWindow4", "<html><head/><body><p align=\"center\">Szorzás</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow4", "Ellenőriz"))
        self.pushButton_3.setText(_translate("MainWindow4", "Tovább"))

    def randomMultiplicationFunction(self):
        try:
            x = sym.symbols('x')
            k = sym.symbols('k', integer=True)

            types = [sym.exp(sym.cos(x)*sym.ln(x)),x**k*k**x,k*x**k*sym.ln(sym.cos(x)),k*sym.sin(k*x)*sym.cos(x**k),(x**k+k*x+k)*sym.tan(k**x),sym.cos(k*x)*sym.exp(sym.tan(x))]

            if len(self.rightSolvedExercises)==len(types):
                Controller.openedszorzas=False
                raise cl.FinishedChallange('szorzás')

            while len(self.rightSolvedExercises) != len(types):
                exerciseType = random.choice(types)
                if str(exerciseType) not in self.rightSolvedExercises:
                    exercise = exerciseType.replace(k, random.randint(2, 10))
                    return exercise, exerciseType,len(types)
                if str(exerciseType) in self.rightSolvedExercises:
                     return self.randomMultiplicationFunction()


        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnSzorzas)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton3)
            msg.exec()


    def getXvalues(self,function):
        "visszaadja az adott függvény értelmezési tartományát"
        x = sym.symbols('x')
        k = sym.symbols('k', integer=True)

        # if re.search("exp.log.x.*cos.x.*",str(function)) != None or (function==sym.simplify(sym.diff(self.generated[0])) and re.search("exp.log.x.*cos.x.*",str(self.generated[0])) != None ):
        #     return np.arange(0.1, 20, 0.1)

        if re.search("exp.tan.x.*cos.*x.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search("exp.tan.x.*cos.*x.*",str(self.generated[0])) != None ):
            return np.arange(-1, 1.3, 0.1)

        elif re.search(".x.*x.*tan.*x.",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search(".x.*x.*tan.*x.",str(self.generated[0])) != None ):
            return np.arange(-1, 2.5, 0.1)

        elif re.search(".*x.*log.*cos.x.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search(".*x.*log.*cos.x.*",str(self.generated[0])) != None ):
            return np.arange(5, 7, 0.1)

        elif re.search(".*x.x.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search(".*x.x.*",str(self.generated[0])) != None ) or re.search(".*sin.*.*cos.x.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search(".*sin.*.*cos.x.*",str(self.generated[0])) != None ):
            return np.arange(-5, 5, 0.1)

        else:
            return np.arange(0.1, 20, 0.1)


    def checking(self):
        try:
            exercise = self.textBrowser.toPlainText()
            solution = self.textEdit.toPlainText()

            new = cl.Exercises(exercise, solution)

            feladat = new.getExercise()
            realsol = sym.diff(feladat)

            if solution=="":
                raise cl.MissingAnswer
            else:
                if realsol.equals(solution):
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/greentickmark.png"))
                    if str(self.generated[1]) not in self.rightSolvedExercises:
                        self.rightSolvedExercises.append(str(self.generated[1]))
                    return True
                else:
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/redcross.png"))
                    return False

        except cl.MissingAnswer:
            pass


    def next(self):
        try:
            if self.checking() and len(self.rightSolvedExercises)!=self.generated[2]:
                self.default()
            elif self.checking() and len(self.rightSolvedExercises)==self.generated[2]:
                Controller.openedszorzas=False
                raise cl.FinishedChallange('szorzás')
            else:
                raise cl.MissingAnswer()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()


        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnSzorzas)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton3)
            msg.exec()


    def default(self):
        self.generated=self.randomMultiplicationFunction()
        self.textBrowser.setText(str(self.generated[0]))
        self.solution = sym.diff(self.generated[0])
        self.textEdit.clear()
        self.iconlabel.clear()
        self.textEdit.setStyleSheet("")
        self.graphicsView.clear()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)


    def drawing(self,exercise,pen,name,xValues):
        x=Controller.values(exercise,xValues)[0]
        y=Controller.values(exercise,xValues)[1]

        x=np.array(x,dtype='float')
        y=np.array(y,dtype='float')

        self.graphicsView.plot(x,y,pen=pen,name=name)


    def drawFunc(self,xValues):
        "alapfüggvény kirajzolását végzi ha a checkbox be van pipálva illetve törlését ha nincs bepipálva"
        color1=mkPen(color=(0,0,128),width=3)
        color2=mkPen(color=(153,0,76),width=3)
        if self.checkBox.isChecked():
            self.drawing(self.generated[0], color1, "f(x)",xValues)
        else:
            if self.checkBox_2.isChecked() and self.checking()== True:
                self.graphicsView.clear()
                self.drawing(self.solution, color2, "f'(x)",xValues)
            else:
                self.graphicsView.clear()


    def drawDiffFunc(self,xValues):
        "derivált függvény kirajzolását végzi ha a checkbox be van pipálva illetve törlését ha nincs bepipálva"
        color1 = mkPen(color=(0, 0, 128), width=3)
        color2 = mkPen(color=(153, 0, 76), width=3)
        if self.checkBox_2.isChecked():
            self.drawing(self.solution, color2, "f'(x)",xValues)
        else:
            if self.checkBox.isChecked():
                self.graphicsView.clear()
                self.drawing(self.generated[0], color1, "f(x)",xValues)
            else:
                self.graphicsView.clear()


    def drawFuncBtn(self):
        self.drawFunc(self.getXvalues(self.generated[0]))
        #self.drawFunc(np.arange(-5, 5, 0.1))

    def drawDiffFuncBtn(self):
        self.drawDiffFunc(self.getXvalues(self.solution))
        #self.drawDiffFunc(np.arange(-5, 5, 0.1))


    def checkBoxChecking(self):
        try:
            if self.checkBox_2.checkState() and (self.checking() == False or self.textEdit.toPlainText() == ""):
                raise cl.MissingAnswer()
            else:
                self.drawDiffFuncBtn()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()


class Ui_MainWindow5(object):

    rightSolvedExercises=[]
    def setupUi(self, MainWindow5):
        try:
            MainWindow5.setObjectName("MainWindow5")
            MainWindow5.resize(852, 616)
            MainWindow5.setFocusPolicy(QtCore.Qt.StrongFocus)
            MainWindow5.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.centralwidget = QtWidgets.QWidget(MainWindow5)
            self.centralwidget.setObjectName("centralwidget")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(10, 20, 131, 71))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/images/images/fogomb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QtCore.QSize(128, 68))
            self.pushButton.setObjectName("pushButton")
            self.graphicsView = PlotWidget(self.centralwidget)
            self.graphicsView.setGeometry(QtCore.QRect(385, 111, 441, 451))
            self.graphicsView.setObjectName("graphicsView")
            self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
            self.textBrowser.setGeometry(QtCore.QRect(80, 110, 251, 71))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textBrowser.setFont(font)
            self.textBrowser.setObjectName("textBrowser")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(10, 110, 81, 71))
            self.label.setObjectName("label")
            self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
            self.textEdit.setGeometry(QtCore.QRect(80, 240, 251, 71))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textEdit.setFont(font)
            self.textEdit.setObjectName("textEdit")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(10, 240, 81, 71))
            self.label_2.setObjectName("label_2")
            self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox.setGeometry(QtCore.QRect(200, 190, 151, 20))
            self.checkBox.setObjectName("checkBox")
            self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox_2.setGeometry(QtCore.QRect(200, 320, 161, 20))
            self.checkBox_2.setObjectName("checkBox_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(150, 20, 671, 71))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("background: rgb(143, 224, 166);")
            self.label_3.setObjectName("label_3")
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(50, 390, 111, 41))
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(False)
            font.setWeight(50)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setStyleSheet("background-color: rgb(198, 249, 203);")
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(210, 390, 111, 41))
            self.pushButton_3.setStyleSheet("background-color: rgb(198, 249, 203);")
            self.pushButton_3.setObjectName("pushButton_3")
            self.iconlabel = QtWidgets.QLabel(self.centralwidget)
            self.iconlabel.setGeometry(QtCore.QRect(340, 250, 40, 51))
            self.iconlabel.setText("")
            self.iconlabel.setObjectName("iconlabel")
            self.label_2.raise_()
            self.label.raise_()
            self.pushButton.raise_()
            self.graphicsView.raise_()
            self.textBrowser.raise_()
            self.textEdit.raise_()
            self.checkBox.raise_()
            self.checkBox_2.raise_()
            self.label_3.raise_()
            self.pushButton_2.raise_()
            self.pushButton_3.raise_()
            self.iconlabel.raise_()
            MainWindow5.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow5)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
            self.menubar.setObjectName("menubar")
            MainWindow5.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow5)
            self.statusbar.setObjectName("statusbar")
            MainWindow5.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow5)
            QtCore.QMetaObject.connectSlotsByName(MainWindow5)

            Controller.loadOsztas()

            self.graphicsView.setBackground('w')
            pencolor = mkPen(color=(0, 0, 0), width=3)
            self.graphicsView.plotItem.getAxis('left').setPen(pencolor)
            self.graphicsView.plotItem.getAxis('bottom').setPen(pencolor)
            self.graphicsView.plotItem.getAxis('left').setTextPen(pencolor)
            self.graphicsView.plotItem.getAxis('bottom').setTextPen(pencolor)

            self.generated = self.randomDivisionFunction()
            self.textBrowser.setText(str(self.generated[0]))
            self.solution = sym.diff(self.generated[0])

        except TypeError:
            pass

        self.pushButton_2.clicked.connect(self.checking)
        self.checkBox.stateChanged.connect(self.drawFuncBtn)
        self.pushButton_3.clicked.connect(self.next)
        self.checkBox_2.stateChanged.connect(self.checkBoxChecking)

    def retranslateUi(self, MainWindow5):
        _translate = QtCore.QCoreApplication.translate
        MainWindow5.setWindowTitle(_translate("MainWindow5", "Osztás"))
        self.label.setText(_translate("MainWindow5", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f(x)=</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow5", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f</span><span style=\" font-size:14pt;\">\'</span><span style=\" font-size:12pt;\">(x)=</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow5", "Függvény kirajzolása"))
        self.checkBox_2.setText(_translate("MainWindow5", "Függvény kirajzolása"))
        self.label_3.setText(_translate("MainWindow5", "<html><head/><body><p align=\"center\">Osztás</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow5", "Ellenőriz"))
        self.pushButton_3.setText(_translate("MainWindow5", "Tovább"))


    def randomDivisionFunction(self):
        try:
            x = sym.symbols('x')
            k = sym.symbols('k', integer=True)

            types = [(sym.tan(sym.sin(k*x**k)))**k/(sym.cos(k**x)),(x**k+k)/(sym.ln(x**k)),sym.tan(sym.ln(k*x))/sym.cos(sym.exp(x)),(sym.exp(x)*sym.sin(x))/x**k*sym.tan(x),sym.acos(k**x)/(k*x**k)]

            if len(self.rightSolvedExercises)==len(types):
                Controller.openedosztas=False
                raise cl.FinishedChallange('osztás')

            while len(self.rightSolvedExercises) != len(types):
                exerciseType = random.choice(types)
                if str(exerciseType) not in self.rightSolvedExercises:
                    exercise = exerciseType.replace(k, random.randint(2, 10))
                    return exercise, exerciseType,len(types)
                if str(exerciseType) in self.rightSolvedExercises:
                     return self.randomDivisionFunction()


        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnOsztas)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton4)
            msg.exec()


    def getXvalues(self,function):
        "visszaadja az adott függvény értelmezési tartományát"
        x = sym.symbols('x')
        k = sym.symbols('k', integer=True)


        if re.search("acos.*x.*x.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search("acos.*x.*x.*",str(self.generated[0])) != None ):
            return np.arange(-1, -0.4, 0.01)

        elif re.search("exp.x.*sin.x.*tan.x.*x.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search("exp.x.*sin.x.*tan.x.*x.*",str(self.generated[0])) != None ):
            return np.arange(-2, -0.3, 0.1)

        elif re.search("tan.*sin.*x.*cos.*x.*",str(function)) != None or (function==sym.diff(self.generated[0]) and re.search("tan.*sin.*x.*cos.*x.*",str(self.generated[0])) != None ):
            return np.arange(-3, 3, 0.1)

        # elif re.search("tan.*log.*x.*cos.*exp.*x.*",str(function)) != None or (function==sym.simplify(sym.diff(self.generated[0])) and re.search("tan.*log.*x.*cos.*exp.*x.*",str(self.generated[0])) != None ):
        #     return np.arange(1.5, 5, 0.1)

        # elif re.search(".*x.*log.*x.*",str(function)) != None or (function==sym.simplify(sym.diff(self.generated[0])) and re.search(".*x.*log.*x.*",str(self.generated[0])) != None ):
        #     return np.arange(0.1, 5, 0.1)
        else:
            return np.arange(1.5,5,0.1)


    def checking(self):
        try:
            exercise = self.textBrowser.toPlainText()
            solution = self.textEdit.toPlainText()

            if solution=="":
                raise cl.MissingAnswer

            else:
                new = cl.Exercises(exercise, solution)
                feladat = new.getExercise()
                realsol = sym.diff(feladat)

                if realsol.equals(solution):
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/greentickmark.png"))
                    if str(self.generated[1]) not in self.rightSolvedExercises:
                        self.rightSolvedExercises.append(str(self.generated[1]))
                    return True
                else:
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/redcross.png"))
                    return False

        except cl.MissingAnswer:
            pass


    def next(self):
        try:
            if self.checking() and len(self.rightSolvedExercises)!=self.generated[2]:
                self.default()
            elif self.checking() and len(self.rightSolvedExercises)==self.generated[2]:
                Controller.openedosztas=False
                raise cl.FinishedChallange('osztás')
            else:
                raise cl.MissingAnswer()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()

        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnOsztas)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton4)
            msg.exec()


    def default(self):
        self.generated=self.randomDivisionFunction()
        self.textBrowser.setText(str(self.generated[0]))
        self.solution = sym.diff(self.generated[0])
        self.textEdit.clear()
        self.iconlabel.clear()
        self.textEdit.setStyleSheet("")
        self.graphicsView.clear()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)


    def drawing(self,exercise,pen,name,xValues):
        x=Controller.values(exercise,xValues)[0]
        y=Controller.values(exercise,xValues)[1]

        x=np.array(x,dtype='float')
        y=np.array(y,dtype='float')

        self.graphicsView.plot(x,y,pen=pen,name=name)


    def drawFunc(self,xValues):
        "alapfüggvény kirajzolását végzi ha a checkbox be van pipálva illetve törlését ha nincs bepipálva"
        color1=mkPen(color=(0,0,128),width=3)
        color2=mkPen(color=(153,0,76),width=3)
        if self.checkBox.isChecked():
            self.drawing(self.generated[0], color1, "f(x)",xValues)
        else:
            if self.checkBox_2.isChecked() and self.checking()== True:
                self.graphicsView.clear()
                self.drawing(self.solution, color2, "f'(x)",xValues)
            else:
                self.graphicsView.clear()


    def drawDiffFunc(self,xValues):
        "derivált függvény kirajzolását végzi ha a checkbox be van pipálva illetve törlését ha nincs bepipálva"
        color1 = mkPen(color=(0, 0, 128), width=3)
        color2 = mkPen(color=(153, 0, 76), width=3)
        if self.checkBox_2.isChecked():
            self.drawing(self.solution, color2, "f'(x)",xValues)
        else:
            if self.checkBox.isChecked():
                self.graphicsView.clear()
                self.drawing(self.generated[0], color1, "f(x)",xValues)
            else:
                self.graphicsView.clear()


    def drawFuncBtn(self):
        self.drawFunc(self.getXvalues(self.generated[0]))
        #self.drawFunc(np.arange(-5, 5, 0.1))

    def drawDiffFuncBtn(self):
        self.drawDiffFunc(self.getXvalues(self.solution))
        #self.drawDiffFunc(np.arange(-5, 5, 0.1))


    def checkBoxChecking(self):
        try:
            if self.checkBox_2.checkState() and (self.checking() == False or self.textEdit.toPlainText() == ""):
                raise cl.MissingAnswer()
            else:
                self.drawDiffFuncBtn()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()


class Ui_MainWindow6(object):
    rightSolvedExercises=[]
    bridgeLvl = len(rightSolvedExercises)
    temp=True
    def setupUi(self, MainWindow6):
        MainWindow6.setObjectName("MainWindow6")
        MainWindow6.resize(852, 616)
        MainWindow6.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow6)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 131, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/fogomb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(128, 68))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 120, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 81, 71))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 210, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 81, 71))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 20, 671, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: rgb(143, 224, 166);")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(198, 249, 203);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 300, 111, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(198, 249, 203);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.iconlabel = QtWidgets.QLabel(self.centralwidget)
        self.iconlabel.setGeometry(QtCore.QRect(440, 210, 40, 51))
        self.iconlabel.setText("")
        self.iconlabel.setObjectName("iconlabel")
        self.bridge = QtWidgets.QLabel(self.centralwidget)
        self.bridge.setGeometry(QtCore.QRect(390, 290, 441, 261))
        self.bridge.setText("")
        self.bridge.setObjectName("bridge")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(450, 100, 361, 101))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.ready = QtWidgets.QLabel(self.centralwidget)
        self.ready.setGeometry(QtCore.QRect(110, 360, 211, 191))
        self.ready.setText("")
        self.ready.setObjectName("ready")
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.textBrowser.raise_()
        self.textEdit.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.iconlabel.raise_()
        self.bridge.raise_()
        self.textBrowser_2.raise_()
        self.ready.raise_()
        MainWindow6.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow6)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
        self.menubar.setObjectName("menubar")
        MainWindow6.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow6)
        self.statusbar.setObjectName("statusbar")
        MainWindow6.setStatusBar(self.statusbar)

        Controller.loadKaland()
        self.bridgeLvl=len(self.rightSolvedExercises)
        self.loadPictures()

        self.retranslateUi(MainWindow6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow6)

        self.generated = self.randomExercises()
        self.textBrowser.setText(str(self.generated[0]))
        self.solution = sym.diff(self.generated[0])

        self.pushButton_2.clicked.connect(self.checking)
        self.pushButton_3.clicked.connect(self.next)

    def retranslateUi(self, MainWindow6):
        _translate = QtCore.QCoreApplication.translate
        MainWindow6.setWindowTitle(_translate("MainWindow6", "Kaland"))
        self.label.setText(_translate("MainWindow6", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f(x)=</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow6", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">f</span><span style=\" font-size:14pt;\">\'</span><span style=\" font-size:12pt;\">(x)=</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow6", "<html><head/><body><p align=\"center\">Segíts felépíteni a hidat!</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow6", "Ellenőriz"))
        self.pushButton_3.setText(_translate("MainWindow6", "Tovább"))
        self.textBrowser_2.setHtml(_translate("MainWindow6", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#005500;\">Minden helyes válasszal, hozzájárulhatsz a híd felépítéséhez. </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#005500;\">Ám vigyázat rossz válasszal hátráltathatod a mérnököket!</span></p></body></html>"))

    def loadPictures(self):
        i=self.bridgeLvl

        picture=":/images/images/hid"+str(i)+".png"
        self.bridge.setPixmap(QtGui.QPixmap(picture))

        if i==10:
            self.ready.setPixmap(QtGui.QPixmap(":/images/images/ready.jpg"))


    def randomExercises(self):
        try:
            x = sym.symbols('x')
            k = sym.symbols('k', integer=True)

            types = [(x**k+k*x+k)*sym.tan(k**x),sym.ln(k*x+sym.sin(x)-x**k),(sym.tan(sym.sin(k*x**k)))**k/(sym.cos(k**x)),sym.cos(sym.exp(k*x*k**x)),sym.tan(x**k/sym.ln(x)),sym.sin(x**k)/sym.cos(sym.exp(k*x)),sym.cot(k**x)*sym.cos(x**k),(x**k+sym.sin(sym.exp(x*k)))/sym.ln(x),k**(x**k+k*x)/sym.cos(x),sym.exp(sym.cos(x**k)*sym.tan(x)),]

            if len(self.rightSolvedExercises) == len(types):
                Controller.openedkaland = False
                raise cl.FinishedChallange('kaland')

            while len(self.rightSolvedExercises) != len(types):
                exerciseType = random.choice(types)
                if str(exerciseType) not in self.rightSolvedExercises:
                    exercise = exerciseType.replace(k, random.randint(2, 10))
                    return exercise, exerciseType, len(types)
                if str(exerciseType) in self.rightSolvedExercises:
                    return self.randomExercises()


        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnKaland)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton5)
            msg.exec()


    def checking(self):
        try:
            exercise = self.textBrowser.toPlainText()
            solution = self.textEdit.toPlainText()

            if solution=="":
                raise cl.MissingAnswer

            else:

                new = cl.Exercises(exercise, solution)
                feladat = new.getExercise()
                realsol = sym.diff(feladat)

                if realsol.equals(solution):
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/greentickmark.png"))
                    if str(self.generated[1]) not in self.rightSolvedExercises:
                        self.rightSolvedExercises.append(str(self.generated[1]))
                        self.bridgeLvl=len(self.rightSolvedExercises)
                        self.temp=True
                    return True
                else:
                    self.iconlabel.setPixmap(QtGui.QPixmap(":/images/images/redcross.png"))
                    if self.bridgeLvl >= 2 and self.temp!=False:
                        self.bridgeLvl=self.bridgeLvl-2
                        self.rightSolvedExercises.remove(random.choice(self.rightSolvedExercises))
                        self.rightSolvedExercises.remove(random.choice(self.rightSolvedExercises))
                        self.loadPictures()
                        self.temp=False
                    return False

        except cl.MissingAnswer:
            pass


    def next(self):
        try:
            if self.checking() and len(self.rightSolvedExercises)!=self.generated[2]:
                #self.bridgeLvl+=1
                self.loadPictures()
                self.default()
            elif self.checking() and len(self.rightSolvedExercises)==self.generated[2]:
                Controller.openedkaland=False
                self.loadPictures()
                raise cl.FinishedChallange('kaland')
            else:
                raise cl.MissingAnswer()

        except cl.MissingAnswer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Előbb be kell írnia a helyes megoldást!")
            msg.exec()


        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(Controller.exitBtnKaland)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(Controller.againButton5)
            msg.exec()


    def default(self):
        self.generated=self.randomExercises()
        self.textBrowser.setText(str(self.generated[0]))
        self.solution = sym.diff(self.generated[0])
        self.textEdit.clear()
        self.iconlabel.clear()
        self.textEdit.setStyleSheet("")



class Controller:

    def __init__(self):
        pass

    isalapderivaltak=False
    openedalapderivaltak=True
    isosszetett=False
    openedosszetett=True
    openedszorzas=True
    isszorzas=False
    openedosztas=True
    isosztas=False
    iskaland=False
    openedkaland=True

    def Show_Fooldal(self):
        self.fooldal = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.fooldal)
        self.ui.pushButton_2.clicked.connect(self.Show_Alapderivaltak)
        self.ui.pushButton_3.clicked.connect(self.Show_Osszetett)
        self.ui.pushButton_4.clicked.connect(self.Show_Szorzas)
        self.ui.pushButton_5.clicked.connect(self.Show_Osztas)
        self.ui.pushButton_6.clicked.connect(self.Show_Kaland)
        self.fooldal.show()
        if self.isalapderivaltak:
            self.alapderivaltak.hide()
            self.isalapderivaltak=False
        elif self.isosszetett:
            self.osszetett.hide()
            self.isosszetett=False
        elif self.isszorzas:
            self.szorzas.hide()
            self.isszorzas=False
        elif self.isosztas:
            self.osztas.hide()
            self.isosztas=False
        elif self.iskaland:
            self.kaland.hide()
            self.iskaland=False

    def Show_Alapderivaltak(self):
        try:
            if self.openedalapderivaltak==True:
                self.alapderivaltak = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow2()
                self.ui.setupUi(self.alapderivaltak)
                self.ui.pushButton.clicked.connect(self.closeAlapderivaltak)
                self.alapderivaltak.show()
                self.isalapderivaltak=True
                self.fooldal.hide()
                print(Ui_MainWindow2.rightSolvedExercises)
            else:
                raise cl.FinishedChallange('alapderiváltak')

        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnAlapderivaltak)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(self.againButton1)
            msg.exec()


    def Show_Osszetett(self):
        try:
            if self.openedosszetett==True:
                self.osszetett = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow3()
                self.ui.setupUi(self.osszetett)
                self.ui.pushButton.clicked.connect(self.closeOsszetett)
                self.osszetett.show()
                self.isosszetett = True
                self.fooldal.hide()
            else:
                raise cl.FinishedChallange('összetett függvények')

        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnOsszetett)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(self.againButton2)
            msg.exec()


    def Show_Szorzas(self):
        try:
            if self.openedszorzas==True:
                self.szorzas = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow4()
                self.ui.setupUi(self.szorzas)
                self.ui.pushButton.clicked.connect(self.closeSzorzas)
                self.szorzas.show()
                self.isszorzas = True
                self.fooldal.hide()
            else:
                raise cl.FinishedChallange('szorzás')

        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnSzorzas)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(self.againButton3)
            msg.exec()


    def Show_Osztas(self):
        try:
            if self.openedosztas==True:
                self.osztas = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow5()
                self.ui.setupUi(self.osztas)
                self.ui.pushButton.clicked.connect(self.closeOsztas)
                self.osztas.show()
                self.isosztas = True
                self.fooldal.hide()
            else:
                raise cl.FinishedChallange('osztás')

        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnOsztas)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(self.againButton4)
            msg.exec()

    def Show_Kaland(self):
        try:
            if self.openedkaland==True:
                self.kaland = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow6()
                self.ui.setupUi(self.kaland)
                self.ui.pushButton.clicked.connect(self.closeKaland)
                self.kaland.show()
                self.iskaland = True
                self.fooldal.hide()
            else:
                raise cl.FinishedChallange('kaland')

        except cl.FinishedChallange as fc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Siker')
            msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(fc.__str__())
            closeBtn = msg.addButton('Kilépés', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnKaland)
            againBtn = msg.addButton('Újra', msg.ActionRole)
            againBtn.clicked.connect(self.againButton5)
            msg.exec()

    def exitBtnAlapderivaltak(self):
        if os.path.exists('database1.txt'):
            os.remove('database1.txt')
        Ui_MainWindow2.rightSolvedExercises=[]
        self.Show_Fooldal()


    def exitBtnOsszetett(self):
        if os.path.exists('database2.txt'):
            os.remove('database2.txt')
        Ui_MainWindow3.rightSolvedExercises=[]
        self.Show_Fooldal()

    def exitBtnSzorzas(self):
        if os.path.exists('database3.txt'):
            os.remove('database3.txt')
        Ui_MainWindow4.rightSolvedExercises=[]
        self.Show_Fooldal()

    def exitBtnOsztas(self):
        if os.path.exists('database4.txt'):
            os.remove('database4.txt')
        Ui_MainWindow5.rightSolvedExercises=[]
        self.Show_Fooldal()

    def exitBtnKaland(self):
        if os.path.exists('database5.txt'):
            os.remove('database5.txt')
        Ui_MainWindow6.rightSolvedExercises=[]
        self.Show_Fooldal()


    def closeAlapderivaltak(self):
        try:
            self.Show_Fooldal()
            raise cl.ClosingConfirmation('alapderiváltak')

        except cl.ClosingConfirmation as cc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Mentés')
            msg.setText(cc.__str__())
            closeBtn = msg.addButton('Nem', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnAlapderivaltak)
            saveBtn = msg.addButton('Igen', msg.ActionRole)
            saveBtn.clicked.connect(self.saveAlapderivaltak)
            msg.exec()

    def closeOsszetett(self):
        try:
            self.Show_Fooldal()
            raise cl.ClosingConfirmation('összetett függvények')
        except cl.ClosingConfirmation as cc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Mentés')
            #msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(cc.__str__())
            closeBtn = msg.addButton('Nem', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnOsszetett)
            saveBtn = msg.addButton('Igen', msg.ActionRole)
            saveBtn.clicked.connect(self.saveOsszetett)
            msg.exec()

    def closeSzorzas(self):
        try:
            self.Show_Fooldal()
            raise cl.ClosingConfirmation('szorzás')

        except cl.ClosingConfirmation as cc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Mentés')
            #msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(cc.__str__())
            closeBtn = msg.addButton('Nem', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnSzorzas)
            saveBtn = msg.addButton('Igen', msg.ActionRole)
            saveBtn.clicked.connect(self.saveSzorzas)
            msg.exec()

    def closeOsztas(self):
        try:
            self.Show_Fooldal()
            raise cl.ClosingConfirmation('osztás')

        except cl.ClosingConfirmation as cc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Mentés')
            #msg.setIconPixmap(QtGui.QPixmap(":/images/images/trophy.png"))
            msg.setText(cc.__str__())
            closeBtn = msg.addButton('Nem', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnOsztas)
            saveBtn = msg.addButton('Igen', msg.ActionRole)
            saveBtn.clicked.connect(self.saveOsztas)
            msg.exec()

    def closeKaland(self):
        try:
            self.Show_Fooldal()
            raise cl.ClosingConfirmation('kaland')

        except cl.ClosingConfirmation as cc:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Mentés')
            msg.setText(cc.__str__())
            closeBtn = msg.addButton('Nem', msg.ActionRole)
            closeBtn.clicked.connect(self.exitBtnKaland)
            saveBtn = msg.addButton('Igen', msg.ActionRole)
            saveBtn.clicked.connect(self.saveKaland)
            msg.exec()

    def againButton1(self):
        self.openedalapderivaltak = True
        Ui_MainWindow2.rightSolvedExercises=[]
        if os.path.exists('database1.txt'):
            os.remove('database1.txt')
        Controller.Show_Alapderivaltak()


    def againButton2(self):
        self.openedosszetett = True
        Ui_MainWindow3.rightSolvedExercises=[]
        if os.path.exists('database2.txt'):
            os.remove('database2.txt')
        Controller.Show_Osszetett()


    def againButton3(self):
        self.openedszorzas = True
        Ui_MainWindow4.rightSolvedExercises=[]
        if os.path.exists('database3.txt'):
            os.remove('database3.txt')
        Controller.Show_Szorzas()


    def againButton4(self):
        self.openedosztas = True
        Ui_MainWindow5.rightSolvedExercises=[]
        if os.path.exists('database4.txt'):
            os.remove('database4.txt')
        Controller.Show_Osztas()


    def againButton5(self):
        self.openedkaland = True
        Ui_MainWindow6.rightSolvedExercises=[]
        if os.path.exists('database5.txt'):
            os.remove('database5.txt')
        Controller.Show_Kaland()


    def values(self,function,xValues):
        "egy függvény x és y tengelyeinek értékét adja vissza"
        x = sym.symbols('x')
        xt =xValues
        yt = []

        for i in xt:
            f=sym.lambdify(x,function,modules=['numpy','sympy'])
            yt.append(f(i))
        return xt, yt

    def saveAlapderivaltak(self):
        exercises=Ui_MainWindow2.rightSolvedExercises
        db = open("database1.txt", "w")
        for i in exercises:
            print(i, file=db)
        exercises.clear()
        db.close()

    def loadAlapderivaltak(self):
        try:
            db = open('database1.txt', 'r')
            for i in db:
                i=i[:-1]
                Ui_MainWindow2.rightSolvedExercises.append(i)
            db.close()
        except FileNotFoundError:
            pass

    def saveOsszetett(self):
        exercises=Ui_MainWindow3.rightSolvedExercises
        db = open("database2.txt", "w")
        for i in exercises:
            print(i, file=db)
        exercises.clear()
        db.close()

    def loadOsszetett(self):
        try:
            db = open('database2.txt', 'r')
            for i in db:
                print(i)
                i=i[:-1]
                Ui_MainWindow3.rightSolvedExercises.append(i)
            db.close()
        except FileNotFoundError:
            pass

    def saveSzorzas(self):
        exercises=Ui_MainWindow4.rightSolvedExercises
        db = open("database3.txt", "w")
        for i in exercises:
            print(i, file=db)
        exercises.clear()
        db.close()

    def loadSzorzas(self):
        try:
            db = open('database3.txt', 'r')
            for i in db:
                print(i)
                i=i[:-1]
                Ui_MainWindow4.rightSolvedExercises.append(i)
            db.close()
        except FileNotFoundError:
            pass

    def saveOsztas(self):
        exercises=Ui_MainWindow5.rightSolvedExercises
        db = open("database4.txt", "w")
        for i in exercises:
            print(i, file=db)
        exercises.clear()
        db.close()

    def loadOsztas(self):
        try:
            db = open('database4.txt', 'r')
            for i in db:
                print(i)
                i=i[:-1]
                Ui_MainWindow5.rightSolvedExercises.append(i)
            db.close()
        except FileNotFoundError:
            pass

    def saveKaland(self):
        exercises=Ui_MainWindow6.rightSolvedExercises
        lvl=Ui_MainWindow6.bridgeLvl
        db = open("database5.txt", "w")
        for i in exercises:
            print(i, file=db)
        exercises.clear()
        db.close()

    def loadKaland(self):
        try:
            db = open('database5.txt', 'r')
            for i in db:
                print(i)
                i=i[:-1]
                Ui_MainWindow6.rightSolvedExercises.append(i)
                print(Ui_MainWindow6.rightSolvedExercises)
            db.close()
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_Fooldal()
    sys.exit(app.exec_())
