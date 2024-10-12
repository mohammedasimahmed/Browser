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
      self.browser.urlChanged.connect(self.changeUrl)
      self.browser.page().settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
      self.browser.page().fullScreenRequested.connect(self.handleFullScreenRequest)
      self.urlBox.returnPressed.connect(self.handleUrlChange)
      
      self.navigationBar = QToolBar()
      self.navigationBar.addWidget(self.backButton)
      self.navigationBar.addWidget(self.reloadButton)
      self.navigationBar.addWidget(self.forwardButton)
      self.navigationBar.addWidget(self.urlBox)
      self.navigationBar.addWidget(self.goButton)
      
      container = QVBoxLayout()
      container.addWidget(self.navigationBar)
      container.addWidget(self.browser)
      
      widget = QWidget()
      widget.setLayout(container)
      
      self.setCentralWidget(widget)   
      self.showMaximized()
   
   def handleUrlChange(self):
      self.browser.setUrl(QUrl(self.urlBox.text()))
   def goBack(self):
      self.browser.back()
   def goForward(self):
      self.browser.forward()
   def reloadPage(self):
      self.browser.reload()
   def changeUrl(self, url):
      self.urlBox.setText(url.toString())
   def handleFullScreenRequest(self, request):
      request.accept()
      if request.toggleOn():
         self.showFullScreen()
         self.navigationBar.hide()
      else:
         self.showMaximized()
         self.navigationBar.show()
            
      
app = QApplication(sys.argv)
QApplication.setApplicationName("My Browser")
window = MainWindow()
window.show()

app.exec()
   
