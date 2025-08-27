import sys
from Resources_rc import resources_rc
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QStackedWidget, QDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, pyqtSignal

#import form form python
from MessageBox_Anywhere.Empty_form import Ui_Form_Empty
from Loading_screen.form_splash import Ui_Form_loading_screen
from Form_Login.formLogin import Ui_Form_login
from Form_Regist.formRegister import Ui_Form_Register
from Form_buat_SecurityQuestion.form_make_SQuestion import Ui_form_buat_scr_question
#from Form_Security_Question.formSecr_question import Ui_Form_Security_QuestionR
#from Form_reset_pass.formRst_pw import Ui_form_resetPassword

#import message Box
from MessageBox_Anywhere.msgBox import Ui_msg_box
from MessageBox_Anywhere.msgWith_btnOk import Ui_msgBox_ok
from MessageBox_Anywhere.msgWith_btnYaTidak import Ui_msgBox_YaTdk 


from service.db import cek_username, insert_user
        
#FORM KOSONG
class empty_form(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.ui = Ui_Form_Empty()
        self.ui.setupUi(self)
        self.stacked = stacked
                
        
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
        QTimer.singleShot(1000, self.open_Login)
    
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
    dataSent = pyqtSignal(str)
    
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
        password = self.ui.txt_password.text().strip()
        jenis_pertanyaan = self.ui.cmbBox_sec_qstion.currentText()
        cek_cmb_box = self.ui.cmbBox_sec_qstion.currentIndex()

        # Buat instance messageBox baru tiap pemanggilan
        msgBox = messageBox()

        # Validasi input
        if len(username) == 0:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon isi username!")
            msgBox.exec_()
            msgBox.rejected.connect(self.back_regist)
            return

        if len(password) == 0:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon isi password!")
            msgBox.exec_()
            msgBox.rejected.connect(self.back_regist)
            return

        if len(username) < 3 or len(username) > 20:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Username harus 3-20 karakter!")
            msgBox.exec_()
            msgBox.rejected.connect(self.back_regist)
            return

        if len(password) < 8 or len(password) > 16:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Password harus 8-16 karakter!")
            msgBox.exec_()
            msgBox.rejected.connect(self.back_regist)
            return

        if cek_cmb_box == 0:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Silahkan pilih security question!")
            msgBox.exec_()
            msgBox.rejected.connect(self.back_regist)
            return

        # Cek username di database
        if cek_username(username):
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Username sudah digunakan!")
            msgBox.exec_()
            msgBox.rejected.connect(self.back_regist)
            return

        # Simpan user baru ke database
        try:
            insert_user(username, password, jenis_pertanyaan)
        except Exception as e:
            msgBox.ui.LblJenisMsg.setText("Error!")
            msgBox.ui.LblKonten_isi.setText(f"Gagal menyimpan data:\n{str(e)}")
            msgBox.show()
            msgBox.rejected.connect(self.back_regist)
            return

        # Jika sukses, lanjut ke security question
        self.dataSent.emit(jenis_pertanyaan)
        self.stacked.setCurrentWidget(buat_sec_question)
        self.stacked.setWindowTitle("SECURITY QUESTION")
        self.stacked.setWindowIcon(QIcon(":/LogoAndWindowsIcon/Aset/LogoIconSolusiku-final.png"))
        self.stacked.setStyleSheet("Background-color: #ebebea;")
                
                
        
    def stay_regist(self):
        msgBox_YaTdk.close()
        self.stacked.setCurrentIndex(2)
    
    def goto_login(self):
        msgBox_YaTdk.close()
        self.ui.txt_username.setText("")
        self.ui.txt_password.setText("")
        self.ui.cmbBox_sec_qstion.setCurrentIndex(0)
        self.ui.chk_show_pw.setChecked(False)
        self.stacked.setCurrentIndex(1)
        self.stacked.setWindowTitle("LOGIN")
        self.stacked.setWindowIcon(QIcon(":/LogoAndWindowsIcon/Aset/LogoIconSolusiku-final.png"))
        self.stacked.setStyleSheet("Background-color: #ebebea;")
            
    #back_to_Login
    def back_Login(self):
        msgBox_YaTdk.ui.LblKonten_isi.setText("Apakah kamu yakin ingin membatalkan proses register ?")
        msgBox_YaTdk.ui.btnTidak.clicked.connect(self.stay_regist)
        msgBox_YaTdk.ui.btnYa.clicked.connect(self.goto_login)
        self.stacked.setCurrentIndex(3)
        msgBox_YaTdk.show()
        
    
    def back_regist(self):
        self.stacked.setCurrentIndex(2)    
        

#FORM MENJAWAB SEQURITY QUESTION
class formJawab_secQuestion(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.ui = Ui_form_buat_scr_question()
        self.ui.setupUi(self)
        self.stacked = stacked
        self.ui.btn_back.clicked.connect(self.open_Regist)
        self.ui.btn_identify.clicked.connect(self.goto_login_process)
    
    
    def data_sending(self, data):
        self.jen_prtny = data
        
        if self.jen_prtny == "Makanan Favorit":
            self.ui.txt_Quest.setText(pertanyaan1)
        elif self.jen_prtny == "Hewan Pelihara":
            self.ui.txt_Quest.setText(pertanyaan2)
        elif self.jen_prtny == "Guru Favorit":
            self.ui.txt_Quest.setText(pertanyaan3)
        elif self.jen_prtny == "Cinta Pertama":
            self.ui.txt_Quest.setText(pertanyaan4)
        elif self.jen_prtny == "Hobi":
            self.ui.txt_Quest.setText(pertanyaan5) 
        
    #back_to_register   
    def open_Regist(self):
        self.stacked.setCurrentIndex(2)
        self.stacked.setWindowTitle("REGISTER")
    
    #tetap di form security question
    def backto_sec_question(self):
        self.stacked.setCurrentIndex(4)
    
    #menuju form login
    def back_sec_questions(self):
        register.ui.txt_username.setText("")
        self.stacked.setCurrentIndex(1)
        self.stacked.setWindowTitle("LOGIN")
        
    #menuju form login melalui button ok    
    def back_sec_questions_btnOk(self):
        #Reset segala komponen yang terdapat di form regist dan sec_question
        register.ui.txt_username.setText("")
        register.ui.txt_password.setText("")
        register.ui.cmbBox_sec_qstion.setCurrentIndex(0)
        register.ui.chk_show_pw.setChecked(False)
        buat_sec_question.ui.txt_answer.setText("")
        
        #close messageBox show form Login
        msgBox_ok.close()
        self.stacked.setCurrentIndex(1)
        self.stacked.setWindowTitle("LOGIN")
        
    #verifikasi untuk Open Login
    def goto_login_process(self):
        jwb_pertanyaan = self.ui.txt_answer.text().strip()
        
        if len(jwb_pertanyaan) == 0:
            msgBox.ui.LblJenisMsg.setText("Peringatan!")
            msgBox.ui.LblKonten_isi.setText("Mohon Maaf!\nAnda belum menjawab security question.")
            self.stacked.setCurrentIndex(3)
            msgBox.show()
            msgBox.rejected.connect(self.backto_sec_question)
            return
        else:
            msgBox_ok.ui.LblJenisMsg.setText("Informasi!")
            msgBox_ok.ui.LblKonten_isi.setText("Register Sukses\nSilahkan Login.")
            self.stacked.setCurrentIndex(3)
            msgBox_ok.show()
            msgBox_ok.rejected.connect(self.back_sec_questions)
            msgBox_ok.ui.btnOk.clicked.connect(self.back_sec_questions_btnOk)
            return
        
    
"""        
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
    emptyform = empty_form(stacked)
    buat_sec_question = formJawab_secQuestion(stacked)
    #===
    stacked.addWidget(windowloading) #0
    stacked.addWidget(login) #1
    stacked.addWidget(register) #2
    stacked.addWidget(emptyform) #3
    stacked.addWidget(buat_sec_question) #4
    #===
    
    #Penghubungan data
    register.dataSent.connect(buat_sec_question.data_sending)
    
    
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