# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ishihara_test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import ishihara_pic
import random


class IshiharaTest_Window(object):
	def setupUi(self, MainWindow, diseas):
		MainWindow.setObjectName("MainWindow")
		MainWindow.showFullScreen()

		self.diseas = diseas

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

		
		self.ishihara_plate = QtWidgets.QLabel(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.ishihara_plate.sizePolicy().hasHeightForWidth())
		self.ishihara_plate.setSizePolicy(sizePolicy)
		self.ishihara_plate.setMaximumSize(QtCore.QSize(600, 600))
		self.ishihara_plate.setText("")
		
		self.ishihara_plate.setScaledContents(True)
		self.ishihara_plate.setObjectName("ishihara_plate")
		self.gridLayout_4.addWidget(self.ishihara_plate, 0, 0, 1, 1)
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
		self.variant_a.setMaximumSize(QtCore.QSize(200, 40))
		self.variant_a.clicked.connect(self.image_test)
		self.variant_a.setObjectName("variant_a")
		self.gridLayout_2.addWidget(self.variant_a, 0, 0, 1, 1)


		self.variant_b = QtWidgets.QPushButton(self.frame_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.variant_b.sizePolicy().hasHeightForWidth())
		self.variant_b.setSizePolicy(sizePolicy)
		self.variant_b.setMaximumSize(QtCore.QSize(200, 40))
		self.variant_b.clicked.connect(self.image_test)
		self.variant_b.setObjectName("variant_b")
		self.gridLayout_2.addWidget(self.variant_b, 0, 1, 1, 1)


		self.variant_c = QtWidgets.QPushButton(self.frame_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.variant_c.sizePolicy().hasHeightForWidth())
		self.variant_c.setSizePolicy(sizePolicy)
		self.variant_c.setMaximumSize(QtCore.QSize(200, 40))
		self.variant_c.clicked.connect(self.image_test)
		self.variant_c.setObjectName("variant_c")
		self.gridLayout_2.addWidget(self.variant_c, 1, 0, 1, 1)


		self.variant_d = QtWidgets.QPushButton(self.frame_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.variant_d.sizePolicy().hasHeightForWidth())
		self.variant_d.setSizePolicy(sizePolicy)
		self.variant_d.setMaximumSize(QtCore.QSize(200, 40))
		self.variant_d.clicked.connect(self.image_test)
		self.variant_d.setObjectName("variant_d")
		self.gridLayout_2.addWidget(self.variant_d, 1, 1, 1, 1)


		self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
		self.gridLayout_6.addWidget(self.frame_5, 1, 0, 1, 1)
		self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 388, 18))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.i = 0
		self.score = 0

		if self.diseas == "Color Blindness":
			self.question_answer_set = [
			["10_ishihara.png","19","10","18","16","10"],
			["11_ishihara.png","11","41","17","14","11"],
			["12_ishihara.png","42","10","12","13","12"],
			["13_ishihara.png","12","10","18","13","13"],
			["14_ishihara.png","11","14","41","17","14"],
			["15_ishihara.png","16","45","75","15","15"],
			["16_ishihara.png","13","10","16","18","16"],
			["17_ishihara.png","71","17","11","14","17"],
			["18_ishihara.png","12","10","18","13","18"],
			["19_ishihara.png","12","10","18","19","19"],
			["20_ishihara.png","22","20","28","23","20"],
			["21_ishihara.png","24","12","21","27","21"],
			["24_ishihara.png","57","27","24","21","24"],
			["25_ishihara.png","26","25","55","28","25"],
			["26_ishihara.png","25","23","28","26","26"],
			["27_ishihara.png","27","25","24","21","27"],
			["28_ishihara.png","20","26","58","28","28"],
			["30_ishihara.png","36","30","68","38","30"],
			["31_ishihara.png","31","34","61","81","31"],
			["33_ishihara.png","33","30","36","66","33"],
			["34_ishihara.png","31","37","64","34","34"],
			["35_ishihara.png","65","30","36","35","35"],
			["36_ishihara.png","36","30","88","38","36"],
			["38_ishihara.png","32","30","38","36","38"],
			["40_ishihara.png","42","43","40","48","40"],
			["41_ishihara.png","42","41","47","71","41"],
			["44_ishihara.png","14","41","44","11","44"],
			["47_ishihara.png","47","44","41","74","47"],
			["48_ishihara.png","40","48","42","43","48"],
			["66_ishihara.png","63","66","88","33","66"],
			["77_ishihara.png","71","11","44","77","77"],
			["88_ishihara.png","33","00","88","66","88"]]

			self.random_question_answer_set = random.sample(self.question_answer_set,15)
		elif self.diseas == "Macular Degeneration":
			self.random_question_answer_set = [
			["amsler_grid.jpg","Lines are wavy or curved","Squares differ in size and shape","Lines are missing","All lines are the same"]]

		

		self.ishihara_plate.setPixmap(QtGui.QPixmap((self.random_question_answer_set[0][0])))
		self.variant_a.setText(self.random_question_answer_set[0][1])
		self.variant_b.setText(self.random_question_answer_set[0][2])
		self.variant_c.setText(self.random_question_answer_set[0][3])
		self.variant_d.setText(self.random_question_answer_set[0][4])  

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.end_test_btn.setText(_translate("MainWindow", "End Test"))
		#self.variant_a.setText(_translate("MainWindow", "12"))
		#self.variant_b.setText(_translate("MainWindow", "72"))
		#self.variant_c.setText(_translate("MainWindow", "42"))
		#self.variant_d.setText(_translate("MainWindow", "43"))



