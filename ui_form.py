# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(375, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(375, 600))
        MainWindow.setMaximumSize(QSize(375, 600))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        self.centralwidget.setPalette(palette1)
        self.vault_btn = QPushButton(self.centralwidget)
        self.vault_btn.setObjectName(u"vault_btn")
        self.vault_btn.setGeometry(QRect(210, 10, 105, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(211, 45, 39, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        self.vault_btn.setPalette(palette2)
        icon = QIcon()
        icon.addFile(u"../assets/images/vault_arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vault_btn.setIcon(icon)
        self.vault_btn.setAutoRepeat(False)
        self.plus_button = QPushButton(self.centralwidget)
        self.plus_button.setObjectName(u"plus_button")
        self.plus_button.setGeometry(QRect(500, 20, 41, 31))
        icon1 = QIcon()
        icon1.addFile(u"../assets/images/plus_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plus_button.setIcon(icon1)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 591, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 192, 38))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setFrame(True)
        self.lineEdit.setClearButtonEnabled(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 20, 18, 18))
        self.pushButton_2.setIcon(icon1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.vault_btn.setText(QCoreApplication.translate("MainWindow", u"Vault", None))
        self.plus_button.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_2.setText("")
    # retranslateUi

