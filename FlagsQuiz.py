# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlagsQuiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#
# follow us on twitter @PY4ALL
#


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_score = QtWidgets.QLabel(self.centralwidget)
        self.label_score.setMinimumSize(QtCore.QSize(0, 16))
        self.label_score.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_score.setObjectName("label_score")
        self.horizontalLayout.addWidget(self.label_score)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("quiz.jpg"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.verticalLayout.addWidget(self.pushButton_next)
        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_start.clicked.connect(lambda:self.newQuiz())
        self.pushButton_next.clicked.connect(lambda:self.nextQuiz())
        self.pushButton_5.clicked.connect(lambda:self.whichbtn(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda:self.whichbtn(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda:self.whichbtn(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda:self.whichbtn(self.pushButton_8))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flags Quiz"))
        self.pushButton_start.setText(_translate("MainWindow", "Start/Restart Quiz"))
        self.label.setText(_translate("MainWindow", "Total Score:"))
        self.label_score.setText(_translate("MainWindow", "0"))
        self.pushButton_5.setText(_translate("MainWindow", "choice 1"))
        self.pushButton_6.setText(_translate("MainWindow", "choice 2"))
        self.pushButton_7.setText(_translate("MainWindow", "choice 3"))
        self.pushButton_8.setText(_translate("MainWindow", "choice 4"))
        self.pushButton_next.setText(_translate("MainWindow", "Next Question"))

        self.pushButton_5.setStyleSheet("background-color: white")
        self.pushButton_6.setStyleSheet("background-color: white")            
        self.pushButton_7.setStyleSheet("background-color: white")         
        self.pushButton_8.setStyleSheet("background-color: white")
        #self.pushButton_next.setStyleSheet("background-color: white")
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_next.setEnabled(False)

    def newQuiz(self):
        global i,score
        score = 0
        i = -1
        random.shuffle(flags_list)
        self.label_score.setText(str(score))
        self.pushButton_next.setEnabled(True)
        self.nextQuiz()

    def country_name(self,raw):
        return ''.join(x if x.isalpha() else ' ' for x in raw[5:].split('.')[0]).strip()

    def nextQuiz(self):
        global i,ans_list
        flags_list_range = [x for x in range(0,len(flags_list))]
        i = random.choice(flags_list_range)
        self.label_2.setPixmap(QtGui.QPixmap(flags_list[i]))
        ans_list = [i]
        flags_list_range.remove(ans_list[0])
        ans_list.append(random.choice(flags_list_range))
        flags_list_range.remove(ans_list[1])
        ans_list.append(random.choice(flags_list_range))
        flags_list_range.remove(ans_list[2])
        ans_list.append(random.choice(flags_list_range))
    
        random.shuffle(ans_list)
        self.pushButton_5.setText(self.country_name(flags_list[ans_list[0]]))
        self.pushButton_6.setText(self.country_name(flags_list[ans_list[1]]))
        self.pushButton_7.setText(self.country_name(flags_list[ans_list[2]]))
        self.pushButton_8.setText(self.country_name(flags_list[ans_list[3]]))

        self.pushButton_5.setStyleSheet("background-color: white")
        self.pushButton_6.setStyleSheet("background-color: white")            
        self.pushButton_7.setStyleSheet("background-color: white")         
        self.pushButton_8.setStyleSheet("background-color: white")
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_next.setEnabled(True)
        
    def whichbtn(self,b):
        global i, score
        if b.text() == self.country_name(flags_list[i]):
            score+=1
            self.label_score.setText(str(score))
        else:
            b.setStyleSheet("background-color: red")
            
        if self.pushButton_5.text()==self.country_name(flags_list[i]):
            self.pushButton_5.setStyleSheet("background-color: green")
        if self.pushButton_6.text()==self.country_name(flags_list[i]):
            self.pushButton_6.setStyleSheet("background-color: green")            
        if self.pushButton_7.text()==self.country_name(flags_list[i]):
            self.pushButton_7.setStyleSheet("background-color: green")         
        if self.pushButton_8.text()==self.country_name(flags_list[i]):
            self.pushButton_8.setStyleSheet("background-color: green")

        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
            
if __name__ == "__main__":
    import sys
    import glob

    global flags_list, countries_list
    flags_list = []
    flags_list.extend(glob.glob('data\*.svg'))
    flags_list.extend(glob.glob('data\*.png'))
    flags_list.extend(glob.glob('data\*.jpg'))
    flags_list.extend(glob.glob('data\*.jpge'))
    

    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
