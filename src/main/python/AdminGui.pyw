# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkflowAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1263, 832)
        MainWindow.setIconSize(QtCore.QSize(40, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 1221, 751))
        self.tabWidget.setMaximumSize(QtCore.QSize(1221, 751))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(50, 16))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabData = QtWidgets.QWidget()
        self.tabData.setObjectName("tabData")
        self.gboxDataFiles = QtWidgets.QGroupBox(self.tabData)
        self.gboxDataFiles.setGeometry(QtCore.QRect(450, 10, 751, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gboxDataFiles.setFont(font)
        self.gboxDataFiles.setStyleSheet("")
        self.gboxDataFiles.setObjectName("gboxDataFiles")
        self.lneMstFile = QtWidgets.QLineEdit(self.gboxDataFiles)
        self.lneMstFile.setGeometry(QtCore.QRect(289, 40, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lneMstFile.setFont(font)
        self.lneMstFile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lneMstFile.setObjectName("lneMstFile")
        self.lneDlyWrkflwDataFile = QtWidgets.QLineEdit(self.gboxDataFiles)
        self.lneDlyWrkflwDataFile.setGeometry(QtCore.QRect(289, 90, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lneDlyWrkflwDataFile.setFont(font)
        self.lneDlyWrkflwDataFile.setToolTip("")
        self.lneDlyWrkflwDataFile.setToolTipDuration(9)
        self.lneDlyWrkflwDataFile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lneDlyWrkflwDataFile.setObjectName("lneDlyWrkflwDataFile")
        self.btnMstFileSlct = QtWidgets.QPushButton(self.gboxDataFiles)
        self.btnMstFileSlct.setGeometry(QtCore.QRect(661, 40, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnMstFileSlct.setFont(font)
        self.btnMstFileSlct.setObjectName("btnMstFileSlct")
        self.btnDlyWrkflwDataSlct = QtWidgets.QPushButton(self.gboxDataFiles)
        self.btnDlyWrkflwDataSlct.setGeometry(QtCore.QRect(661, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnDlyWrkflwDataSlct.setFont(font)
        self.btnDlyWrkflwDataSlct.setObjectName("btnDlyWrkflwDataSlct")
        self.lblMstFile = QtWidgets.QLabel(self.gboxDataFiles)
        self.lblMstFile.setGeometry(QtCore.QRect(36, 40, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblMstFile.setFont(font)
        self.lblMstFile.setObjectName("lblMstFile")
        self.lblDlyWrkflwDataFile = QtWidgets.QLabel(self.gboxDataFiles)
        self.lblDlyWrkflwDataFile.setGeometry(QtCore.QRect(35, 90, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblDlyWrkflwDataFile.setFont(font)
        self.lblDlyWrkflwDataFile.setToolTip("")
        self.lblDlyWrkflwDataFile.setToolTipDuration(10)
        self.lblDlyWrkflwDataFile.setWhatsThis("")
        self.lblDlyWrkflwDataFile.setObjectName("lblDlyWrkflwDataFile")
        self.lneDlyWrkflwRptFile = QtWidgets.QLineEdit(self.gboxDataFiles)
        self.lneDlyWrkflwRptFile.setGeometry(QtCore.QRect(289, 140, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lneDlyWrkflwRptFile.setFont(font)
        self.lneDlyWrkflwRptFile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lneDlyWrkflwRptFile.setObjectName("lneDlyWrkflwRptFile")
        self.lblDlyWrkflwRptFile = QtWidgets.QLabel(self.gboxDataFiles)
        self.lblDlyWrkflwRptFile.setGeometry(QtCore.QRect(35, 140, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblDlyWrkflwRptFile.setFont(font)
        self.lblDlyWrkflwRptFile.setObjectName("lblDlyWrkflwRptFile")
        self.btnDlyWrkflwRptSlct = QtWidgets.QPushButton(self.gboxDataFiles)
        self.btnDlyWrkflwRptSlct.setGeometry(QtCore.QRect(661, 140, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnDlyWrkflwRptSlct.setFont(font)
        self.btnDlyWrkflwRptSlct.setObjectName("btnDlyWrkflwRptSlct")
        self.btnMstFileSlct.raise_()
        self.lblMstFile.raise_()
        self.lblDlyWrkflwDataFile.raise_()
        self.btnDlyWrkflwDataSlct.raise_()
        self.lneDlyWrkflwDataFile.raise_()
        self.lneMstFile.raise_()
        self.lneDlyWrkflwRptFile.raise_()
        self.lblDlyWrkflwRptFile.raise_()
        self.btnDlyWrkflwRptSlct.raise_()
        self.gboxStatus = QtWidgets.QGroupBox(self.tabData)
        self.gboxStatus.setEnabled(False)
        self.gboxStatus.setGeometry(QtCore.QRect(10, 370, 421, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gboxStatus.setFont(font)
        self.gboxStatus.setObjectName("gboxStatus")
        self.lblCurrStatus = QtWidgets.QLabel(self.gboxStatus)
        self.lblCurrStatus.setGeometry(QtCore.QRect(10, 40, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblCurrStatus.setFont(font)
        self.lblCurrStatus.setStyleSheet("color: rgb(0, 0, 0);")
        self.lblCurrStatus.setObjectName("lblCurrStatus")
        self.lblTasksCmpl = QtWidgets.QLabel(self.gboxStatus)
        self.lblTasksCmpl.setGeometry(QtCore.QRect(10, 80, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblTasksCmpl.setFont(font)
        self.lblTasksCmpl.setStyleSheet("color: rgb(0, 0, 0);")
        self.lblTasksCmpl.setObjectName("lblTasksCmpl")
        self.lneCurrStatus = QtWidgets.QLineEdit(self.gboxStatus)
        self.lneCurrStatus.setGeometry(QtCore.QRect(209, 40, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lneCurrStatus.setFont(font)
        self.lneCurrStatus.setStyleSheet("color: rgb(135, 135, 135);")
        self.lneCurrStatus.setFrame(False)
        self.lneCurrStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lneCurrStatus.setObjectName("lneCurrStatus")
        self.lneTasksCmpl = QtWidgets.QLineEdit(self.gboxStatus)
        self.lneTasksCmpl.setGeometry(QtCore.QRect(209, 80, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lneTasksCmpl.setFont(font)
        self.lneTasksCmpl.setStyleSheet("color: rgb(0, 0, 0);")
        self.lneTasksCmpl.setFrame(False)
        self.lneTasksCmpl.setObjectName("lneTasksCmpl")
        self.lineData = QtWidgets.QFrame(self.tabData)
        self.lineData.setGeometry(QtCore.QRect(10, 315, 1191, 31))
        self.lineData.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineData.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineData.setObjectName("lineData")
        self.btnDataUpdte = QtWidgets.QPushButton(self.tabData)
        self.btnDataUpdte.setGeometry(QtCore.QRect(526, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnDataUpdte.setFont(font)
        self.btnDataUpdte.setStyleSheet("background-color: rgb(16, 88, 82);\n"
"color: rgb(255, 255, 255);")
        self.btnDataUpdte.setObjectName("btnDataUpdte")
        self.lblDataMgmt = QtWidgets.QLabel(self.tabData)
        self.lblDataMgmt.setGeometry(QtCore.QRect(10, 5, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lblDataMgmt.setFont(font)
        self.lblDataMgmt.setStyleSheet("color: rgb(198, 45, 66);")
        self.lblDataMgmt.setObjectName("lblDataMgmt")
        self.teDataMgmt = QtWidgets.QPlainTextEdit(self.tabData)
        self.teDataMgmt.setEnabled(False)
        self.teDataMgmt.setGeometry(QtCore.QRect(10, 40, 421, 151))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.teDataMgmt.setFont(font)
        self.teDataMgmt.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.teDataMgmt.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.teDataMgmt.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.teDataMgmt.setObjectName("teDataMgmt")
        self.gboxOutput = QtWidgets.QGroupBox(self.tabData)
        self.gboxOutput.setGeometry(QtCore.QRect(450, 370, 751, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gboxOutput.setFont(font)
        self.gboxOutput.setObjectName("gboxOutput")
        self.teDataStatOut = QtWidgets.QTextEdit(self.gboxOutput)
        self.teDataStatOut.setEnabled(True)
        self.teDataStatOut.setGeometry(QtCore.QRect(20, 40, 701, 231))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.teDataStatOut.setFont(font)
        self.teDataStatOut.setStyleSheet("color: rgb(0, 0, 0);")
        self.teDataStatOut.setReadOnly(True)
        self.teDataStatOut.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.teDataStatOut.setObjectName("teDataStatOut")
        self.gboxStatus.raise_()
        self.gboxDataFiles.raise_()
        self.lineData.raise_()
        self.btnDataUpdte.raise_()
        self.lblDataMgmt.raise_()
        self.teDataMgmt.raise_()
        self.gboxOutput.raise_()
        self.tabWidget.addTab(self.tabData, "")
        self.tabEmail = QtWidgets.QWidget()
        self.tabEmail.setObjectName("tabEmail")
        self.lblEmailMgmt = QtWidgets.QLabel(self.tabEmail)
        self.lblEmailMgmt.setGeometry(QtCore.QRect(10, 5, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lblEmailMgmt.setFont(font)
        self.lblEmailMgmt.setStyleSheet("color: rgb(198, 45, 66);")
        self.lblEmailMgmt.setObjectName("lblEmailMgmt")
        self.teDataMgmt_2 = QtWidgets.QPlainTextEdit(self.tabEmail)
        self.teDataMgmt_2.setEnabled(False)
        self.teDataMgmt_2.setGeometry(QtCore.QRect(10, 40, 451, 131))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.teDataMgmt_2.setFont(font)
        self.teDataMgmt_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.teDataMgmt_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.teDataMgmt_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.teDataMgmt_2.setObjectName("teDataMgmt_2")
        self.gboxEmailInpt = QtWidgets.QGroupBox(self.tabEmail)
        self.gboxEmailInpt.setGeometry(QtCore.QRect(500, 10, 671, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gboxEmailInpt.setFont(font)
        self.gboxEmailInpt.setObjectName("gboxEmailInpt")
        self.pteEmailInpt = QtWidgets.QPlainTextEdit(self.gboxEmailInpt)
        self.pteEmailInpt.setGeometry(QtCore.QRect(80, 30, 431, 51))
        self.pteEmailInpt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pteEmailInpt.setObjectName("pteEmailInpt")
        self.lblEmailInpt = QtWidgets.QLabel(self.gboxEmailInpt)
        self.lblEmailInpt.setGeometry(QtCore.QRect(10, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblEmailInpt.setFont(font)
        self.lblEmailInpt.setObjectName("lblEmailInpt")
        self.gboxEmailStatOut = QtWidgets.QGroupBox(self.tabEmail)
        self.gboxEmailStatOut.setGeometry(QtCore.QRect(10, 320, 1161, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gboxEmailStatOut.setFont(font)
        self.gboxEmailStatOut.setObjectName("gboxEmailStatOut")
        self.teEmailStatOut = QtWidgets.QTextEdit(self.gboxEmailStatOut)
        self.teEmailStatOut.setGeometry(QtCore.QRect(10, 30, 1141, 201))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.teEmailStatOut.setFont(font)
        self.teEmailStatOut.setObjectName("teEmailStatOut")
        self.lineEmail = QtWidgets.QFrame(self.tabEmail)
        self.lineEmail.setGeometry(QtCore.QRect(10, 290, 1161, 16))
        self.lineEmail.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineEmail.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineEmail.setObjectName("lineEmail")
        self.gboxEmailRpts = QtWidgets.QGroupBox(self.tabEmail)
        self.gboxEmailRpts.setGeometry(QtCore.QRect(500, 130, 671, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gboxEmailRpts.setFont(font)
        self.gboxEmailRpts.setObjectName("gboxEmailRpts")
        self.lblEmailRpts = QtWidgets.QLabel(self.gboxEmailRpts)
        self.lblEmailRpts.setGeometry(QtCore.QRect(10, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblEmailRpts.setFont(font)
        self.lblEmailRpts.setObjectName("lblEmailRpts")
        self.pteEmailRpts = QtWidgets.QPlainTextEdit(self.gboxEmailRpts)
        self.pteEmailRpts.setGeometry(QtCore.QRect(80, 30, 431, 71))
        self.pteEmailRpts.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pteEmailRpts.setObjectName("pteEmailRpts")
        self.btnEmailRptsSlct = QtWidgets.QPushButton(self.gboxEmailRpts)
        self.btnEmailRptsSlct.setGeometry(QtCore.QRect(512, 30, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnEmailRptsSlct.setFont(font)
        self.btnEmailRptsSlct.setObjectName("btnEmailRptsSlct")
        self.btnEmailSend = QtWidgets.QPushButton(self.tabEmail)
        self.btnEmailSend.setGeometry(QtCore.QRect(530, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnEmailSend.setFont(font)
        self.btnEmailSend.setStyleSheet("background-color: rgb(16, 88, 82);\n"
"color: rgb(255, 255, 255);")
        self.btnEmailSend.setObjectName("btnEmailSend")
        self.tabWidget.addTab(self.tabEmail, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1263, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Loan Workflow Admin"))
        self.gboxDataFiles.setTitle(_translate("MainWindow", "File Selections"))
        self.lneDlyWrkflwDataFile.setPlaceholderText(_translate("MainWindow", "DailyWorkflowData.xlsx"))
        self.btnMstFileSlct.setText(_translate("MainWindow", "Select"))
        self.btnDlyWrkflwDataSlct.setText(_translate("MainWindow", "Select"))
        self.lblMstFile.setText(_translate("MainWindow", "Encompass data file:"))
        self.lblDlyWrkflwDataFile.setText(_translate("MainWindow", "Daily Workflow data file:"))
        self.lneDlyWrkflwRptFile.setPlaceholderText(_translate("MainWindow", "DailyWorkflowRpting.xlsx"))
        self.lblDlyWrkflwRptFile.setText(_translate("MainWindow", "Daily Workflow Reporting file:"))
        self.btnDlyWrkflwRptSlct.setText(_translate("MainWindow", "Select"))
        self.gboxStatus.setTitle(_translate("MainWindow", "Status"))
        self.lblCurrStatus.setText(_translate("MainWindow", "Current Status:"))
        self.lblTasksCmpl.setText(_translate("MainWindow", "Tasks Completed:"))
        self.lneCurrStatus.setPlaceholderText(_translate("MainWindow", "Idle"))
        self.btnDataUpdte.setText(_translate("MainWindow", "Start Transfer"))
        self.lblDataMgmt.setText(_translate("MainWindow", "Data Management"))
        self.teDataMgmt.setPlainText(_translate("MainWindow", "Update Daily Workflow File(s) with latest Encompass download.\n"
"\n"
"Use \'File Selections\' to choose appropriate files.\n"
"\n"
"Click \'Start Transfer\' to initiate data update.\n"
"\n"
""))
        self.gboxOutput.setTitle(_translate("MainWindow", "Tasks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), _translate("MainWindow", "Data"))
        self.lblEmailMgmt.setText(_translate("MainWindow", "Email Management"))
        self.teDataMgmt_2.setPlainText(_translate("MainWindow", "Administer Email communication of reports to recipients.\n"
"\n"
""))
        self.gboxEmailInpt.setTitle(_translate("MainWindow", "Email(s) Input"))
        self.lblEmailInpt.setText(_translate("MainWindow", "Emails:"))
        self.gboxEmailStatOut.setTitle(_translate("MainWindow", "Status"))
        self.gboxEmailRpts.setTitle(_translate("MainWindow", "Report(s) Selection"))
        self.lblEmailRpts.setText(_translate("MainWindow", "Report(s):"))
        self.btnEmailRptsSlct.setText(_translate("MainWindow", "Select"))
        self.btnEmailSend.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEmail), _translate("MainWindow", "Email"))
