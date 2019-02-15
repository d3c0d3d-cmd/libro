# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.navTree = QtWidgets.QTreeWidget(self.splitter)
        self.navTree.setObjectName("navTree")
        self.navTree.headerItem().setText(0, "1")
        self.bookTable = BookTableView(self.splitter)
        self.bookTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.bookTable.setObjectName("bookTable")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAddBooks = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbar/tool-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddBooks.setIcon(icon)
        self.actionAddBooks.setIconVisibleInMenu(False)
        self.actionAddBooks.setObjectName("actionAddBooks")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionExit.setObjectName("actionExit")
        self.actionConvertToDisk = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/toolbar/tool-hdd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConvertToDisk.setIcon(icon1)
        self.actionConvertToDisk.setIconVisibleInMenu(False)
        self.actionConvertToDisk.setObjectName("actionConvertToDisk")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/toolbar/tool-settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon2)
        self.actionSettings.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionSettings.setIconVisibleInMenu(False)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRemoveBooks = QtWidgets.QAction(MainWindow)
        self.actionRemoveBooks.setObjectName("actionRemoveBooks")
        self.actionAboutQt = QtWidgets.QAction(MainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.menuFile.addAction(self.actionAddBooks)
        self.menuFile.addAction(self.actionRemoveBooks)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConvertToDisk)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAddBooks)
        self.toolBar.addAction(self.actionConvertToDisk)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        self.actionAddBooks.triggered.connect(MainWindow.onActionAddBooks)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionConvertToDisk.triggered.connect(MainWindow.onActionConvertToDisk)
        self.actionSettings.triggered.connect(MainWindow.onActionSettings)
        self.actionRemoveBooks.triggered.connect(MainWindow.onActionRemoveBooks)
        self.actionAbout.triggered.connect(MainWindow.onActionAbout)
        self.actionAboutQt.triggered.connect(MainWindow.onActionAboutQt)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAddBooks.setText(_translate("MainWindow", "Add books"))
        self.actionAddBooks.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionConvertToDisk.setText(_translate("MainWindow", "Convert to disk"))
        self.actionConvertToDisk.setToolTip(_translate("MainWindow", "Convert book to disk"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionRemoveBooks.setText(_translate("MainWindow", "Remove books"))
        self.actionRemoveBooks.setToolTip(_translate("MainWindow", "Remove books"))
        self.actionRemoveBooks.setShortcut(_translate("MainWindow", "Del"))
        self.actionAboutQt.setText(_translate("MainWindow", "About Qt"))

from .booktableview import BookTableView
from . import resources_rc