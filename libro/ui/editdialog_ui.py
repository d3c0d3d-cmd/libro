# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\editdialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(600, 400))
        Dialog.setMaximumSize(QtCore.QSize(600, 400))
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.coverImage = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coverImage.sizePolicy().hasHeightForWidth())
        self.coverImage.setSizePolicy(sizePolicy)
        self.coverImage.setMinimumSize(QtCore.QSize(150, 200))
        self.coverImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.coverImage.setAlignment(QtCore.Qt.AlignCenter)
        self.coverImage.setObjectName("coverImage")
        self.verticalLayout_2.addWidget(self.coverImage)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.titleEdit = ComboEdit(Dialog)
        self.titleEdit.setEditable(True)
        self.titleEdit.setObjectName("titleEdit")
        self.verticalLayout.addWidget(self.titleEdit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.authorEdit = ComboEdit(Dialog)
        self.authorEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.authorEdit.setEditable(True)
        self.authorEdit.setObjectName("authorEdit")
        self.verticalLayout.addWidget(self.authorEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.seriesEdit = ComboEdit(Dialog)
        self.seriesEdit.setEditable(True)
        self.seriesEdit.setObjectName("seriesEdit")
        self.gridLayout.addWidget(self.seriesEdit, 1, 0, 1, 1)
        self.seriesIndexEdit = ComboEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seriesIndexEdit.sizePolicy().hasHeightForWidth())
        self.seriesIndexEdit.setSizePolicy(sizePolicy)
        self.seriesIndexEdit.setEditable(True)
        self.seriesIndexEdit.setObjectName("seriesIndexEdit")
        self.gridLayout.addWidget(self.seriesIndexEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.tagsEdit = ComboEdit(Dialog)
        self.tagsEdit.setEditable(True)
        self.tagsEdit.setObjectName("tagsEdit")
        self.verticalLayout.addWidget(self.tagsEdit)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.translatorEdit = ComboEdit(Dialog)
        self.translatorEdit.setEditable(True)
        self.translatorEdit.setObjectName("translatorEdit")
        self.gridLayout_2.addWidget(self.translatorEdit, 1, 0, 1, 1)
        self.langEdit = ComboEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langEdit.sizePolicy().hasHeightForWidth())
        self.langEdit.setSizePolicy(sizePolicy)
        self.langEdit.setEditable(True)
        self.langEdit.setObjectName("langEdit")
        self.gridLayout_2.addWidget(self.langEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prevButton = QtWidgets.QPushButton(Dialog)
        self.prevButton.setObjectName("prevButton")
        self.horizontalLayout_2.addWidget(self.prevButton)
        self.nextButton = QtWidgets.QPushButton(Dialog)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit metadata"))
        self.coverImage.setText(_translate("Dialog", "No cover"))
        self.label_2.setText(_translate("Dialog", "Title"))
        self.label_3.setText(_translate("Dialog", "Author"))
        self.label_4.setText(_translate("Dialog", "Series"))
        self.label_5.setText(_translate("Dialog", "Index"))
        self.label_6.setText(_translate("Dialog", "Tags"))
        self.label_8.setText(_translate("Dialog", "Translator"))
        self.label_7.setText(_translate("Dialog", "Lang"))
        self.prevButton.setText(_translate("Dialog", "Previous"))
        self.nextButton.setText(_translate("Dialog", "Next"))

from .comboedit import ComboEdit