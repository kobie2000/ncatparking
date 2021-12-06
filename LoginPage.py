from PyQt5.QtWidgets import QWidget,QVBoxLayout, QPushButton,QLabel,QLineEdit,QApplication
import sys
from HomePage import HomeUI

class LoginUI(QWidget):
	def _init_(self):
	super()._init_()
	self.setPageTitle("User Login")
	self.resize(400,200)
	layout = QVBoxLayout()
	
	label_uname = QLabel("Username: ")
	labe_uname.setStyleSheet("color:#FFD700;padding:10px;font-size:20px;")
	self.input_uname = QLineEdit()
	self.input_uname.setStyleSheet("padding:8px;font-size:18px")
	label_password = QLabel("Password: ")
	label_password.setStyleSheet("color:#FFD700;padding:10px;font-size:20px;")
	self.input_password = QLineEdit()
	self.input_password.setStyleSheet("padding:8px;font-size:18px")
	seff.errornote = QLabel()
	self.errornote.setStyleSheet("color:red;padding:8px;font-size:18px;text-align:center") 
	button_login = QPushButton("Login")
	button_login.setStyleSheet("padding:8px;font-size:18px;background:blue;color:#FFD700")
	layout.addWidget(labe_uname)
	layout.addWidget(self.input_uname)
	layout.addWidget(label_password)
	layout.addWidget(self.input_password)
	layout.addWidget(self.errornote)
	layout.addWidget(button_login)
	layout.addStretch()
	button_login.clicked.connect(self.showHome)
	self.setLayout(layout)
	
def showLoginUI(self):
	self.show()
	
