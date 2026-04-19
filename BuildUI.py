# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BuildUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QLineEdit, QSizePolicy, QTabWidget,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1133, 686)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(270, 650, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.main_tabWidget = QTabWidget(Dialog)
        self.main_tabWidget.setObjectName(u"main_tabWidget")
        self.main_tabWidget.setGeometry(QRect(20, 30, 1091, 601))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.player2_groupBox = QGroupBox(self.tab)
        self.player2_groupBox.setObjectName(u"player2_groupBox")
        self.player2_groupBox.setGeometry(QRect(200, 30, 161, 121))
        self.p2_lineEdit = QLineEdit(self.player2_groupBox)
        self.p2_lineEdit.setObjectName(u"p2_lineEdit")
        self.p2_lineEdit.setGeometry(QRect(20, 30, 113, 26))
        self.player1_groupBox = QGroupBox(self.tab)
        self.player1_groupBox.setObjectName(u"player1_groupBox")
        self.player1_groupBox.setGeometry(QRect(10, 30, 161, 121))
        self.p1_lineEdit = QLineEdit(self.player1_groupBox)
        self.p1_lineEdit.setObjectName(u"p1_lineEdit")
        self.p1_lineEdit.setGeometry(QRect(20, 30, 113, 26))
        self.player3_groupBox = QGroupBox(self.tab)
        self.player3_groupBox.setObjectName(u"player3_groupBox")
        self.player3_groupBox.setGeometry(QRect(380, 30, 161, 121))
        self.p3_lineEdit = QLineEdit(self.player3_groupBox)
        self.p3_lineEdit.setObjectName(u"p3_lineEdit")
        self.p3_lineEdit.setGeometry(QRect(20, 30, 113, 26))
        self.player4_groupBox = QGroupBox(self.tab)
        self.player4_groupBox.setObjectName(u"player4_groupBox")
        self.player4_groupBox.setGeometry(QRect(570, 30, 161, 121))
        self.p4_lineEdit = QLineEdit(self.player4_groupBox)
        self.p4_lineEdit.setObjectName(u"p4_lineEdit")
        self.p4_lineEdit.setGeometry(QRect(20, 30, 113, 26))
        self.main_tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.main_tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.main_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.player2_groupBox.setTitle(QCoreApplication.translate("Dialog", u"Player 2", None))
        self.player1_groupBox.setTitle(QCoreApplication.translate("Dialog", u"Player 1", None))
        self.player3_groupBox.setTitle(QCoreApplication.translate("Dialog", u"Player 3", None))
        self.player4_groupBox.setTitle(QCoreApplication.translate("Dialog", u"Player 4", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Players View", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Settings", None))
    # retranslateUi

