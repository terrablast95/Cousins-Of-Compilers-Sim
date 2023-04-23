# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTextBrowser,
    QTextEdit, QWidget)
import pictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"background-color: rgb(26, 24, 27);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1280, 720))
        self.stackedWidget.setMinimumSize(QSize(1280, 720))
        font = QFont()
        font.setPointSize(24)
        self.stackedWidget.setFont(font)
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.Title = QLabel(self.homepage)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(320, 140, 671, 71))
        font1 = QFont()
        font1.setPointSize(35)
        font1.setBold(True)
        self.Title.setFont(font1)
        self.by = QLabel(self.homepage)
        self.by.setObjectName(u"by")
        self.by.setGeometry(QRect(450, 260, 31, 31))
        font2 = QFont()
        font2.setPointSize(18)
        self.by.setFont(font2)
        self.names = QLabel(self.homepage)
        self.names.setObjectName(u"names")
        self.names.setGeometry(QRect(500, 260, 441, 91))
        self.names.setFont(font2)
        self.topic = QLabel(self.homepage)
        self.topic.setObjectName(u"topic")
        self.topic.setGeometry(QRect(420, 370, 531, 81))
        font3 = QFont()
        font3.setPointSize(23)
        font3.setBold(True)
        self.topic.setFont(font3)
        self.go_btn = QPushButton(self.homepage)
        self.go_btn.setObjectName(u"go_btn")
        self.go_btn.setGeometry(QRect(440, 510, 131, 51))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.go_btn.setFont(font4)
        self.go_btn.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.quit_btn = QPushButton(self.homepage)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setGeometry(QRect(770, 510, 131, 51))
        self.quit_btn.setFont(font4)
        self.quit_btn.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget.addWidget(self.homepage)
        self.disclaimer = QWidget()
        self.disclaimer.setObjectName(u"disclaimer")
        self.disc = QLabel(self.disclaimer)
        self.disc.setObjectName(u"disc")
        self.disc.setGeometry(QRect(140, 110, 1021, 501))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(False)
        self.disc.setFont(font5)
        self.disc.setWordWrap(True)
        self.continue_btn = QPushButton(self.disclaimer)
        self.continue_btn.setObjectName(u"continue_btn")
        self.continue_btn.setGeometry(QRect(540, 580, 191, 71))
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        self.continue_btn.setFont(font6)
        self.continue_btn.setStyleSheet(u"border: 1px solid white;")
        self.label_2 = QLabel(self.disclaimer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 60, 311, 71))
        font7 = QFont()
        font7.setPointSize(34)
        font7.setBold(True)
        self.label_2.setFont(font7)
        self.stackedWidget.addWidget(self.disclaimer)
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.menu_head = QLabel(self.menu)
        self.menu_head.setObjectName(u"menu_head")
        self.menu_head.setGeometry(QRect(250, 40, 841, 201))
        font8 = QFont()
        font8.setPointSize(49)
        font8.setBold(True)
        self.menu_head.setFont(font8)
        self.prep_btn = QPushButton(self.menu)
        self.prep_btn.setObjectName(u"prep_btn")
        self.prep_btn.setGeometry(QRect(250, 260, 351, 151))
        self.prep_btn.setFont(font4)
        self.prep_btn.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.linker_btn = QPushButton(self.menu)
        self.linker_btn.setObjectName(u"linker_btn")
        self.linker_btn.setGeometry(QRect(250, 450, 351, 151))
        self.linker_btn.setFont(font4)
        self.linker_btn.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.loader_btn = QPushButton(self.menu)
        self.loader_btn.setObjectName(u"loader_btn")
        self.loader_btn.setGeometry(QRect(740, 450, 351, 151))
        self.loader_btn.setFont(font4)
        self.loader_btn.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.assembler_btn = QPushButton(self.menu)
        self.assembler_btn.setObjectName(u"assembler_btn")
        self.assembler_btn.setGeometry(QRect(740, 260, 351, 151))
        self.assembler_btn.setFont(font4)
        self.assembler_btn.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.home_btn = QPushButton(self.menu)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setGeometry(QRect(40, 30, 71, 51))
        self.home_btn.setFont(font4)
        self.home_btn.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget.addWidget(self.menu)
        self.prep = QWidget()
        self.prep.setObjectName(u"prep")
        self.to_menu = QPushButton(self.prep)
        self.to_menu.setObjectName(u"to_menu")
        self.to_menu.setGeometry(QRect(970, 50, 231, 51))
        self.to_menu.setFont(font4)
        self.to_menu.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.prep_home = QLabel(self.prep)
        self.prep_home.setObjectName(u"prep_home")
        self.prep_home.setGeometry(QRect(70, 30, 421, 101))
        font9 = QFont()
        font9.setPointSize(37)
        font9.setBold(True)
        self.prep_home.setFont(font9)
        self.stackedWidget_2 = QStackedWidget(self.prep)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(29, 159, 1231, 551))
        self.prepmenu = QWidget()
        self.prepmenu.setObjectName(u"prepmenu")
        self.desc = QTextBrowser(self.prepmenu)
        self.desc.setObjectName(u"desc")
        self.desc.setGeometry(QRect(40, 40, 611, 211))
        self.desc.setFont(font2)
        self.prepdiag = QLabel(self.prepmenu)
        self.prepdiag.setObjectName(u"prepdiag")
        self.prepdiag.setGeometry(QRect(730, 30, 451, 391))
        self.prepdiag.setPixmap(QPixmap(u":/newPrefix/prepdiag.png"))
        self.macro_btn = QPushButton(self.prepmenu)
        self.macro_btn.setObjectName(u"macro_btn")
        self.macro_btn.setGeometry(QRect(40, 270, 271, 61))
        font10 = QFont()
        font10.setPointSize(15)
        self.macro_btn.setFont(font10)
        self.macro_btn.setStyleSheet(u"border: 1px solid white")
        self.file_btn = QPushButton(self.prepmenu)
        self.file_btn.setObjectName(u"file_btn")
        self.file_btn.setGeometry(QRect(380, 270, 271, 61))
        self.file_btn.setFont(font10)
        self.file_btn.setStyleSheet(u"border: 1px solid white")
        self.lang_btn = QPushButton(self.prepmenu)
        self.lang_btn.setObjectName(u"lang_btn")
        self.lang_btn.setGeometry(QRect(40, 350, 271, 61))
        self.lang_btn.setFont(font10)
        self.lang_btn.setStyleSheet(u"border: 1px solid white")
        self.comp_btn = QPushButton(self.prepmenu)
        self.comp_btn.setObjectName(u"comp_btn")
        self.comp_btn.setGeometry(QRect(380, 350, 271, 61))
        self.comp_btn.setFont(font10)
        self.comp_btn.setStyleSheet(u"border: 1px solid white")
        self.stackedWidget_2.addWidget(self.prepmenu)
        self.macro = QWidget()
        self.macro.setObjectName(u"macro")
        self.itpbox = QTextEdit(self.macro)
        self.itpbox.setObjectName(u"itpbox")
        self.itpbox.setGeometry(QRect(530, 60, 241, 281))
        font11 = QFont()
        font11.setPointSize(13)
        self.itpbox.setFont(font11)
        self.itpbox.setStyleSheet(u"background-color: rgb(26, 24, 27);\n"
"color: #ffffff;\n"
"border: 2px solid red;")
        self.mactitle = QLabel(self.macro)
        self.mactitle.setObjectName(u"mactitle")
        self.mactitle.setGeometry(QRect(40, 40, 241, 51))
        self.mactitle.setFont(font6)
        self.macdef = QTextBrowser(self.macro)
        self.macdef.setObjectName(u"macdef")
        self.macdef.setGeometry(QRect(30, 120, 421, 211))
        self.macdef.setFont(font2)
        self.macdiag = QLabel(self.macro)
        self.macdiag.setObjectName(u"macdiag")
        self.macdiag.setGeometry(QRect(30, 350, 781, 141))
        self.macdiag.setPixmap(QPixmap(u":/newPrefix/macrodiag.png"))
        self.toprep_menu = QPushButton(self.macro)
        self.toprep_menu.setObjectName(u"toprep_menu")
        self.toprep_menu.setGeometry(QRect(900, 430, 191, 51))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        self.toprep_menu.setFont(font12)
        self.toprep_menu.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.mactitle_2 = QLabel(self.macro)
        self.mactitle_2.setObjectName(u"mactitle_2")
        self.mactitle_2.setGeometry(QRect(920, 200, 241, 51))
        self.mactitle_2.setFont(font4)
        self.ppotext = QTextEdit(self.macro)
        self.ppotext.setObjectName(u"ppotext")
        self.ppotext.setGeometry(QRect(850, 240, 311, 171))
        font13 = QFont()
        font13.setPointSize(13)
        font13.setBold(True)
        self.ppotext.setFont(font13)
        self.ppotext.setStyleSheet(u"background-color: rgb(26, 24, 27);\n"
"color: #ffffff;\n"
"border: 2px solid purple;")
        self.ppotext.setReadOnly(True)
        self.trybox_3 = QTextBrowser(self.macro)
        self.trybox_3.setObjectName(u"trybox_3")
        self.trybox_3.setGeometry(QRect(850, 60, 311, 141))
        self.trybox_3.setFont(font10)
        self.trybox_3.setStyleSheet(u"border:1px solid yellow;")
        self.execute_btn2_2 = QPushButton(self.macro)
        self.execute_btn2_2.setObjectName(u"execute_btn2_2")
        self.execute_btn2_2.setGeometry(QRect(1060, 160, 101, 41))
        font14 = QFont()
        font14.setPointSize(12)
        font14.setBold(True)
        self.execute_btn2_2.setFont(font14)
        self.execute_btn2_2.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.label = QLabel(self.macro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(630, 320, 49, 16))
        self.label.setStyleSheet(u"color: red;")
        self.stackedWidget_2.addWidget(self.macro)
        self.mactitle_2.raise_()
        self.trybox_3.raise_()
        self.itpbox.raise_()
        self.mactitle.raise_()
        self.macdef.raise_()
        self.macdiag.raise_()
        self.toprep_menu.raise_()
        self.ppotext.raise_()
        self.execute_btn2_2.raise_()
        self.label.raise_()
        self.langpage = QWidget()
        self.langpage.setObjectName(u"langpage")
        self.filetitle_2 = QLabel(self.langpage)
        self.filetitle_2.setObjectName(u"filetitle_2")
        self.filetitle_2.setGeometry(QRect(40, 60, 291, 51))
        self.filetitle_2.setFont(font6)
        self.macdef_2 = QTextBrowser(self.langpage)
        self.macdef_2.setObjectName(u"macdef_2")
        self.macdef_2.setGeometry(QRect(40, 230, 1131, 201))
        self.macdef_2.setFont(font2)
        self.langdiag1 = QLabel(self.langpage)
        self.langdiag1.setObjectName(u"langdiag1")
        self.langdiag1.setGeometry(QRect(260, 120, 521, 51))
        self.langdiag1.setPixmap(QPixmap(u":/newPrefix/langdiag1.png"))
        self.langdiag2 = QLabel(self.langpage)
        self.langdiag2.setObjectName(u"langdiag2")
        self.langdiag2.setGeometry(QRect(260, 160, 891, 51))
        self.langdiag2.setPixmap(QPixmap(u":/newPrefix/langdiag2.png"))
        self.toprep_menu_3 = QPushButton(self.langpage)
        self.toprep_menu_3.setObjectName(u"toprep_menu_3")
        self.toprep_menu_3.setGeometry(QRect(720, 450, 191, 51))
        self.toprep_menu_3.setFont(font12)
        self.toprep_menu_3.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget_2.addWidget(self.langpage)
        self.fileprep = QWidget()
        self.fileprep.setObjectName(u"fileprep")
        self.execute_btn2 = QPushButton(self.fileprep)
        self.execute_btn2.setObjectName(u"execute_btn2")
        self.execute_btn2.setGeometry(QRect(1070, 160, 111, 41))
        self.execute_btn2.setFont(font14)
        self.execute_btn2.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.filetitle = QLabel(self.fileprep)
        self.filetitle.setObjectName(u"filetitle")
        self.filetitle.setGeometry(QRect(30, 30, 241, 51))
        self.filetitle.setFont(font6)
        self.filedef_2 = QTextBrowser(self.fileprep)
        self.filedef_2.setObjectName(u"filedef_2")
        self.filedef_2.setGeometry(QRect(30, 90, 421, 241))
        font15 = QFont()
        font15.setPointSize(16)
        self.filedef_2.setFont(font15)
        self.trybox_2 = QTextBrowser(self.fileprep)
        self.trybox_2.setObjectName(u"trybox_2")
        self.trybox_2.setGeometry(QRect(870, 60, 311, 141))
        self.trybox_2.setFont(font10)
        self.trybox_2.setStyleSheet(u"border:1px solid yellow;")
        self.toprep_menu_2 = QPushButton(self.fileprep)
        self.toprep_menu_2.setObjectName(u"toprep_menu_2")
        self.toprep_menu_2.setGeometry(QRect(140, 370, 191, 51))
        self.toprep_menu_2.setFont(font12)
        self.toprep_menu_2.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.itfbox = QTextEdit(self.fileprep)
        self.itfbox.setObjectName(u"itfbox")
        self.itfbox.setGeometry(QRect(490, 60, 301, 381))
        self.itfbox.setFont(font13)
        self.itfbox.setStyleSheet(u"background-color: rgb(26, 24, 27);\n"
"color: #ffffff;\n"
"border: 2px solid red;")
        self.filetitle_3 = QLabel(self.fileprep)
        self.filetitle_3.setObjectName(u"filetitle_3")
        self.filetitle_3.setGeometry(QRect(950, 200, 241, 51))
        self.filetitle_3.setFont(font4)
        self.fiotext = QTextEdit(self.fileprep)
        self.fiotext.setObjectName(u"fiotext")
        self.fiotext.setGeometry(QRect(870, 260, 311, 171))
        self.fiotext.setFont(font13)
        self.fiotext.setStyleSheet(u"background-color: rgb(26, 24, 27);\n"
"color: #ffffff;\n"
"border: 2px solid purple;")
        self.fiotext.setReadOnly(True)
        self.label_3 = QLabel(self.fileprep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(620, 420, 49, 16))
        self.label_3.setStyleSheet(u"color: red;")
        self.stackedWidget_2.addWidget(self.fileprep)
        self.filetitle.raise_()
        self.filedef_2.raise_()
        self.toprep_menu_2.raise_()
        self.itfbox.raise_()
        self.filetitle_3.raise_()
        self.fiotext.raise_()
        self.trybox_2.raise_()
        self.execute_btn2.raise_()
        self.label_3.raise_()
        self.compilerdirectivepage = QWidget()
        self.compilerdirectivepage.setObjectName(u"compilerdirectivepage")
        self.comptitle_3 = QLabel(self.compilerdirectivepage)
        self.comptitle_3.setObjectName(u"comptitle_3")
        self.comptitle_3.setGeometry(QRect(40, 40, 241, 51))
        self.comptitle_3.setFont(font6)
        self.comdef_3 = QTextBrowser(self.compilerdirectivepage)
        self.comdef_3.setObjectName(u"comdef_3")
        self.comdef_3.setGeometry(QRect(40, 120, 421, 331))
        self.comdef_3.setFont(font15)
        self.compdiag_4 = QLabel(self.compilerdirectivepage)
        self.compdiag_4.setObjectName(u"compdiag_4")
        self.compdiag_4.setGeometry(QRect(640, 110, 451, 241))
        self.compdiag_4.setPixmap(QPixmap(u":/newPrefix/compdiag.png"))
        self.toprep_menu_4 = QPushButton(self.compilerdirectivepage)
        self.toprep_menu_4.setObjectName(u"toprep_menu_4")
        self.toprep_menu_4.setGeometry(QRect(800, 390, 191, 51))
        self.toprep_menu_4.setFont(font12)
        self.toprep_menu_4.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget_2.addWidget(self.compilerdirectivepage)
        self.stackedWidget.addWidget(self.prep)
        self.assembler = QWidget()
        self.assembler.setObjectName(u"assembler")
        self.asblr = QLabel(self.assembler)
        self.asblr.setObjectName(u"asblr")
        self.asblr.setGeometry(QRect(40, 50, 421, 101))
        self.asblr.setFont(font9)
        self.to_menu_2 = QPushButton(self.assembler)
        self.to_menu_2.setObjectName(u"to_menu_2")
        self.to_menu_2.setGeometry(QRect(950, 60, 231, 51))
        self.to_menu_2.setFont(font4)
        self.to_menu_2.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.asblrdesc = QTextBrowser(self.assembler)
        self.asblrdesc.setObjectName(u"asblrdesc")
        self.asblrdesc.setGeometry(QRect(40, 190, 611, 211))
        self.asblrdesc.setFont(font2)
        self.asblrdiag = QLabel(self.assembler)
        self.asblrdiag.setObjectName(u"asblrdiag")
        self.asblrdiag.setGeometry(QRect(40, 440, 611, 221))
        self.asblrdiag.setPixmap(QPixmap(u":/newPrefix/asblrdiag.png"))
        self.view_src = QPushButton(self.assembler)
        self.view_src.setObjectName(u"view_src")
        self.view_src.setGeometry(QRect(840, 590, 231, 51))
        self.view_src.setFont(font4)
        self.view_src.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.view_trans = QPushButton(self.assembler)
        self.view_trans.setObjectName(u"view_trans")
        self.view_trans.setGeometry(QRect(840, 530, 231, 51))
        self.view_trans.setFont(font4)
        self.view_trans.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget_3 = QStackedWidget(self.assembler)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(769, 179, 391, 281))
        self.translator = QWidget()
        self.translator.setObjectName(u"translator")
        self.inputline = QLineEdit(self.translator)
        self.inputline.setObjectName(u"inputline")
        self.inputline.setGeometry(QRect(10, 40, 361, 41))
        self.inputline.setFont(font11)
        self.inputprompt = QLabel(self.translator)
        self.inputprompt.setObjectName(u"inputprompt")
        self.inputprompt.setGeometry(QRect(10, 0, 241, 41))
        self.inputprompt.setFont(font11)
        self.outputline = QLineEdit(self.translator)
        self.outputline.setObjectName(u"outputline")
        self.outputline.setGeometry(QRect(10, 200, 361, 41))
        self.outputline.setFont(font13)
        self.outputline.setStyleSheet(u"color: rgb(223, 189, 54);")
        self.outputline.setReadOnly(True)
        self.outputline.setClearButtonEnabled(False)
        self.outputprompt = QLabel(self.translator)
        self.outputprompt.setObjectName(u"outputprompt")
        self.outputprompt.setGeometry(QRect(10, 160, 241, 41))
        self.outputprompt.setFont(font11)
        self.go = QPushButton(self.translator)
        self.go.setObjectName(u"go")
        self.go.setGeometry(QRect(320, 90, 51, 31))
        font16 = QFont()
        font16.setPointSize(11)
        font16.setBold(True)
        self.go.setFont(font16)
        self.go.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget_3.addWidget(self.translator)
        self.outputprompt.raise_()
        self.inputprompt.raise_()
        self.inputline.raise_()
        self.outputline.raise_()
        self.go.raise_()
        self.limitations = QWidget()
        self.limitations.setObjectName(u"limitations")
        self.limtext = QLabel(self.limitations)
        self.limtext.setObjectName(u"limtext")
        self.limtext.setGeometry(QRect(0, 5, 371, 261))
        font17 = QFont()
        font17.setPointSize(18)
        font17.setBold(True)
        font17.setUnderline(True)
        self.limtext.setFont(font17)
        self.limtext.setStyleSheet(u"border: 1px solid white")
        self.limtext.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.limtext.setWordWrap(True)
        self.textBrowser = QTextBrowser(self.limitations)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(15, 60, 341, 192))
        self.textBrowser.setFont(font11)
        self.textBrowser.setStyleSheet(u"border: 0px solid black;")
        self.stackedWidget_3.addWidget(self.limitations)
        self.view_lim = QPushButton(self.assembler)
        self.view_lim.setObjectName(u"view_lim")
        self.view_lim.setGeometry(QRect(840, 470, 231, 51))
        self.view_lim.setFont(font4)
        self.view_lim.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget.addWidget(self.assembler)
        self.stackedWidget_3.raise_()
        self.asblr.raise_()
        self.to_menu_2.raise_()
        self.asblrdesc.raise_()
        self.asblrdiag.raise_()
        self.view_src.raise_()
        self.view_trans.raise_()
        self.view_lim.raise_()
        self.asblrsrc = QWidget()
        self.asblrsrc.setObjectName(u"asblrsrc")
        self.asblr_2 = QLabel(self.asblrsrc)
        self.asblr_2.setObjectName(u"asblr_2")
        self.asblr_2.setGeometry(QRect(40, 50, 501, 101))
        self.asblr_2.setFont(font9)
        self.to_menu_6 = QPushButton(self.asblrsrc)
        self.to_menu_6.setObjectName(u"to_menu_6")
        self.to_menu_6.setGeometry(QRect(950, 60, 231, 51))
        self.to_menu_6.setFont(font4)
        self.to_menu_6.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.asblrdesc_2 = QTextBrowser(self.asblrsrc)
        self.asblrdesc_2.setObjectName(u"asblrdesc_2")
        self.asblrdesc_2.setGeometry(QRect(40, 190, 571, 501))
        self.asblrdesc_2.setFont(font2)
        self.asblrdesc_3 = QTextBrowser(self.asblrsrc)
        self.asblrdesc_3.setObjectName(u"asblrdesc_3")
        self.asblrdesc_3.setGeometry(QRect(630, 190, 631, 321))
        font18 = QFont()
        font18.setPointSize(18)
        font18.setKerning(True)
        self.asblrdesc_3.setFont(font18)
        self.to_asblrmenu = QPushButton(self.asblrsrc)
        self.to_asblrmenu.setObjectName(u"to_asblrmenu")
        self.to_asblrmenu.setGeometry(QRect(760, 580, 351, 51))
        self.to_asblrmenu.setFont(font4)
        self.to_asblrmenu.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget.addWidget(self.asblrsrc)
        self.linker = QWidget()
        self.linker.setObjectName(u"linker")
        self.linkertitle = QLabel(self.linker)
        self.linkertitle.setObjectName(u"linkertitle")
        self.linkertitle.setGeometry(QRect(40, 60, 421, 101))
        self.linkertitle.setFont(font9)
        self.to_menu_3 = QPushButton(self.linker)
        self.to_menu_3.setObjectName(u"to_menu_3")
        self.to_menu_3.setGeometry(QRect(970, 50, 231, 51))
        self.to_menu_3.setFont(font4)
        self.to_menu_3.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.linkdiag = QLabel(self.linker)
        self.linkdiag.setObjectName(u"linkdiag")
        self.linkdiag.setGeometry(QRect(60, 210, 541, 431))
        self.linkdiag.setPixmap(QPixmap(u":/newPrefix/linkerdiag.png"))
        self.linkdef_3 = QTextBrowser(self.linker)
        self.linkdef_3.setObjectName(u"linkdef_3")
        self.linkdef_3.setGeometry(QRect(660, 240, 491, 281))
        self.linkdef_3.setFont(font2)
        self.to_loader = QPushButton(self.linker)
        self.to_loader.setObjectName(u"to_loader")
        self.to_loader.setGeometry(QRect(790, 550, 231, 51))
        self.to_loader.setFont(font4)
        self.to_loader.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget.addWidget(self.linker)
        self.loader = QWidget()
        self.loader.setObjectName(u"loader")
        self.loadtitle = QLabel(self.loader)
        self.loadtitle.setObjectName(u"loadtitle")
        self.loadtitle.setGeometry(QRect(40, 60, 421, 101))
        self.loadtitle.setFont(font9)
        self.loaddef = QTextBrowser(self.loader)
        self.loaddef.setObjectName(u"loaddef")
        self.loaddef.setGeometry(QRect(40, 180, 1201, 211))
        self.loaddef.setFont(font2)
        self.loaddiag = QLabel(self.loader)
        self.loaddiag.setObjectName(u"loaddiag")
        self.loaddiag.setGeometry(QRect(40, 420, 721, 251))
        self.loaddiag.setPixmap(QPixmap(u":/newPrefix/loaderdiag.png"))
        self.to_menu_5 = QPushButton(self.loader)
        self.to_menu_5.setObjectName(u"to_menu_5")
        self.to_menu_5.setGeometry(QRect(970, 50, 231, 51))
        self.to_menu_5.setFont(font4)
        self.to_menu_5.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.to_linker = QPushButton(self.loader)
        self.to_linker.setObjectName(u"to_linker")
        self.to_linker.setGeometry(QRect(910, 520, 231, 51))
        self.to_linker.setFont(font4)
        self.to_linker.setStyleSheet(u"\n"
"border: 1px solid white;")
        self.stackedWidget.addWidget(self.loader)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(3)
        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CDProjekt", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"COMPILER DESIGN PROJECT", None))
        self.by.setText(QCoreApplication.translate("MainWindow", u"By", None))
        self.names.setText(QCoreApplication.translate("MainWindow", u"Aryan Sinha (RA2011003010066)\n"
"Shruthi Kannan (RA2011003010037)", None))
        self.topic.setText(QCoreApplication.translate("MainWindow", u"TOPIC:    COUSINS OF COMPILERS", None))
        self.go_btn.setText(QCoreApplication.translate("MainWindow", u"BEGIN", None))
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u"QUIT", None))
        self.disc.setText(QCoreApplication.translate("MainWindow", u"This mini-project is meant to help users quickly go through and deeply understand the Cousins of Compilers concept in an interactive and easy-to-digest manner. Current functionality includes explanations to all cousin components, and a brief look at the inner workings of Assemblers and Pre-Processors.\n"
"\n"
"This software will continue to be worked on on our github page \n"
"\"https://github.com/terrablast95/Cousins-Of-Compilers-Sim\"\n"
"and we hope to expand the scope of this project to eventually encompass all concepts of CD, including visual aids on what each component of the compiler is internally doing; to deepen our understand of the compilers.\n"
"\n"
"We encourage you all to try out and leave feedback and recommendations on our software, or even collaborate :D", None))
        self.continue_btn.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Introduction", None))
        self.menu_head.setText(QCoreApplication.translate("MainWindow", u"     CHOOSE YOUR CoC!", None))
        self.prep_btn.setText(QCoreApplication.translate("MainWindow", u"PRE-PROCESSOR", None))
        self.linker_btn.setText(QCoreApplication.translate("MainWindow", u"LINKER", None))
        self.loader_btn.setText(QCoreApplication.translate("MainWindow", u"LOADER", None))
        self.assembler_btn.setText(QCoreApplication.translate("MainWindow", u"ASSEMBLER", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"home", None))
        self.to_menu.setText(QCoreApplication.translate("MainWindow", u"<--  Back To Menu", None))
        self.prep_home.setText(QCoreApplication.translate("MainWindow", u"PRE-PROCESSOR:", None))
        self.desc.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A pre-processor is a program or a set of instructions that processes the source code before it is compiled. The purpose of a pre-processor is to modify or manipulate the source code in some way to make it easier to compile or to improve the efficiency of the compiled program.</p></body></html>", None))
        self.prepdiag.setText("")
        self.macro_btn.setText(QCoreApplication.translate("MainWindow", u"Macro Processing", None))
        self.file_btn.setText(QCoreApplication.translate("MainWindow", u"File Inclusion", None))
        self.lang_btn.setText(QCoreApplication.translate("MainWindow", u"Language Extension", None))
        self.comp_btn.setText(QCoreApplication.translate("MainWindow", u"Compiler Directive", None))
        self.itpbox.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.mactitle.setText(QCoreApplication.translate("MainWindow", u"Macro Processing", None))
        self.macdef.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">A macro processor is a program that processes text input and performs operations on it, such as replacing certain text patterns with predefined strings or code. It is commonly used in software development to simplify repetitive tasks and improve code readability.</span></p></body></html>", None))
        self.macdiag.setText("")
        self.toprep_menu.setText(QCoreApplication.translate("MainWindow", u"<--  To Pre-processor Menu", None))
        self.mactitle_2.setText(QCoreApplication.translate("MainWindow", u"Macros Declared:", None))
        self.ppotext.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400;\"><br /></p></body></html>", None))
        self.trybox_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">TRY OUT OUR INTERACTIVE TEXT BOX!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Type some code, and press the button; and we will show you which lines take part in Macro Processing!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p></body></html>", None))
        self.execute_btn2_2.setText(QCoreApplication.translate("MainWindow", u"Go -->", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextBox", None))
        self.filetitle_2.setText(QCoreApplication.translate("MainWindow", u"Language  extension", None))
        self.macdef_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In preprocessing, language extension refers to the ability to add new features or syntax to a programming language through the use of preprocessor directives or macros. This can be useful for extending the functionality of a language or making it more expressive, but it can also make code harder to read and maintain. Examples of language extensions include adding new data types, defining new control "
                        "structures, or creating new ways to handle error conditions.</p></body></html>", None))
        self.langdiag1.setText("")
        self.langdiag2.setText("")
        self.toprep_menu_3.setText(QCoreApplication.translate("MainWindow", u"<--  To Pre-processor Menu", None))
        self.execute_btn2.setText(QCoreApplication.translate("MainWindow", u"Go -->", None))
        self.filetitle.setText(QCoreApplication.translate("MainWindow", u"File Inclusion", None))
        self.filedef_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">File inclusion is a process in compilers where a source code file includes the contents of another file during the compilation process. This allows the compiler to access the code in the included file as if it were part of the original source file, improving code reusability and modularity.</p></body></html>", None))
        self.trybox_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">TRY OUT OUR INTERACTIVE TEXT BOX!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Type some code, and press the button; and we will show you which lines take part in File Inclusion!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p></body></html>", None))
        self.toprep_menu_2.setText(QCoreApplication.translate("MainWindow", u"<--  To Pre-processor Menu", None))
        self.itfbox.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400;\"><br /></p></body></html>", None))
        self.filetitle_3.setText(QCoreApplication.translate("MainWindow", u"Files Included:", None))
        self.fiotext.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextBox", None))
        self.comptitle_3.setText(QCoreApplication.translate("MainWindow", u"Compiler Directive:", None))
        self.comdef_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Compiler directives are instructions to the compiler that are processed before compilation. They are used to control how the code is compiled, optimize the output, or provide additional information to the compiler.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">They are typically declared via #[directive-name]</p>\n"
