from clients import Ui_Clients
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Clients = QtWidgets.QDialog()
    ui = Ui_Clients()
    ui.setupUi(Clients)
    Clients.show()
    sys.exit(app.exec_())


