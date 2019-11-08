import sys

from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,1600,800)
        self.setWindowTitle("Applikacja do badania wad wzroku")
        self.main_menu()
        self.show()


    def main_menu(self):
            print(self.height())
            print(self.width())
            self.start_test_btn = QtWidgets.QPushButton("Start Test",self)
            self.start_test_btn.setGeometry(700,250,200,50)
            self.start_test_btn.clicked.connect(self.start_test)
            self.information_btn = QtWidgets.QPushButton("Information about Diseases",self)
            self.information_btn.setGeometry(700,350,200,50)
            self.information_btn.clicked.connect(self.disease_info)
            self.exit_btn = QtWidgets.QPushButton("Exit",self)
            self.exit_btn.setGeometry(700,450,200,50)   
            self.exit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit) 

    def start_test(self):
        self.test_window = Test()
        self.test_window.showMaximized()
        self.setGeometry(100,100,1600,800)
        self.show()
        self.close()

    def disease_info(self):
        self.info_window = InformationWindow()
        self.info_window.showMaximized()
        self.setGeometry(100,100,1600,800)
        self.show()
        self.close()


    
class Test(QtWidgets.QMainWindow):
    

    def __init__(self):
        super(Test, self).__init__()
        self.setGeometry(100,100,1600,800)
        self.setWindowTitle("Applikacja do badania wad wzroku")
        self.tests()
        self.show()

    def tests(self):
            self.choose_test = QtWidgets.QLabel("Choose the test",self)
            self.choose_test.setGeometry(650,100,300,50)
            self.astigmatism_btn = QtWidgets.QPushButton("Astigmatism Test",self)
            self.astigmatism_btn.setGeometry(700,250,200,50)
            self.color_blindness_btn = QtWidgets.QPushButton("Color Blindness Test",self)
            self.color_blindness_btn.setGeometry(700,350,200,50)
            self.acuity_btn = QtWidgets.QPushButton("Visual Acuity Test",self)
            self.acuity_btn.setGeometry(700,450,200,50)   
            self.maculodystrophy_btn = QtWidgets.QPushButton("Maculodystrophy Test",self)
            self.maculodystrophy_btn.setGeometry(700,550,200,50) 
            self.return_btn = QtWidgets.QPushButton("Return",self)
            self.return_btn.setGeometry(700,650,200,50) 
            self.return_btn.clicked.connect(self.return_fun)

    def return_fun(self):
            self.main_menu = Window()
            self.main_menu.showMaximized()
            self.setGeometry(100,100,1600,800)
            self.show()
            self.close()       

class InformationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(InformationWindow, self).__init__()
        self.setGeometry(100,100,1600,800)
        self.setWindowTitle("Applikacja do badania wad wzroku")
        self.info()
        self.show()

    def info(self):
        self.astigmatism_btn = QtWidgets.QPushButton("Astigmatism",self)
        self.astigmatism_btn.setGeometry(700,250,200,50)
        self.color_blindness_btn = QtWidgets.QPushButton("Color Blindness",self) 
        self.color_blindness_btn.setGeometry(700,350,200,50)   
        self.maculodystrophy_btn = QtWidgets.QPushButton("Maculodystrophy",self)
        self.maculodystrophy_btn.setGeometry(700,450,200,50) 
        self.return_btn = QtWidgets.QPushButton("Return",self)
        self.return_btn.setGeometry(700,550,200,50) 
        self.return_btn.clicked.connect(self.return_fun)

    def return_fun(self):
            self.main_menu = Window()
            self.main_menu.showMaximized()
            self.setGeometry(100,100,1600,800)
            self.show()
            self.close()  
        
    


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    gui.showMaximized()
    sys.exit(app.exec_())
    

run()        