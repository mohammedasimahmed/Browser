from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import sys
import os
import random

from PyQt5.QtWidgets import QWidget
class Tab(QMainWindow):
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
      self.browser.page().loadFinished.connect(self.handleTitleChange)
      
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
      # self.showMaximized()
   
   def handleUrlChange(self):
      self.browser.setUrl(QUrl(self.urlBox.text()))
      self.browser.page().loadFinished.connect(self.handleTitleChange)
   def goBack(self):
      self.browser.back()
   def goForward(self):
      self.browser.forward()
   def reloadPage(self):
      self.browser.reload()
   def changeUrl(self, url):
      self.urlBox.setText(url.toString())
   def handleTitleChange(self):
      self.setWindowTitle(self.browser.page().title())
      # print(self.browser.page().title())
   def handleFullScreenRequest(self, request):
      request.accept()
      if request.toggleOn():
         self.showFullScreen()
         self.navigationBar.hide()
      else:
         self.showMaximized()
         self.navigationBar.show()
 
class TableWidget(QWidget):
   def __init__(self):
      super().__init__()
      self.tabs = QTabWidget()
      self.tab = Tab()
      self.addtab = QPushButton()
      self.addtab.setText("add tab")
      self.tabs.addTab(self.tab, "")
      self.tabs.setCornerWidget(self.addtab)
      self.addtab.clicked.connect(self.addnewTab)
      
      self.tab.windowTitleChanged.connect(lambda : self.handleTabTitleChange(self.tab))
      
      self.tabs.setTabsClosable(True)
      self.tabs.tabCloseRequested.connect(self.closeTab)
      
      container = QVBoxLayout()
      container.addWidget(self.tabs)
      self.setLayout(container)
      
   def handleTabTitleChange(self, tab):
      ind = self.tabs.indexOf(tab)
      self.tabs.setTabText(ind, tab.windowTitle())
      # print(ind)
      # print
      # print("bye")
   
   def closeTab(self, index):
      if self.tabs.count()<2:
         return
      self.tabs.removeTab(index)
   def addnewTab(self):
      num = str(random.randint(10, 10000000))  
      newtab = "tab" + num
      tab_instance = Tab()
      
      setattr(self, newtab, tab_instance) 
      
      self.tabs.addTab(tab_instance, "")
      tab_instance.windowTitleChanged.connect(lambda: self.handleTabTitleChange(tab_instance))
      # print("hey")

      
class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self.table = TableWidget()
      self.setCentralWidget(self.table)
      self.showMaximized()
      
      
app = QApplication(sys.argv)
QApplication.setApplicationName("My Browser")
window = MainWindow()
window.show()
app.exec()
   
