import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QStackedWidget
from PySide6.QtGui import QTextCursor, QTextCharFormat
from PySide6.QtCore import Qt
from mainwindow_ui import Ui_MainWindow
from PySide6.QtGui import QTextDocument, QColor
from PySide6.QtWidgets import QTextEdit

def assemble(asm):
    parts = asm.split()
    opcode = parts[0]
    opcode = opcode.lower()
    if opcode == 'mov':
        op = '0001'
    elif opcode == 'add':
        op = '0010'
    elif opcode == 'sub':
        op = '0011'
    elif opcode == 'jmp':
        op = '0100'
    elif opcode == 'mul':
        op = '0101'
    elif opcode == 'div':
        op = '0110'
    elif opcode == 'and':
        op = '0111'
    elif opcode == 'or':
        op = '1000'
    elif opcode == 'xor':
        op = '1001'
    elif opcode == 'not':
        op = '1010'
    elif opcode == 'push':
        op = '1011'
    elif opcode == 'pop':
        op = '1100'
    elif opcode == 'load':
        op = '1101'
    elif opcode == 'store':
        op = '1110'
    else:
        raise ValueError(f"Unknown opcode: {opcode}")

    r1 = f"{int(parts[1][1]):03b}"
    if len(parts) == 3:
        const = f"{int(parts[2]):08b}"
    else:
        const = '00000000'

    if opcode in ['push', 'pop', 'load', 'store']:
        return f"{op} {r1} 00000000"
    else:
        return f"{op} {r1} {const}"
    
    

class mainwindow:
    def __init__(self):
        self.main_win=QMainWindow()
        self.ui=Ui_MainWindow()
        
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)

        self.ui.prep_btn.clicked.connect(self.showprep)
        self.ui.to_asblrmenu.clicked.connect(self.showasm)
        self.ui.to_menu.clicked.connect(self.showmenu)
        self.ui.to_menu_2.clicked.connect(self.showmenu)
        self.ui.to_menu_3.clicked.connect(self.showmenu)
        self.ui.to_menu_5.clicked.connect(self.showmenu)
        self.ui.to_menu_6.clicked.connect(self.showmenu)
        self.ui.view_lim.clicked.connect(self.showlim)
        self.ui.view_src.clicked.connect(self.showsrc)
        self.ui.view_trans.clicked.connect(self.showtrans)
        self.ui.continue_btn.clicked.connect(self.showmenu)
        self.ui.go_btn.clicked.connect(self.showdisc)
        self.ui.to_loader.clicked.connect(self.showloader)
        self.ui.to_linker.clicked.connect(self.showlinker)
        self.ui.assembler_btn.clicked.connect(self.showasm)
        self.ui.home_btn.clicked.connect(self.showhome)
        self.ui.linker_btn.clicked.connect(self.showlinker)
        self.ui.loader_btn.clicked.connect(self.showloader)
        self.ui.view_lim.clicked.connect(self.showlim)
        self.ui.toprep_menu.clicked.connect(self.showprep)
        self.ui.toprep_menu_2.clicked.connect(self.showprep)
        self.ui.toprep_menu_3.clicked.connect(self.showprep)
        self.ui.toprep_menu_4.clicked.connect(self.showprep)
        self.ui.comp_btn.clicked.connect(self.showcomp)
        self.ui.file_btn.clicked.connect(self.showfil)
        self.ui.lang_btn.clicked.connect(self.showlang)
        self.ui.macro_btn.clicked.connect(self.showmac)
        self.ui.go.clicked.connect(self.printans)
        self.ui.execute_btn2.clicked.connect(self.execute)
        self.ui.execute_btn2_2.clicked.connect(self.execute2)
        self.ui.quit_btn.clicked.connect(QApplication.quit)


    def show(self):
        self.main_win.show()

    
    def showmenu(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.menu)

    def showhome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)

    def showdisc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.disclaimer)

    def showprep(self):
        prep_stacked = self.ui.prep.findChild(QStackedWidget)
        prep_stacked.setCurrentWidget(self.ui.prepmenu)
        self.ui.stackedWidget.setCurrentWidget(self.ui.prep)     

    def showasm(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.assembler)

    def showlim(self):
        prep_stacked = self.ui.assembler.findChild(QStackedWidget)
        prep_stacked.setCurrentWidget(self.ui.limitations)
        self.ui.stackedWidget.setCurrentWidget(self.ui.assembler)

    def showsrc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.asblrsrc)

    def showtrans(self):
        prep_stacked = self.ui.assembler.findChild(QStackedWidget)
        prep_stacked.setCurrentWidget(self.ui.translator)
        self.ui.stackedWidget.setCurrentWidget(self.ui.assembler)

    def showloader(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loader)

    def showlinker(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.linker)

    def showcomp(self):
        prep_stacked = self.ui.prep.findChild(QStackedWidget)
        prep_stacked.setCurrentWidget(self.ui.compilerdirectivepage)
        self.ui.stackedWidget.setCurrentWidget(self.ui.prep)

    def showfil(self):
        prep_stacked = self.ui.prep.findChild(QStackedWidget)
        prep_stacked.setCurrentWidget(self.ui.fileprep)
        self.ui.stackedWidget.setCurrentWidget(self.ui.prep)

    def showlang(self):
        prep_stacked = self.ui.prep.findChild(QStackedWidget)
        prep_stacked.setCurrentWidget(self.ui.langpage)
        self.ui.stackedWidget.setCurrentWidget(self.ui.prep)

    def showmac(self):
        prep_stacked = self.ui.prep.findChild(QStackedWidget)
        prep_stacked.setCurrentWidget(self.ui.macro)
        self.ui.stackedWidget.setCurrentWidget(self.ui.prep)

    def printans(self):
        asm=self.ui.inputline.text()
        try:
             machine_code = assemble(asm)
             self.ui.outputline.setText(machine_code)
        except Exception as e:
             self.ui.outputline.setText(str(e))

    def execute(self):
        itfbox_text = self.ui.itfbox.toPlainText()
        lines = itfbox_text.split('\n')
        fiotext_text = ''
        for line in lines:
            if '#include' in line:
                include_str = line[line.find('#include')+8:].strip()
                if include_str.startswith('"') and include_str.endswith('"'):
                    fiotext_text += include_str[1:-1] + '\n'
                elif include_str.startswith('<') and include_str.endswith('>'):
                    fiotext_text += include_str[1:-1] + '\n'
        self.ui.fiotext.setPlainText(fiotext_text)

    def execute2(self):
        self.ui.ppotext.clear()
        text = self.ui.itpbox.toPlainText()
        lines = text.split("\n")
        for line in lines:
            if line.startswith("#def"):
                words = line.split()
                macro = words[1]
                value = " ".join(words[2:])
                self.ui.ppotext.append(f"Macro: {macro}, Value: {value}")


    
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    main_win=mainwindow()
    main_win.show()
    sys.exit(app.exec())




