from PyQt5 import QtCore, QtGui, QtWidgets
from invoice import Ui_Rechnung3000
import json
import re


class Ui_Clients(object):
    def setupUi(self, Clients):
        Clients.setObjectName("Clients")
        Clients.resize(728, 640)
        self.clients_wrapper = QtWidgets.QGridLayout(Clients)
        self.clients_wrapper.setObjectName("clients_wrapper")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.client_list = QtWidgets.QTableWidget(Clients)
        self.client_list.setObjectName("client_list")
        self.client_list.setColumnCount(6)
        self.client_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.client_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.client_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.client_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.client_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.client_list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.client_list.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.client_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.remove_client_bt = QtWidgets.QPushButton(Clients)
        self.remove_client_bt.setEnabled(True)
        self.remove_client_bt.setFlat(True)
        self.remove_client_bt.setObjectName("remove_client_bt")
        self.horizontalLayout.addWidget(self.remove_client_bt)
        self.add_client_bt = QtWidgets.QPushButton(Clients)
        self.add_client_bt.setEnabled(True)
        self.add_client_bt.setFlat(True)
        self.add_client_bt.setObjectName("add_client_bt")
        self.horizontalLayout.addWidget(self.add_client_bt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.clients_wrapper.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.new_invoice_bt = QtWidgets.QPushButton(Clients)
        self.new_invoice_bt.setObjectName("new_invoice_bt")
        self.clients_wrapper.addWidget(self.new_invoice_bt, 1, 0, 1, 1)

        with open('data/clients.json') as json_file:
            self.clients = json.load(json_file)

        self.client_list.setRowCount(len(self.clients))
        for index,customer in enumerate(self.clients):
            self.client_list.setItem(index,0,QtWidgets.QTableWidgetItem(customer["name"]))
            self.client_list.setItem(index,1,QtWidgets.QTableWidgetItem(customer["short"]))
            self.client_list.setItem(index,2,QtWidgets.QTableWidgetItem(customer["data"]["street"]))
            self.client_list.setItem(index,3,QtWidgets.QTableWidgetItem(customer["data"]["zip"]))
            self.client_list.setItem(index,4,QtWidgets.QTableWidgetItem(customer["data"]["city"]))
            self.client_list.setItem(index,5,QtWidgets.QTableWidgetItem('{:0>3}'.format(customer["data"]["number"])))
        self.client_list.itemChanged.connect(self.updateClients)

        self.client_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.client_list.resizeColumnsToContents()
        self.client_list.horizontalHeader().setStretchLastSection(True)


        self.add_client_bt.clicked.connect(self.addClient)
        self.remove_client_bt.clicked.connect(self.removeClient)

        self.new_invoice_bt.clicked.connect(self.newInvoice)

        self.retranslateUi(Clients)
        QtCore.QMetaObject.connectSlotsByName(Clients)

    def retranslateUi(self, Clients):
        _translate = QtCore.QCoreApplication.translate
        Clients.setWindowTitle(_translate("Clients", "Form"))
        item = self.client_list.horizontalHeaderItem(0)
        item.setText(_translate("Clients", "Name"))
        item = self.client_list.horizontalHeaderItem(1)
        item.setText(_translate("Clients", "Short"))
        item = self.client_list.horizontalHeaderItem(2)
        item.setText(_translate("Clients", "Straße"))
        item = self.client_list.horizontalHeaderItem(3)
        item.setText(_translate("Clients", "Zip"))
        item = self.client_list.horizontalHeaderItem(4)
        item.setText(_translate("Clients", "Stadt"))
        item = self.client_list.horizontalHeaderItem(5)
        item.setText(_translate("Clients", "Nummer"))
        self.remove_client_bt.setText(_translate("Clients", "-"))
        self.add_client_bt.setText(_translate("Clients", "+"))
        self.new_invoice_bt.setText(_translate("Clients", "Neue Rechnung"))

    def addClient(self):
        self.client_list.insertRow(self.client_list.rowCount())
        self.updateClients()

    def removeClient(self):
        rows = set()
        for index in self.client_list.selectedIndexes():
            rows.add(index.row())

        for row in sorted(rows, reverse=True):
            self.client_list.removeRow(row)
        self.updateClients()

    def updateClients(self):
        self.clients =[]
        for x in range(self.client_list.rowCount()):
            client = {"name":"","short":"","data":{"street":"","zip":"","city":"","number":""}}
            client["name"] = self.client_list.item(x,0).text() if self.client_list.item(x,0) else '-'
            client["short"] = self.client_list.item(x,1).text() if self.client_list.item(x,1) else '-'
            client["data"]["street"] = self.client_list.item(x,2).text() if self.client_list.item(x,2) else '-'
            client["data"]["zip"] = self.client_list.item(x,3).text() if self.client_list.item(x,3) else '-'
            client["data"]["city"] = self.client_list.item(x,4).text() if self.client_list.item(x,4) else '-'
            d = self.client_list.item(x,5).text() if self.client_list.item(x,5) else '-'
            num = re.findall(r'\d+', d)[0] if re.findall(r'\d+', d) else 0
            client["data"]["number"] = num
            self.clients.append(client)

        with open('data/clients.json', 'w') as outfile:
            json.dump(self.clients, outfile)

        try:
            self.newInvoice.setCustomers(self.clients)
        except Exception:
            pass

        print('clients updated')

    def newInvoice(self):
        try:
            self.Rechnung3000.reject()
        except Exception as e:
            print(e)
            pass
        self.Rechnung3000 = QtWidgets.QDialog()
        self.newInvoice = Ui_Rechnung3000()
        selectedIndex=self.client_list.selectedIndexes()[0].row() if self.client_list.selectedIndexes() else 0
        self.newInvoice.setupUi(self.Rechnung3000,self.clients,selectedIndex)
        self.Rechnung3000.show()
        self.Rechnung3000.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Clients = QtWidgets.QWidget()
    ui = Ui_Clients()
    ui.setupUi(Clients)
    Clients.show()
    sys.exit(app.exec_())