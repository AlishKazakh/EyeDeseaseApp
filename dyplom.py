import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from main_menu import Main_Window
from information_diseases_menu import Information_Window
from tests import Test_Window
from all_diseases_info import Diseases_Info_Window
from ishihara_test import IshiharaTest_Window
from text_test import TextTests
from text_test_end import TextTestEnd_Window
from test_instructions import Instruction_Window
from snellen_test import SnellenTest_Window
from astigmatism_test import AstigmatismTest_Window


class Main_Menu(QtWidgets.QMainWindow, Main_Window):
    def __init__(self):
        super(Main_Menu, self).__init__()
        self.setupUi(self)


    def disease_info(self):    
        #self.window = QtWidgets.QMainWindow()
        self.info_window = Diseases_Info() 
        self.hide()
        #self.info_window.show()

    def start_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.test_window = Tests() 
        self.hide()
        #self.info_window.show()    


class Tests(QtWidgets.QMainWindow, Test_Window):
    def __init__(self):
        super(Tests, self).__init__()
        self.setupUi(self)

    def astigmatism_instruction_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.astigmatism_instruction_window = TestInstructions("Astigmatism") 
        self.hide()
        #self.main_window.show()

    def color_blnd_instruction_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.color_blnd_instruction_window = TestInstructions("Color Blindness") 
        self.hide()
        #self.main_window.show()
        
    def macular_deg_instruction_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.macular_instruction_window = TestInstructions("Macular Degeneration") 
        self.hide()
        #self.main_window.show()

    def vis_acuity_instruction_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.vis_acuity_instruction_window = TestInstructions("Visual Acuity") 
        self.hide()
        #self.main_window.show()

    def dry_eye_instruction_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.dry_eye_instruction_window = TestInstructions("Dry Eye") 
        self.hide()
        #self.main_window.show()

    def accommodation_instruction_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.accommodation_instruction_window = TestInstructions("Accommodation") 
        self.hide()
        #self.main_window.show()    

    def start_color_blnd_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.color_blnd_test_window = IshiharaTest() 
        self.hide()
        #self.main_window.show()

    def start_snellen_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.snellen_test_window = SnellenTest() 
        self.hide()
        #self.main_window.show()

    def start_dry_eye_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.dry_eye_test_window = Text_Tests("Dry Eye") 
        self.hide()
        #self.main_window.show()

    def start_accommodation_test(self):    
        #self.window = QtWidgets.QMainWindow()
        self.accommodation_window = Text_Tests("Accommodation") 
        self.hide()
        #self.main_window.show()        

    def return_fun(self):    
        #self.window = QtWidgets.QMainWindow()
        self.main_window = Main_Menu() 
        self.hide()
        #self.main_window.show()


    
class Diseases_Info(QtWidgets.QMainWindow, Information_Window):
    def __init__(self):
        super(Diseases_Info, self).__init__()
        self.setupUi(self)

    def astigmatism_information(self):
        self.astig_inf_win = All_Diseases_Info("Astigmatism")
        self.hide()

    def color_blnd_information(self):
        self.color_blnd_inf_win = All_Diseases_Info("Color Blindness")
        self.hide()  

    def macular_degeneration_information(self):
        self.macular_deg_inf_win = All_Diseases_Info("Macular Degeneration")
        self.hide()  

    def dry_eye_information(self):
        self.dry_eye_inf_win = All_Diseases_Info("Dry Eye")
        self.hide()  
        
    def eye_accomodation_information(self):
        self.eye_accomodation_inf_win = All_Diseases_Info("Eye Accommodation")
        self.hide()                



    def return_fun(self):    
        #self.window = QtWidgets.QMainWindow()
        self.main_window = Main_Menu() 
        self.hide()
        #self.main_window.show()   


class All_Diseases_Info(QtWidgets.QMainWindow, Diseases_Info_Window):
    def __init__(self,diseas):
        super(All_Diseases_Info, self).__init__()
        self.setupUi(self,diseas)            
        
    def return_to_info(self):    
        #self.window = QtWidgets.QMainWindow()
        self.info_window = Diseases_Info() 
        self.hide()
        #self.info_window.show()    

