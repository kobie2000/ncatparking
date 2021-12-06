import sys
import os
from LoginPage import LoginUI
from PyQt5.QtWidgets import QApplication, QSplashScreen, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class MainUI():
	def showSplashScreen(self):
		self.pix = QPixap("ncatparking.jpg)
		self.splassh = QSplashScreen(self.pix,  Qt.WindowStaysOnTopHint)
		self.splassh.show()
		

def showLoginPage():
	mainUI.splassh.close()
	login.showLoginUI()
	
app = QApplication(sys.argv)
login = LoginUI()
mainscrn = MainUI()
mainscrn.showSplashScreen()

if os.path.exists("./config.json"):
	QTimer.singleShot(3000,showLoginPage)
else:
	print("error")

sys.exit((app.exec_())
