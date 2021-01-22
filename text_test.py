# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class TextTests(object):
    def setupUi(self, MainWindow,diseas_type):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()

        self.dry_eye_questions_set = [
            "How often do you feel the presence of a foreign object in your eye?",
            "Are your eyes sensitive to wind, computer screen, and heaters?",
            "How often do you feel pain in your eyes?",
            "How often do your eyes water?",
            "How often do you have red eyes?",
            "How often do you blink?",
            "How often do you observe blurred vision?",
            "How often do you feel the tension in your eyes?",
            "How often do you observe itching in your eyes?"
        ]

        self.random_dry_eye_questions_set = random.sample(self.dry_eye_questions_set,9)


        self.accomodation_question_set = [
            "Is it difficult for you to concentrate while reading/working at the computer?",
            "Do your eyes tire quickly?",
            "Does your vision fluctuate during the day?",
            "Does your vision deteriorate after working with a computer?",
            "Do you sometimes bleed for no particular reason?",
            "Do you have red eyes?",
            "Did your vision become slightly blurred/double?",
            "Do you experience pain in the brow area?",
            "Do you have pain in your eyes?"
        ]

        self.random_accomodation_question_set = random.sample(self.accomodation_question_set,9)

        self.diseas_type = diseas_type
        self.score = 0
        self.i = 0
        

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.end_test_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        sizePolicy.setHeightForWidth(self.end_test_btn.sizePolicy().hasHeightForWidth())
        self.end_test_btn.setSizePolicy(sizePolicy)
        self.end_test_btn.setMaximumSize(QtCore.QSize(150, 40))
        self.end_test_btn.clicked.connect(self.return_to_tests)
        self.end_test_btn.setObjectName("end_test_btn")
        self.gridLayout_3.addWidget(self.end_test_btn, 0, 0, 1, 1)


        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.question = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setMaximumSize(QtCore.QSize(1200, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.question.setFont(font)
        self.question.setTextFormat(QtCore.Qt.AutoText)
        self.question.setScaledContents(False)
        self.question.setAlignment(QtCore.Qt.AlignCenter)
        self.question.setObjectName("question")
        self.gridLayout_4.addWidget(self.question, 0, 0, 1, 1)
        if self.diseas_type == "Dry Eye":
            self.question.setText(self.random_dry_eye_questions_set[self.i])
        elif self.diseas_type == "Accommodation":
            self.question.setText(self.random_accomodation_question_set[self.i])    


        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.variant_a = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        sizePolicy.setHeightForWidth(self.variant_a.sizePolicy().hasHeightForWidth())
        self.variant_a.setSizePolicy(sizePolicy)
        self.variant_a.setMaximumSize(QtCore.QSize(350, 50))
        self.variant_a.clicked.connect(self.dry_eye_test)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.variant_a.setFont(font)
        self.variant_a.setObjectName("variant_a")
        self.gridLayout_2.addWidget(self.variant_a, 0, 0, 1, 1)


        self.variant_b = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variant_b.sizePolicy().hasHeightForWidth())
        self.variant_b.setSizePolicy(sizePolicy)
        self.variant_b.setMaximumSize(QtCore.QSize(350, 50))
        self.variant_b.clicked.connect(self.dry_eye_test)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.variant_b.setFont(font)
        self.variant_b.setObjectName("variant_b")
        self.gridLayout_2.addWidget(self.variant_b, 0, 1, 1, 1)


        self.variant_c = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variant_c.sizePolicy().hasHeightForWidth())
        self.variant_c.setSizePolicy(sizePolicy)
        self.variant_c.setMaximumSize(QtCore.QSize(350, 50))
        self.variant_c.clicked.connect(self.dry_eye_test)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.variant_c.setFont(font)
        self.variant_c.setObjectName("variant_c")
        self.gridLayout_2.addWidget(self.variant_c, 1, 0, 1, 1)


        self.variant_d = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variant_d.sizePolicy().hasHeightForWidth())
        self.variant_d.setSizePolicy(sizePolicy)
        self.variant_d.setMaximumSize(QtCore.QSize(350, 50))
        self.variant_d.clicked.connect(self.dry_eye_test)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.variant_d.setFont(font)
        self.variant_d.setObjectName("variant_d")
        self.gridLayout_2.addWidget(self.variant_d, 1, 1, 1, 1)

            
        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

            

        #self.question.setText(self.dry_eye_questions_set[0])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

        print(self.i)    



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.end_test_btn.setText(_translate("MainWindow", "End Test"))
        #self.question.setText(_translate("MainWindow", "How often do You observe itching in Your eyes?"))
        self.variant_a.setText(_translate("MainWindow", "Never"))
        self.variant_b.setText(_translate("MainWindow", "Rare"))
        self.variant_c.setText(_translate("MainWindow", "Sometimes"))
        self.variant_d.setText(_translate("MainWindow", "Often"))

    

        
        #print(self.score) 






