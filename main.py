import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("tg_messages_table_gui.ui", self)
        self.tableWidget.setColumnWidth(0, 250)
        self.loaddata()

    def loaddata(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(850)
    widget.setFixedWidth(1120)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
