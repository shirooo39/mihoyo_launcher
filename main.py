try:
    import sys
    from PySide6.QtWidgets import QApplication
    from modules.ui_main import MainWindow
    from modules.clear_output import clear_output
except ImportError as import_error:
    print(
        'An error has occurred when importing modules!\n\n' + 
        f'>>> {import_error}'
    )

    exit()
except Exception as unknown_error:
    print(
        'An unknown error has occurred!\n\n' + 
        f'>>> {unknown_error}'
    )

    exit()
else:
    pass


def main():
    clear_output()

    app = QApplication([])
    MainWindow()
    app.exec()

    sys.exit()

if __name__ == '__main__':
    main()