"<"
                        "p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here are some of the most commonly used directives.</p></body></html>", None))
        self.compdiag_4.setText("")
        self.toprep_menu_4.setText(QCoreApplication.translate("MainWindow", u"<--  To Pre-processor Menu", None))
        self.asblr.setText(QCoreApplication.translate("MainWindow", u"ASSEMBLER:", None))
        self.to_menu_2.setText(QCoreApplication.translate("MainWindow", u"<--  Back To Menu", None))
        self.asblrdesc.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Assemblers are programs that translate assembly language into machine code, which is the low-level language that a computer can understand. Assemblers are typically used as the first step in compiling code for a specific architecture.</p></body></html>", None))
        self.asblrdiag.setText("")
        self.view_src.setText(QCoreApplication.translate("MainWindow", u"View Source", None))
        self.view_trans.setText(QCoreApplication.translate("MainWindow", u"View Translator", None))
        self.inputline.setText("")
        self.inputprompt.setText(QCoreApplication.translate("MainWindow", u"Enter a single-lined instruction:", None))
        self.outputline.setText("")
        self.outputprompt.setText(QCoreApplication.translate("MainWindow", u"Machine-Code Translation:", None))
        self.go.setText(QCoreApplication.translate("MainWindow", u"Go ->", None))
        self.limtext.setText(QCoreApplication.translate("MainWindow", u"LIMITATIONS:", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">This is a very basic translator with limited functionality. It supports a limited set of instructions, and registers; and only shows what the computer reads when the assembler is done processing the source text file.</span></p></body></html>", None))
        self.view_lim.setText(QCoreApplication.translate("MainWindow", u"View Limitations", None))
        self.asblr_2.setText(QCoreApplication.translate("MainWindow", u"ASSEMBLER (Source):", None))
        self.to_menu_6.setText(QCoreApplication.translate("MainWindow", u"<--  Back To Menu", None))
        self.asblrdesc_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">def generate_machine_code(self, text):</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    OPCODES = {</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" font-size:12pt;\">	&quot;add&quot;: &quot;0001&quot;,</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">	&quot;mov&quot;: &quot;0010&quot;,</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">	&quot;sub&quot;: &quot;0011&quot;,</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">	&quot;jmp&quot;: &quot;0100&quot;,.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                    . . .</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" font-size:12pt;\">	}</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    instruction_parts = text.split()</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    if instruction_parts[0] not in OPCODES.keys() or len(instruction_parts) != 3:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    self.ui.lineEdit_2.setText(&quot;Invalid instruction!&quot;)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    return</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br /></span></p></body></html>", None))
        self.asblrdesc_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><a name=\"docs-internal-guid-4485387d-7fff-4b56-a724-ab66b52df3c6\"></a><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">\u00a0</span><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">opcode = OPCODES[instruction_parts[0]]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0register_value = bin(int(instruction_parts[1][1:]))[2:].zfill(3)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0constant_value = bin(int(instruction_parts[2]))[2:].zfill(8)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0if opcode == &quot;0100&quot;:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0machine_code = opcode + &quot;000&quot; + constant_value</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0else:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0machine_code = opcode + register_value + constant_value</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px; line-height:180%;\"><span style=\" font-family:'Arial'; font-size:11pt; color:#ffffff; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0self.ui.lineEdit_2.setText(machine_code)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"><br /></span></p></body></html>", None))
        self.to_asblrmenu.setText(QCoreApplication.translate("MainWindow", u"<--  Back To Assembler Menu", None))
        self.linkertitle.setText(QCoreApplication.translate("MainWindow", u"LINKER:", None))
        self.to_menu_3.setText(QCoreApplication.translate("MainWindow", u"<--  Back To Menu", None))
        self.linkdiag.setText("")
        self.linkdef_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Linkers are programs that combine multiple object files generated by the compiler into a single executable file. They resolve external references between object files, assign memory locations to instructions and data, and generate relocation information. Linkers also perform dead code elimination and symbol resolution.</p></body></html>", None))
        self.to_loader.setText(QCoreApplication.translate("MainWindow", u"Go To Loader -->", None))
        self.loadtitle.setText(QCoreApplication.translate("MainWindow", u"LOADER:", None))
        self.loaddef.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Loaders are programs that load an executable file into memory for execution. They are the final step in the compilation process, and their primary role is to resolve the symbolic references between the modules in the program. Loaders also allocate memory for the program, set up the program's stack and heap, and start the program's execution. Additionally, they perform various security checks to ensur"
                        "e that the loaded program does not violate system security policies. Overall, loaders are crucial in ensuring that the compiled program runs smoothly and securely on the target system.</p></body></html>", None))
        self.loaddiag.setText("")
        self.to_menu_5.setText(QCoreApplication.translate("MainWindow", u"<--  Back To Menu", None))
        self.to_linker.setText(QCoreApplication.translate("MainWindow", u"<-- Go to Linker", None))
    # retranslateUi

