# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_test_end.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class TextTestEnd_Window(object):
    def setupUi(self, MainWindow, diseas_type, score, result):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 600))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.smile_lbl = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        sizePolicy.setHeightForWidth(self.smile_lbl.sizePolicy().hasHeightForWidth())
        self.smile_lbl.setSizePolicy(sizePolicy)
        self.smile_lbl.setMaximumSize(QtCore.QSize(500, 500))
        self.smile_lbl.setText("")
        
        self.smile_lbl.setScaledContents(True)
        self.smile_lbl.setObjectName("smile_lbl")
        self.gridLayout_2.addWidget(self.smile_lbl, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.result_lbl = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        sizePolicy.setHeightForWidth(self.result_lbl.sizePolicy().hasHeightForWidth())
        self.result_lbl.setSizePolicy(sizePolicy)
        self.result_lbl.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.result_lbl.setFont(font)
        self.result_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.result_lbl.setObjectName("result_lbl")
        self.gridLayout_3.addWidget(self.result_lbl, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.return_to_tests_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        sizePolicy.setHeightForWidth(self.return_to_tests_btn.sizePolicy().hasHeightForWidth())
        self.return_to_tests_btn.setSizePolicy(sizePolicy)
        self.return_to_tests_btn.setMaximumSize(QtCore.QSize(350, 60))
        self.return_to_tests_btn.clicked.connect(self.return_to_tests)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.return_to_tests_btn.setFont(font)
        self.return_to_tests_btn.setObjectName("return_to_tests_btn")
        self.gridLayout_4.addWidget(self.return_to_tests_btn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.test_result_set = [
        "In Your case the presence of {} is unlikely".format(diseas_type.lower()),
        "You have an average chance of having {}.".format(diseas_type.lower()),
        "You are more likely to have {}.".format(diseas_type.lower())
        ]


        if score in range(24,37) and diseas_type == "Dry Eye":
            self.result_lbl.setText(self.test_result_set[0])
            self.smile_lbl.setPixmap(QtGui.QPixmap("happy_smile.png"))
        elif score in range(13,24) and diseas_type == "Dry Eye":
            self.result_lbl.setText(self.test_result_set[1])
            self.smile_lbl.setPixmap(QtGui.QPixmap("neutral_smile.png"))
        elif score in range(13) and diseas_type == "Dry Eye":
            self.result_lbl.setText(self.test_result_set[2])
            self.smile_lbl.setPixmap(QtGui.QPixmap("sad_smile.png"))
        elif score in range(27,37) and diseas_type == "Accommodation":
            self.result_lbl.setText(self.test_result_set[0])
            self.smile_lbl.setPixmap(QtGui.QPixmap("happy_smile.png")) 
        elif score in range(19,27) and diseas_type == "Accommodation":
            self.result_lbl.setText(self.test_result_set[1])
            self.smile_lbl.setPixmap(QtGui.QPixmap("neutral_smile.png"))
        elif score in range(19) and diseas_type == "Accommodation":
            self.result_lbl.setText(self.test_result_set[2])
            self.smile_lbl.setPixmap(QtGui.QPixmap("sad_smile.png"))
        elif result == "In Your case the presence of astigmatism is unlikely" and diseas_type == "Astigmatism":
            self.result_lbl.setText(result)
            self.smile_lbl.setPixmap(QtGui.QPixmap("happy_smile.png"))
        elif result == "You are more likely to have astigmatism" and diseas_type == "Astigmatism":
            self.result_lbl.setText(result)
            self.smile_lbl.setPixmap(QtGui.QPixmap("sad_smile.png"))
        elif int(score) > 7 and diseas_type == "Color Blindness":
            self.result_lbl.setText("In Your case the presence of color blindness is unlikely")
            self.smile_lbl.setPixmap(QtGui.QPixmap("happy_smile.png"))
        elif int(score) <= 7 and diseas_type == "Color Blindness":
            self.result_lbl.setText("You are more likely to have color blindness")
            self.smile_lbl.setPixmap(QtGui.QPixmap("sad_smile.png"))
        elif result == "In Your case the presence of macular degeneration is unlikely" and diseas_type == "Macular Degeneration":
            self.result_lbl.setText(result)
            self.smile_lbl.setPixmap(QtGui.QPixmap("happy_smile.png"))
        elif result == "You are more likely to have macular degeneration" and diseas_type == "Macular Degeneration":
            self.result_lbl.setText(result)
            self.smile_lbl.setPixmap(QtGui.QPixmap("sad_smile.png"))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.result_lbl.setText(_translate("MainWindow", "In Your case the presence of dry eyes is unlikely"))
        self.return_to_tests_btn.setText(_translate("MainWindow", "Return to Tests"))

