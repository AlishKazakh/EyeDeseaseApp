# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color_blnd_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class AstigmatismInfo_Window(object):
    def setupUi(self, MainWindow,diseas):
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
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label.setText(diseas)

        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setTabStopWidth(80)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        if diseas == "Color Blindness":
            self.plainTextEdit.setPlainText("Color blindness, also known as color vision deficiency, is the decreased ability to see color or differences in color. Simple tasks such as selecting ripe fruit, choosing clothing, and reading traffic lights can be more challenging. Color blindness may also make some educational activities more difficult. However, problems are generally minor, and most people find that they can adapt. People with total color blindness (achromatopsia) may also have decreased visual acuity and be uncomfortable in bright environments.\n"
"\n"
"The most common cause of color blindness is an inherited problem in the development of one or more of the three sets of color-sensing cones in the eye. Males are more likely to be color blind than females, as the genes responsible for the most common forms of color blindness are on the X chromosome. As females have two X chromosomes, a defect in one is typically compensated for by the other, therefore females can be carriers. Males only have one X chromosome and therefore express the genetic disorder. Color blindness can also result from physical or chemical damage to the eye, optic nerve or parts of the brain. Diagnosis is typically with the Ishihara color test; however, a number of other testing methods, including genetic testing, also exist.\n")
        elif diseas == "Astigmatism":
            self.plainTextEdit.setPlainText("Astigmatism is a type of refractive error in which the eye does not focus light evenly on the retina. This results in distorted or blurred vision at any distance. Other symptoms can include eyestrain, headaches, and trouble driving at night. If it occurs in early life, it can later result in amblyopia.\n"
"\n"
"The cause of astigmatism is unclear, however it is believed to be partly related to genetic factors. The underlying mechanism involves an irregular curvature of the cornea or abnormalities in the lens of the eye. Diagnosis is by an eye examination.\n"
"\n"
"Three treatment options are available: glasses, contact lenses, and surgery. Glasses are the simplest. Contact lenses can provide a wider field of vision. Refractive surgery permanently changes the shape of the eye.\n"
"\n"
"In Europe and Asia, astigmatism affects between 30 and 60% of adults. People of all ages can be affected by astigmatism. Astigmatism was first reported by Thomas Young in 1801.")
        else:
            self.plainTextEdit.setPlainText(" ")    

        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 20))
        self.pushButton.clicked.connect(self.return_to_info)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.label.setText(_translate("MainWindow", "Astigmatism"))
#         self.plainTextEdit.setPlainText(_translate("MainWindow", "Astigmatism is a type of refractive error in which the eye does not focus light evenly on the retina. This results in distorted or blurred vision at any distance. Other symptoms can include eyestrain, headaches, and trouble driving at night. If it occurs in early life, it can later result in amblyopia.\n"
# "\n"
# "The cause of astigmatism is unclear, however it is believed to be partly related to genetic factors. The underlying mechanism involves an irregular curvature of the cornea or abnormalities in the lens of the eye. Diagnosis is by an eye examination.\n"
# "\n"
# "Three treatment options are available: glasses, contact lenses, and surgery. Glasses are the simplest. Contact lenses can provide a wider field of vision. Refractive surgery permanently changes the shape of the eye.\n"
# "\n"
# "In Europe and Asia, astigmatism affects between 30 and 60% of adults. People of all ages can be affected by astigmatism. Astigmatism was first reported by Thomas Young in 1801."))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


часто ли ты чувствуешь наличие инородного объекта в глазу?  How often do you feel the presence of a foreign object in your eye?
чувствительны ли твои глаза к ветру, экрану компьютера и обогревателям?   Are your eyes sensitive to wind, computer screen, and heaters?
часто ли ты чувствуешь боль в глазах?         How often do you feel pain in your eyes?
у тебя часто слезятся глаза?                  How often do your eyes water?
часто ли у тебя бывает покраснение глаз?      How often do you have red eyes?
достаточно ли ты моргаешь?                    How often do you blink?
часто ли ты наблюдаешь размытость зрения?     How often do you observe blurred vision?
часто ли ты чувствуешь напряженность глаз?    How often do you feel the tension in your eyes?
часто ли ты наблюдаешь зуд в глазах?          How often do you observe itching in your eyes?

ты часто наблюдаешь жжение в глазах?
часто ли ты чувствуешь дискомфорт в глазах?
чувствительны ли твои глаза к свету?





сложно ли тебе сконцентрироваться во время чтения/работы за компьютером?
быстро ли утомляются твои глаза?
колеблется ли твое зрение в течение дня?
ухудшается ли твое зрение после работы с компьютером?
бывает ли у тебя слезоточение без особых на то причин?
бывает ли у тебя покраснение глаз?
стало ли твое зрение вблизь слегка размытым/двоящимся?
возникают ли у тебя боли в надбровной области?
возникают ли у тебя боли в глазах?


is it difficult for you to concentrate while reading/working at the computer?
do your eyes tire quickly?
does your vision fluctuate during the day?
does your vision deteriorate after working with a computer?
do you sometimes bleed for no particular reason?
do you have red eyes?
did your vision become slightly blurred/double?
do you experience pain in the brow area?
do you have pain in your eyes?



У тебя средняя вероятность наличия сухости глаз.
У тебя большая вероятность наличия сухости глаз.
В твоем случае наличие спазма аккомодации маловероятно.
У тебя средняя вероятность наличия спазма аккомодации.
У тебя большая вероятность наличия спазма аккомодации. 

You have an average chance of having dry eyes.
You are more likely to have dry eyes.
In your case, the presence of a spasm of accommodation is unlikely.
You have an average chance of having an accommodation spasm.
You're more likely to have an accommodation spasm.

300/6.94


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())