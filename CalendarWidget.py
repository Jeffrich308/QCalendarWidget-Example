# -------------------------------------------------------------------------------
# Name:             CalendarWidget.py
# Purpose:          Use the Calendar widget as a popup date selector
#
# Author:           Jeffreaux
#
# Created:          01July24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QCalendarWidget, QLabel, QDateEdit
from PyQt5 import uic
import sys




class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("CalendarWidget_GUI.ui", self)

        self.calWidget.setHidden(True)  # Hiding Calendar Widget at startup
        
        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.actExit = self.findChild(QAction, "actExit")
        self.calWidget = self.findChild(QCalendarWidget, "calWidget")
        self.btnDate = self.findChild(QPushButton, "btnDate")
        self.lblDate = self.findChild(QLabel, "lblDate")
        self.dateEdit = self.findChild(QDateEdit, "dateEdit")


        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.actExit.triggered.connect(self.closeEvent)
        self.btnDate.clicked.connect(self.showCal)
        self.calWidget.selectionChanged.connect(self.getDate) # Get date when a date is selected in Calendar

        # Show the app
        self.show()


    def showCal(self):
        print("Getting Date")
        self.calWidget.setHidden(False) # Showing Calendar Widget at startup


    def getDate(self):
        dateSelected = self.calWidget.selectedDate()  # Assign date from Cal widget to variable
        self.calWidget.setHidden(True)  # Hide the calendar after date selected
        self.lblDate.setText(str(dateSelected.toString()))  # Print date to label



    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
