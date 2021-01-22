# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'astigmatism_test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class AstigmatismTest_Window(object):
	def setupUi(self, MainWindow):
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
		self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
		self.gridLayout_6.setObjectName("gridLayout_6")
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
		self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
		self.gridLayout_3.setObjectName("gridLayout_3")


		self.end_test_btn = QtWidgets.QPushButton(self.frame_4)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.end_test_btn.sizePolicy().hasHeightForWidth())
		self.end_test_btn.setSizePolicy(sizePolicy)
		self.end_test_btn.setMaximumSize(QtCore.QSize(150, 60))
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


		self.astigmatism_test_picture = QtWidgets.QLabel(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.astigmatism_test_picture.sizePolicy().hasHeightForWidth())
		self.astigmatism_test_picture.setSizePolicy(sizePolicy)
		self.astigmatism_test_picture.setMaximumSize(QtCore.QSize(600, 600))
		font = QtGui.QFont()
		font.setPointSize(20)
		self.astigmatism_test_picture.setFont(font)
		self.astigmatism_test_picture.setText("")
		self.astigmatism_test_picture.setTextFormat(QtCore.Qt.AutoText)
		self.astigmatism_test_picture.setScaledContents(True)
		self.astigmatism_test_picture.setAlignment(QtCore.Qt.AlignCenter)
		self.astigmatism_test_picture.setObjectName("astigmatism_test_picture")
		self.gridLayout_4.addWidget(self.astigmatism_test_picture, 0, 0, 1, 1)


		self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)
		self.frame_2 = QtWidgets.QFrame(self.frame_5)
		self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
		self.gridLayout_2.setObjectName("gridLayout_2")


		self.variant_b = QtWidgets.QPushButton(self.frame_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.variant_b.sizePolicy().hasHeightForWidth())
		self.variant_b.setSizePolicy(sizePolicy)
		self.variant_b.setMaximumSize(QtCore.QSize(350, 70))
		self.variant_b.clicked.connect(self.astigmatism_test)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.variant_b.setFont(font)
		self.variant_b.setObjectName("variant_b")
		self.gridLayout_2.addWidget(self.variant_b, 0, 1, 1, 1)


		self.variant_a = QtWidgets.QPushButton(self.frame_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.variant_a.sizePolicy().hasHeightForWidth())
		self.variant_a.setSizePolicy(sizePolicy)
		self.variant_a.setMaximumSize(QtCore.QSize(350, 70))
		self.variant_a.clicked.connect(self.astigmatism_test)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.variant_a.setFont(font)
		self.variant_a.setObjectName("variant_a")
		self.gridLayout_2.addWidget(self.variant_a, 0, 0, 1, 1)


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

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.i = 0
		self.score_list = []

		self.astigmatism_question_answer_set = [
		["astigmatism_1.jpg","Presence of blurred lines","All lines are the same"],
		["astigmatism_2.png","Presence of blurred lines","All lines are the same"]]
		self.astigmatism_test_picture.setPixmap(QtGui.QPixmap((self.astigmatism_question_answer_set[0][0])))
		self.variant_a.setText(self.astigmatism_question_answer_set[0][1])
		self.variant_b.setText(self.astigmatism_question_answer_set[0][2])

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.end_test_btn.setText(_translate("MainWindow", "End Test"))





