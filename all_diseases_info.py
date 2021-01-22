# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color_blnd_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Diseases_Info_Window(object):
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
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
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
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
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
        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)
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
        elif diseas == "Macular Degeneration":
            self.plainTextEdit.setPlainText("Macular degeneration, also known as age-related macular degeneration (AMD or ARMD), is a medical condition which may result in blurred or no vision in the center of the visual field. Early on there are often no symptoms. Over time, however, some people experience a gradual worsening of vision that may affect one or both eyes. While it does not result in complete blindness, loss of central vision can make it hard to recognize faces, drive, read, or perform other activities of daily life. Visual hallucinations may also occur but these do not represent a mental illness.\n"
"\n"
"Macular degeneration typically occurs in older people. Genetic factors and smoking also play a role. It is due to damage to the macula of the retina. Diagnosis is by a complete eye exam. The severity is divided into early, intermediate, and late types. The late type is additionally divided into 'dry' and 'wet' forms with the dry form making up 90% of cases.\n")

        elif diseas == "Dry Eye":
            self.plainTextEdit.setPlainText("Dry eye syndrome (DES), also known as keratoconjunctivitis sicca (KCS), is the condition of having dry eyes. Other associated symptoms include irritation, redness, discharge, and easily fatigued eyes. Blurred vision may also occur. The symptoms can range from mild and occasional to severe and continuous. Scarring of the cornea may occur in some cases without treatment.\n"
"\n"
"Dry eye occurs when either the eye does not produce enough tears or when the tears evaporate too quickly. This can result from contact lens use, meibomian gland dysfunction, allergies, pregnancy, Sjögren syndrome, vitamin A deficiency, LASIK surgery, and certain medications such as antihistamines, some blood pressure medication, hormone replacement therapy, and antidepressants. Chronic conjunctivitis such as from tobacco smoke exposure or infection may also lead to the condition. Diagnosis is mostly based on the symptoms, though a number of other tests may be used.\n"
"\n"
"Treatment depends on the underlying cause. Artificial tears are the usual first line treatment. Wrap around glasses that fit close to the face may decrease tear evaporation. Stopping or changing certain medications may help. The medication ciclosporin or steroid eye drops may be used in some cases. Another option is lacrimal plugs that prevent tears from draining from the surface of the eye. Dry eye syndrome occasionally makes wearing contact lenses impossible.\n")

        elif diseas == "Eye Accommodation":
            self.plainTextEdit.setPlainText("Accommodation is the process by which the vertebrate eye changes optical power to maintain a clear image or focus on an object as its distance varies. In this, distances vary for individuals from the far point—the maximum distance from the eye for which a clear image of an object can be seen, to the near point—the minimum distance for a clear image. Accommodation usually acts like a reflex, including as part of the accommodation-vergence reflex, but it can also be consciously controlled. Mammals, birds and reptiles vary the optical power by changing the form of the elastic lens using the ciliary body (in humans up to 15 dioptres). Fish and amphibians vary the power by changing the distance between a rigid lens and the retina with muscles.\n"
"\n"
"The young human eye can change focus from distance (infinity) to as near as 6.5 cm from the eye. This dramatic change in focal power of the eye of approximately 15 dioptres (the reciprocal of focal length in metres) occurs as a consequence of a reduction in zonular tension induced by ciliary muscle contraction. This process can occur in as little as 224 ± 30 milliseconds in bright light. The amplitude of accommodation declines with age. By the fifth decade of life the accommodative amplitude can decline so that the near point of the eye is more remote than the reading distance. When this occurs the patient is presbyopic. Once presbyopia occurs, those who are emmetropic (do not require optical correction for distance vision) will need an optical aid for near vision; those who are myopic (nearsighted and require an optical correction for distance vision), will find that they see better at near without their distance correction; and those who are hyperopic (farsighted) will find that they may need a correction for both distance and near vision. Note that these effects are most noticeable when the pupil is large; i.e. in dim light. The age-related decline in accommodation occurs almost universally to less than 2 dioptres by the time a person reaches 45 to 50 years, by which time most of the population will have noticed a decrease in their ability to focus on close objects and hence require glasses for reading or bifocal lenses. Accommodation decreases to about 1 dioptre at the age of 70 years. The dependency of accommodation amplitude on age is graphically summarized by Duane's classical curves.\n")

        else:
            self.plainTextEdit.setPlainText(" ") 


        self.gridLayout_5.addWidget(self.frame_3, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 80))
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
        self.pushButton.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton.clicked.connect(self.return_to_info)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 1, 1, 1)


        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 1, 0, 1, 1)
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
#         self.label.setText(_translate("MainWindow", "Astigmatism"))
#         self.plainTextEdit.setPlainText(_translate("MainWindow", "Astigmatism is a type of refractive error in which the eye does not focus light evenly on the retina. This results in distorted or blurred vision at any distance. Other symptoms can include eyestrain, headaches, and trouble driving at night. If it occurs in early life, it can later result in amblyopia.\n"
# "\n"
# "The cause of astigmatism is unclear, however it is believed to be partly related to genetic factors. The underlying mechanism involves an irregular curvature of the cornea or abnormalities in the lens of the eye. Diagnosis is by an eye examination.\n"
# "\n"
# "Three treatment options are available: glasses, contact lenses, and surgery. Glasses are the simplest. Contact lenses can provide a wider field of vision. Refractive surgery permanently changes the shape of the eye.\n"
# "\n"
# "In Europe and Asia, astigmatism affects between 30 and 60% of adults. People of all ages can be affected by astigmatism. Astigmatism was first reported by Thomas Young in 1801."))
        self.pushButton.setText(_translate("MainWindow", "Return"))