class IshiharaTest(QtWidgets.QMainWindow, IshiharaTest_Window):
    def __init__(self,diseas):
        super(IshiharaTest, self).__init__()
        self.setupUi(self,diseas)       

    def image_test(self):
        
        sender = self.sender()
        
        if self.diseas == "Color Blindness":
            if sender.text() == self.random_question_answer_set[self.i][5]:
                self.score = self.score + 1
            self.result = ""
        elif self.diseas == "Macular Degeneration":
            if sender.text() == "All lines are the same":
                self.result = "In Your case the presence of macular degeneration is unlikely"
                #print(self.result)
            elif sender.text() != "All lines are the same":
                self.result = "You are more likely to have macular degeneration"
                #print(self.result)
        
        self.i = self.i + 1

        if self.i == len(self.random_question_answer_set) and self.diseas == "Color Blindness":
            self.test_window = TextTestEnd("Color Blindness", self.score, self.result) 
            self.hide() 
            self.i = 0
        elif self.i == len(self.random_question_answer_set) and self.diseas == "Macular Degeneration":
            self.test_window = TextTestEnd("Macular Degeneration", self.score, self.result) 
            self.hide() 
            self.i = 0
        

        
        if self.i < len(self.random_question_answer_set):
            self.ishihara_plate.setPixmap(QtGui.QPixmap((self.random_question_answer_set[self.i][0])))
            self.variant_a.setText(self.random_question_answer_set[self.i][1])
            self.variant_b.setText(self.random_question_answer_set[self.i][2])
            self.variant_c.setText(self.random_question_answer_set[self.i][3])
            self.variant_d.setText(self.random_question_answer_set[self.i][4])
            
        
    def return_to_tests(self):    
        #self.window = QtWidgets.QMainWindow()
        self.test_window = Tests() 
        self.hide()
        #self.info_window.show()  

class Text_Tests(QtWidgets.QMainWindow, TextTests):
    def __init__(self,diseas_type):
        super(Text_Tests, self).__init__()
        self.setupUi(self,diseas_type) 
        
    def dry_eye_test(self):
        
        sender = self.sender()
        
            
        if sender.text() == "Never":
            self.score = self.score + 4
        elif sender.text() == "Rare":
            self.score = self.score + 3
        elif sender.text() == "Sometimes":
            self.score = self.score + 2
        elif sender.text() == "Often":
            self.score = self.score + 1
        
        self.i = self.i + 1

        self.result = ""

        if self.i == len(self.random_dry_eye_questions_set) and self.diseas_type == "Dry Eye":
            self.test_window = TextTestEnd("Dry Eye", self.score, self.result) 
            self.hide() 
            self.i = 0
        elif self.i == len(self.random_accomodation_question_set) and self.diseas_type == "Accommodation":
            self.test_window = TextTestEnd("Accommodation", self.score, self.result) 
            self.hide() 
            self.i = 0

        
        if self.i < len(self.random_dry_eye_questions_set) and self.diseas_type == "Dry Eye":
            self.question.setText(self.random_dry_eye_questions_set[self.i])
        elif self.i < len(self.random_accomodation_question_set) and self.diseas_type == "Accommodation":
            self.question.setText(self.random_accomodation_question_set[self.i])
               
        
    def return_to_tests(self):    
        #self.window = QtWidgets.QMainWindow()
        self.test_window = Tests() 
        self.hide()
        #self.info_window.show() 

class TextTestEnd(QtWidgets.QMainWindow, TextTestEnd_Window):
    def __init__(self,diseas_type,score,result):
        super(TextTestEnd, self).__init__()
        self.setupUi(self,diseas_type,score, result)            
        
    def return_to_tests(self):    
        #self.window = QtWidgets.QMainWindow()
        self.test_window = Tests() 
        self.hide()
        #self.info_window.show()  

class TestInstructions(QtWidgets.QMainWindow, Instruction_Window):
    def __init__(self,diseas_type):
        super(TestInstructions, self).__init__()
        self.setupUi(self,diseas_type)            
    

    def start_test_after_instruction(self,diseas_type):
        if diseas_type == "Color Blindness":
            self.color_blnd_test_window = IshiharaTest("Color Blindness") 
            self.hide()            
        elif diseas_type == "Dry Eye":
            self.dry_eye_test_window = Text_Tests("Dry Eye") 
            self.hide()
        elif diseas_type == "Accommodation":
            self.dry_eye_test_window = Text_Tests("Accommodation") 
            self.hide()
        elif diseas_type == "Visual Acuity":
            self.snellen_test_window = SnellenTest() 
            self.hide()
        elif diseas_type == "Astigmatism":
            self.snellen_test_window = AstigmatismTest() 
            self.hide()
        elif diseas_type == "Macular Degeneration":
            self.color_blnd_test_window = IshiharaTest("Macular Degeneration") 
            self.hide() 


    def return_to_tests(self):    
        #self.window = QtWidgets.QMainWindow()
        self.test_window = Tests() 
        self.hide()
        #self.info_window.show()    


