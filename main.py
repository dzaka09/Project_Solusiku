import sys
from Resources_rc import resources_rc
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QStackedWidget, QDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

#import form form python
from Loading_screen.form_splash import Ui_Form_loading_screen
from Form_Login.formLogin import Ui_Form_login
from Form_Regist.formRegister import Ui_Form_Register
#from Form_buat_SecurityQuestion.form_make_SQuestion import Ui_form_buat_scr_question
#from Form_Security_Question.formSecr_question import Ui_Form_Security_QuestionR
#from Form_reset_pass.formRst_pw import Ui_form_resetPassword

#import message Box
from MessageBox_Anywhere.msgBox import Ui_msg_box
from MessageBox_Anywhere.msgWith_btnOk import Ui_msgBox_ok
from MessageBox_Anywhere.msgWith_btnYaTidak import Ui_msgBox_YaTdk 

#import database db_solusiku
from service.db import cek_username
        
#MessaageBox_without_btn
class messageBox(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_msg_box()
        self.ui.setupUi(self)
        
#MessageBox_WithBtnOk
class messBok_btnOk(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_msgBox_ok()
        self.ui.setupUi(self)
        
class messBok_btnYaTdk(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_msgBox_YaTdk()
        self.ui.setupUi(self)
      


#LOADING SCREEN
class MainApp(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.ui = Ui_Form_loading_screen()
        self.ui.setupUi(self)
        self.stacked = stacked
        
        #Splash_Show
        QTimer.singleShot(4000, self.open_Login)
    
    def open_Login(self):
        self.stacked.setCurrentIndex(1)
        self.stacked.setWindowTitle("LOGIN")
        self.stacked.setWindowIcon(QIcon(":/LogoAndWindowsIcon/Aset/LogoIconSolusiku-final.png"))
        self.stacked.setStyleSheet("Background-color: #ebebea;")
        
        
#FORM LOGIN  
class formLogin(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.ui = Ui_Form_login()
        self.ui.setupUi(self)
        
        self.stacked = stacked
        
        self.ui.txt_passwords.setEchoMode(QLineEdit.Password)
        self.ui.chk_show_Pw.stateChanged.connect(self.show_pw)
        self.ui.btn_to_Regist.clicked.connect(self.open_Register)
        
    #show / hide password
    def show_pw(self, state):
        if state == 2:
            self.ui.txt_passwords.setEchoMode(QLineEdit.Normal)
        else :
            self.ui.txt_passwords.setEchoMode(QLineEdit.Password)
            
    
    #open Register
    def open_Register(self):
        self.ui.txt_usernames.setText("")
        self.ui.txt_passwords.setText("")
        self.ui.txt_passwords.setEchoMode(QLineEdit.Password)
        self.ui.chk_show_Pw.setChecked(False)
        self.stacked.setCurrentIndex(2)
        self.stacked.setWindowTitle("REGISTER")
        self.stacked.setWindowIcon(QIcon(":/LogoAndWindowsIcon/Aset/LogoIconSolusiku-final.png"))
        self.stacked.setStyleSheet("Background-color: #ebebea;")
    
     
               
           
#FORM REGISTER
class formRegist(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.ui = Ui_Form_Register()
        self.ui.setupUi(self)
        
        #Inisialisasi stacked widget
        self.stacked = stacked
        #======
        self.ui.txt_password.setEchoMode(QLineEdit.Password)
        self.ui.chk_show_pw.stateChanged.connect(self.show_pw)
        
         #back to Login
        self.ui.btn_back.clicked.connect(self.back_Login)
        
        
        #item_cmbJenisPertanyaan
        self.ui.cmbBox_sec_qstion.addItem("Pilih pertanyaan keamanan..")
        self.ui.cmbBox_sec_qstion.addItem("Makanan Favorit")
        self.ui.cmbBox_sec_qstion.addItem("Hewan Pelihara")
        self.ui.cmbBox_sec_qstion.addItem("Guru Favorit")
        self.ui.cmbBox_sec_qstion.addItem("Cinta Pertama")
        self.ui.cmbBox_sec_qstion.addItem("Hobi")
        self.ui.cmbBox_sec_qstion.setCurrentIndex(0)
        
        #register
        self.ui.btn_register.clicked.connect(self.register_akun)
    
    #show / hide password
    def show_pw(self, state):
        if state == 2:
            self.ui.txt_password.setEchoMode(QLineEdit.Normal)
        else :
            self.ui.txt_password.setEchoMode(QLineEdit.Password)  
        
    
    
            
        
    def register_akun(self):
        username = self.ui.txt_username.text().strip()
        
        if len(username) < 3 or len(username) > 20:
            QMessageBox.warning(self, "Peringatan", "Username harus 3–20 karakter!")
            return
        
        if cek_username(username):
            QMessageBox.warning(self, "Peringatan", "Username telah digunakan!")
        else:
            QMessageBox.information(self, "Informasi","Username tersedia")
            
                
                
                
        """
        elif len(username) < 3 and len(password) < 8:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon Maaf!\nUsername hanya dapat memuat 3 - 20 karakter, serta Password hanya dapat memuat 8 - 16 karakter.")
            msgBox.exec_()
            return
        elif len(username) > 20 and len(password) > 16:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon Maaf!\nUsername hanya dapat memuat 3 - 20 karakter, serta Password hanya dapat memuat 8 - 16 karakter.")
            msgBox.exec_()
            return
        elif len(username) > 20 and len(password) < 8:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon Maaf!\nUsername hanya dapat memuat 3 - 20 karakter, serta Password hanya dapat memuat 8 - 16 karakter.")
            msgBox.exec_()
            return
        elif len(username) < 3 and len(password) > 16:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon Maaf!\nUsername hanya dapat memuat 3 - 20 karakter, serta Password hanya dapat memuat 8 - 16 karakter.")
            msgBox.exec_()
            return
        elif len(username) > 20 or len(username) < 3:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon Maaf!\nUsername hanya dapat memuat 3 - 20 karakter.")
            msgBox.exec_()
            return
        elif len(password) > 16 or len(password) < 8:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon Maaf!\nPassword hanya dapat memuat 8 - 16 karakter.")
            msgBox.exec_()
            return
        elif self.cekSec_question == 0:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon Maaf!\nAnda belum memilih pertanyaan keamanan.")
            msgBox.exec_()
            return
        """
        
        
            
    #back_to_Login
    def back_Login(self):
        self.ui.txt_username.setText("")
        self.ui.txt_password.setText("")
        self.ui.cmbBox_sec_qstion.setCurrentIndex(0)
        self.ui.chk_show_pw.setChecked(False)
        self.stacked.setCurrentIndex(1)
        self.stacked.setWindowTitle("LOGIN")
        self.stacked.setWindowIcon(QIcon(":/LogoAndWindowsIcon/Aset/LogoIconSolusiku-final.png"))
        self.stacked.setStyleSheet("Background-color: #ebebea;")
        
        
"""
#FORM MENJAWAB SEQURITY QUESTION
class formJawab_secQuestion(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_buat_scr_question()
        self.ui.setupUi(self)
        self.windowRegst = formRegist()
       
        
        if jenis_pertanyaan == "Makanan Favorit":
            self.ui.txt_Quest.setText(pertanyaan1)
        elif jenis_pertanyaan == "Hewan Pelihara":
            self.ui.txt_Quest.setText(pertanyaan2)
        elif jenis_pertanyaan == "Guru Favorit":
            self.ui.txt_Quest.setText(pertanyaan3)
        elif jenis_pertanyaan == "Cinta Pertama":
            self.ui.txt_Quest.setText(pertanyaan4)
        elif jenis_pertanyaan == "Hobi":
            self.ui.txt_Quest.setText(pertanyaan5)
        
            
        self.ui.btn_back.clicked.connect(self.open_Regist)
        
        self.ui.btn_identify.clicked.connect(self.save_db_solusiku)
        
    #Simpan Username, Password, Jawaban, Jenis_Pertanyaan ke database  
    def save_db_solusiku(self):
        username = self.usn
        password = self.psw
        jenis_pertanyaan = self.jenis_pertanyaan
        jwb_pertanyaan = self.ui.txt_answer.text()
        
        if len(jwb_pertanyaan) > 0 and len(jwb_pertanyaan) < 100:
            insert_register(username, password, jenis_pertanyaan, jwb_pertanyaan)
            msgBox_Ok.ui.LblKonten_isi.setText(f"Register Berhasil!\nSilahkan Login {username}!")
            msgBox_Ok.rejected.connect(self.tutup_messageBox_andgo_to_Login)
            msgBox_Ok.ui.btnOk.clicked.connect(self.tutup_messageBox_andgo_to_Login)
            msgBox_Ok.exec_()
        elif len(jwb_pertanyaan) == 0:
            msgBox_Ok.ui.LblJenisMsg.setText("Peringatan!")
            msgBox_Ok.ui.LblKonten_isi.setText(f"Register Gagal!\nMohon masukkan jawaban kamu {username}!")
            msgBox_Ok.ui.btnOk.clicked.connect(self.close_msgBox)
            msgBox_Ok.exec_()
            
    def close_msgBox(self):
        msgBox_Ok.hide()
    
    
    def tutup_messageBox_andgo_to_Login(self):
        self.windowRegst.ui.txt_username.setText("")
        self.windowRegst.ui.txt_password.setText("")
        self.windowRegst.ui.cmbBox_sec_qstion.setCurrentIndex(0)
        self.windowRegst.ui.chk_show_pw.setChecked(False)
        self.ui.txt_answer.setText("")
        self.ui.txt_Quest.setText("")
        msgBox_Ok.close()
        self.stacke
        
     #back_to_register   
    def open_Regist(self):
        self.hide()
        self.windowRegst.show()
    
        
class formJawabSec_question(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_Security_QuestionR()
        self.ui.setupUi(self)
        self.formLogin = formLogin
"""




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #Message Box
    msgBox = messageBox()
    msgBox_ok = messBok_btnOk()
    msgBox_YaTdk = messBok_btnYaTdk()
    
    #===
    stacked = QStackedWidget()
    #===
    
    windowloading = MainApp(stacked)
    login = formLogin(stacked)
    register = formRegist(stacked)
    
    #===
    stacked.addWidget(windowloading) #0
    stacked.addWidget(login) #1
    stacked.addWidget(register) #2
    #===
    
    
    
    stacked.setFixedSize(stacked.currentWidget().size())
    stacked.setCurrentIndex(0)
    stacked.setWindowTitle("Loading...")
    stacked.setWindowIcon(QIcon(":/LogoAndWindowsIcon/Aset/LogoIconSolusiku-final.png"))
    stacked.setStyleSheet("Background-color: #ebebea;")
    stacked.show()
    
    #Daftar Pertanyaan Security Question
    pertanyaan1 = "Apa makanan favoritmu dari kecil hingga saat ini ?"
    pertanyaan2 = "Hewan apa yang pertama kali kamu pelihara ?"
    pertanyaan3 = "Siapa nama guru favoritmu ketika kamu masih duduk dibangku sma atau smk ?"
    pertanyaan4 = "Siapa nama seseorang yang kamu cintai pertama kali ?"
    pertanyaan5 = "Apa hobi kamu ketika kamu masih duduk di bangku sma atau smk ?"
    
    sys.exit(app.exec_())