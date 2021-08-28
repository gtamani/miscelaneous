import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QTableWidgetItem


class example_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI.ui",self)

        # Activate button
        self.activate.setEnabled(True)
        self.activate.clicked.connect(self.fn_activate)

        # Desactivate button
        self.desactivate.setEnabled(False)
        self.desactivate.clicked.connect(self.fn_desactivate)

        # Add input
        self.spending_description.setPlaceholderText("Gasto")

        # Table

       

    def fn_activate(self):
        """ Activate button handler event """
        self.activate.setEnabled(False)
        self.desactivate.setEnabled(True)
        self.label.setText("Activado!")


    def fn_desactivate(self):
        """ Desctivate button handler event """
        self.desactivate.setEnabled(False)
        self.activate.setEnabled(True)
        self.label.setText("Desactivado!")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = example_GUI()
    GUI.show()
    sys.exit(app.exec_())