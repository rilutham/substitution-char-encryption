import sys 
import sip
sip.setapi('QString', 3)
sip.setapi('QVariant', 3)
from PyQt4 import QtGui

class ApplicationWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Aplikasi Kriptografi Subtitusi Karakter")
        
        # TextEdit for plain text
        self.text_edit_plain = QtGui.QTextEdit(self)
        
        # QPushButton for encrypt
        self.btn_encrypt = QtGui.QPushButton('Encryption', self)
        self.btn_encrypt.clicked.connect(self.encryption)
        
        # TextEdit for result chiper text
        self.text_edit_chiper = QtGui.QTextEdit(self)
        
        # TextEdit for chiper text 2
        self.text_edit_chiper_2 = QtGui.QTextEdit(self)
        
        # QPushButton for decrypt
        self.btn_decrypt = QtGui.QPushButton('Decryption', self)
        self.btn_decrypt.clicked.connect(self.decryption)
        
        # TextEdit for result plain text 2
        self.text_edit_plain_2 = QtGui.QTextEdit(self)
        
        hbox = QtGui.QHBoxLayout()
        grid = QtGui.QGridLayout()
        
        hbox.addLayout(grid)

        grid.addWidget(self.text_edit_plain,0,0)
        grid.addWidget(self.btn_encrypt,1,0)
        grid.addWidget(self.text_edit_chiper,2,0)
        grid.addWidget(self.text_edit_chiper_2,0,1)
        grid.addWidget(self.btn_decrypt,1,1)
        grid.addWidget(self.text_edit_plain_2,2,1)
    
        self.setLayout(hbox)
    
    def encryption(self):
        
        self.plain_text = self.text_edit_plain.toPlainText()
        self.length = len(self.plain_text)
        chiper_text_list = ""
        
        for i in range(self.length):
        
            # Convert character to ASCII decimal number
            self.ascii_num = ord(self.plain_text[i])
            
            # Substitute ASCII decimal number
            if (self.ascii_num % 2 == 0):
                self.ascii_num = self.ascii_num - 7
            elif (self.ascii_num % 2 == 1):
                self.ascii_num = self.ascii_num + 9 
            
            # Convert ASCII decimal number to character
            chiper_text = chr(self.ascii_num)
            
            # Append character to chiper text string
            chiper_text_list = chiper_text_list + chiper_text
            
        self.text_edit_chiper.setText(chiper_text_list)
    
    def decryption(self):
        
        self.chiper_text = self.text_edit_chiper_2.toPlainText()
        self.length = len(self.chiper_text)
        plain_text_list = ""
        
        for i in range(self.length):
            
            # Convert character to ASCII decimal number
            self.ascii_num = ord(self.chiper_text[i])
            
            if (self.ascii_num % 2 == 0):
                self.ascii_num = self.ascii_num - 9
            elif (self.ascii_num % 2 == 1):
                self.ascii_num = self.ascii_num + 7
            
            # Convert ASCII decimal number to character
            plain_text = chr(self.ascii_num)
            
            # Append character to plain text string
            plain_text_list = plain_text_list + plain_text
        
        self.text_edit_plain_2.setText(plain_text_list)
  
if __name__ == '__main__':  
    app = QtGui.QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec_())