class SnellenTest(QtWidgets.QMainWindow, SnellenTest_Window):
    def __init__(self):
        super(SnellenTest, self).__init__()
        self.setupUi(self)       

    def visual_acuity_test(self):
        
        sender = self.sender()
        
            
        if sender.text() == self.random_question_answer_set[self.i][5]:
            self.score = self.score + 1
        
        self.i = self.i + 1
            
        if self.i == 1:
            font = QtGui.QFont()
            font.setFamily("Eyechart")
            font.setPointSize(37)
            self.letter_snellen.setFont(font)
        elif self.i == 2:
            font = QtGui.QFont()
            font.setFamily("Eyechart")
            font.setPointSize(25)
            self.letter_snellen.setFont(font)
        elif self.i == 3:
            font = QtGui.QFont()
            font.setFamily("Eyechart")
            font.setPointSize(19)
            self.letter_snellen.setFont(font)
        elif self.i == 4:
            font = QtGui.QFont()
            font.setFamily("Eyechart")
            font.setPointSize(15)
            self.letter_snellen.setFont(font)
        elif self.i == 5:
            font = QtGui.QFont()
            font.setFamily("Eyechart")
            font.setPointSize(12)
            self.letter_snellen.setFont(font)
        elif self.i == 6:
            font = QtGui.QFont()
            font.setFamily("Eyechart")
            font.setPointSize(9)
            self.letter_snellen.setFont(font)
        elif self.i == 7:
            font = QtGui.QFont()
            font.setFamily("Eyechart")
            font.setPointSize(7)
            self.letter_snellen.setFont(font)
        
        

        if self.i == len(self.random_question_answer_set):
            self.test_window = Tests() 
            self.hide() 
            self.i = 0
        

        
        if self.i < len(self.random_question_answer_set):
            self.letter_snellen.setText(self.random_question_answer_set[self.i][0])
            self.a_answer.setText(self.random_question_answer_set[self.i][1])
            self.b_answer.setText(self.random_question_answer_set[self.i][2])
            self.c_answer.setText(self.random_question_answer_set[self.i][3])
            self.d_answer.setText(self.random_question_answer_set[self.i][4])

        print(self.score)    
            
        
    def return_to_tests(self):    
        #self.window = QtWidgets.QMainWindow()
        self.test_window = Tests() 
        self.hide()
        #self.info_window.show() 

class AstigmatismTest(QtWidgets.QMainWindow, AstigmatismTest_Window):
    def __init__(self):
        super(AstigmatismTest, self).__init__()
        self.setupUi(self)       

    def astigmatism_test(self):
        
        sender = self.sender()

        self.score = 0

        if sender.text() == "All lines are the same":
            self.score_list.append("In Your case the presence of astigmatism is unlikely")
            #print(self.result)
        elif sender.text() != "All lines are the same":
            self.score_list.append("You are more likely to have astigmatism")

        if "You are more likely to have astigmatism" in self.score_list:
            self.result = "You are more likely to have astigmatism"
            #print(self.result)
        else:
            self.result = "In Your case the presence of astigmatism is unlikely"
        
        self.i = self.i + 1

        if self.i == len(self.astigmatism_question_answer_set):
            self.test_window = TextTestEnd("Astigmatism", self.score, self.result) 
            self.hide() 
            self.i = 0
        

        
        if self.i < len(self.astigmatism_question_answer_set):
            self.astigmatism_test_picture.setPixmap(QtGui.QPixmap((self.astigmatism_question_answer_set[self.i][0])))
            self.variant_a.setText(self.astigmatism_question_answer_set[self.i][1])
            self.variant_b.setText(self.astigmatism_question_answer_set[self.i][2])

            
            
        
    def return_to_tests(self):    
        #self.window = QtWidgets.QMainWindow()
        self.test_window = Tests() 
        self.hide()
        #self.info_window.show()                  


    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
    ui = Main_Menu()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
    sys.exit(app.exec())      