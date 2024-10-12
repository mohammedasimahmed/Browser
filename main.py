from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import sys
import os
class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self.setWindowTitle("Browser")

      self.urlBox = QLineEdit("https://www.google.com")
      self.goButton = QPushButton("Go")
      self.backButton = QPushButton("←")
      self.forwardButton = QPushButton("→")
      self.reloadButton = QPushButton("⟳")
      self.browser = QWebEngineView()
      
      self.backButton.clicked.connect(self.goBack)
      self.forwardButton.clicked.connect(self.goForward)
      self.reloadButton.clicked.connect(self.reloadPage)
      self.goButton.clicked.connect(self.handleUrlChange)
      self.browser.setUrl(QUrl("https://www.google.com"))
      self.urlBox.returnPressed.connect(self.handleUrlChange)
      
      navigationBar = QHBoxLayout()
      navigationBar.addWidget(self.backButton)
      navigationBar.addWidget(self.reloadButton)
      navigationBar.addWidget(self.forwardButton)
      navigationBar.addWidget(self.urlBox)
      navigationBar.addWidget(self.goButton)
      
      container = QVBoxLayout()
      container.addLayout(navigationBar)
      container.addWidget(self.browser)
      
      widget = QWidget()
      widget.setLayout(container)
      
      self.setCentralWidget(widget)   
   
   def handleUrlChange(self):
      self.browser.setUrl(QUrl(self.urlBox.text()))
   def goBack(self):
      self.browser.back()
      self.browser.urlChanged.connect(self.changeUrl)
   def goForward(self):
      self.browser.forward()
      self.browser.urlChanged.connect(self.changeUrl)
   def reloadPage(self):
      self.browser.reload()
   def changeUrl(self):
      self.urlBox.setText(self.browser.url().toString())
            
      
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
   
