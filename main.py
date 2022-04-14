import sys
from PySide6.QtWidgets import QApplication
from modules.ui_main import MainWindow
from modules.clear_output import clear_output


def main():
    clear_output()
    app = QApplication([])
    MainWindow()
    app.exec()
    sys.exit()

    
if __name__ == '__main__':
    main()

