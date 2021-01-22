# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snellen_test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random

class SnellenTest_Window(object):
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
		self.frame_5 = QtWidgets.QFrame(self.frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
		self.frame_5.setSizePolicy(sizePolicy)
		self.frame_5.setMaximumSize(QtCore.QSize(16777215, 300))
		self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_5.setObjectName("frame_5")
		self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
		self.gridLayout_5.setObjectName("gridLayout_5")


		self.return_btn = QtWidgets.QPushButton(self.frame_5)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.return_btn.sizePolicy().hasHeightForWidth())
		self.return_btn.setSizePolicy(sizePolicy)
		self.return_btn.setMaximumSize(QtCore.QSize(250, 40))
		self.return_btn.clicked.connect(self.return_to_tests)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.return_btn.setFont(font)
		self.return_btn.setObjectName("return_btn")
		self.gridLayout_5.addWidget(self.return_btn, 0, 0, 1, 1)


		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
		self.gridLayout_6.addWidget(self.frame_5, 0, 0, 1, 1)
		self.frame_4 = QtWidgets.QFrame(self.frame)
		self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_4.setObjectName("frame_4")
		self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
		self.gridLayout_4.setObjectName("gridLayout_4")
		self.frame_2 = QtWidgets.QFrame(self.frame_4)
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


		self.letter_snellen = QtWidgets.QLabel(self.frame_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.letter_snellen.sizePolicy().hasHeightForWidth())
		self.letter_snellen.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Eyechart")
		font.setPointSize(75)
		self.letter_snellen.setFont(font)
		self.letter_snellen.setAlignment(QtCore.Qt.AlignCenter)
		self.letter_snellen.setObjectName("letter_snellen")
		self.gridLayout_2.addWidget(self.letter_snellen, 0, 0, 1, 1)


		self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
		self.frame_3 = QtWidgets.QFrame(self.frame_4)
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
		self.gridLayout_3.setObjectName("gridLayout_3")


		self.a_answer = QtWidgets.QPushButton(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.a_answer.sizePolicy().hasHeightForWidth())
		self.a_answer.setSizePolicy(sizePolicy)
		self.a_answer.setMaximumSize(QtCore.QSize(450, 70))
		self.a_answer.clicked.connect(self.visual_acuity_test)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.a_answer.setFont(font)
		self.a_answer.setObjectName("a_answer")
		self.gridLayout_3.addWidget(self.a_answer, 0, 0, 1, 1)


		self.b_answer = QtWidgets.QPushButton(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.b_answer.sizePolicy().hasHeightForWidth())
		self.b_answer.setSizePolicy(sizePolicy)
		self.b_answer.setMaximumSize(QtCore.QSize(450, 70))
		self.b_answer.clicked.connect(self.visual_acuity_test)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.b_answer.setFont(font)
		self.b_answer.setObjectName("b_answer")
		self.gridLayout_3.addWidget(self.b_answer, 0, 1, 1, 1)


		self.c_answer = QtWidgets.QPushButton(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.c_answer.sizePolicy().hasHeightForWidth())
		self.c_answer.setSizePolicy(sizePolicy)
		self.c_answer.setMaximumSize(QtCore.QSize(450, 70))
		self.c_answer.clicked.connect(self.visual_acuity_test)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.c_answer.setFont(font)
		self.c_answer.setObjectName("c_answer")
		self.gridLayout_3.addWidget(self.c_answer, 1, 0, 1, 1)


		self.d_answer = QtWidgets.QPushButton(self.frame_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.d_answer.sizePolicy().hasHeightForWidth())
		self.d_answer.setSizePolicy(sizePolicy)
		self.d_answer.setMaximumSize(QtCore.QSize(450, 70))
		self.d_answer.clicked.connect(self.visual_acuity_test)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.d_answer.setFont(font)
		self.d_answer.setObjectName("d_answer")
		self.gridLayout_3.addWidget(self.d_answer, 1, 1, 1, 1)


		self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)
		self.gridLayout_6.addWidget(self.frame_4, 1, 0, 1, 1)
		self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 18))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.i = 0
		self.score = 0

		self.question_answer_set = [
		["E","F","L","E","P","E"],
		["F","F","L","E","P","F"],
		["O","C","O","D","P","O"],
		["C","C","O","D","P","C"],
		["T","F","L","I","T","T"],
		["Z","F","L","N","Z","Z"],
		["P","F","R","D","P","P"],
		["D","O","D","C","P","D"],
		["L","F","L","E","I","L"],
		["N","F","L","N","Z","N"]]
		
		

		self.random_question_answer_set = random.sample(self.question_answer_set,8)
		self.letter_snellen.setText(self.random_question_answer_set[0][0])
		self.a_answer.setText(self.random_question_answer_set[0][1])
		self.b_answer.setText(self.random_question_answer_set[0][2])
		self.c_answer.setText(self.random_question_answer_set[0][3])
		self.d_answer.setText(self.random_question_answer_set[0][4])

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.return_btn.setText(_translate("MainWindow", "Return"))
		
		


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())