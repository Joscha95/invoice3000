from PyQt5 import QtCore, QtGui, QtWidgets
from helpers import find
from createPDF import PDF
import re
import json
from datetime import datetime

class Ui_Rechnung3000(object):
    def setupUi(self, Rechnung3000,customers,selectedIndex):
        self.Rechnung3000=Rechnung3000
        self.Rechnung3000.setObjectName("Rechnung3000")
        self.Rechnung3000.resize(523, 738)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Rechnung3000.sizePolicy().hasHeightForWidth())
        self.Rechnung3000.setSizePolicy(sizePolicy)
        self.Rechnung3000.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(self.Rechnung3000)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.main_layout.setContentsMargins(0, -1, 0, -1)
        self.main_layout.setSpacing(1)
        self.main_layout.setObjectName("main_layout")
        self.body_header = QtWidgets.QHBoxLayout()
        self.body_header.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.body_header.setObjectName("body_header")
        self.invoice_nr_label = QtWidgets.QLabel(self.Rechnung3000)
        self.invoice_nr_label.setObjectName("invoice_nr_label")
        self.body_header.addWidget(self.invoice_nr_label)
        self.invoice_nr = QtWidgets.QTextEdit(self.Rechnung3000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoice_nr.sizePolicy().hasHeightForWidth())
        self.invoice_nr.setSizePolicy(sizePolicy)
        self.invoice_nr.setMaximumSize(QtCore.QSize(120, 20))
        self.invoice_nr.setObjectName("invoice_nr")
        self.body_header.addWidget(self.invoice_nr)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.body_header.addItem(spacerItem1)
        self.customer_nr = QtWidgets.QLabel(self.Rechnung3000)
        self.customer_nr.setObjectName("customer_nr")
        self.body_header.addWidget(self.customer_nr)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.body_header.addItem(spacerItem2)
        self.invoice_date = QtWidgets.QTextEdit(self.Rechnung3000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoice_date.sizePolicy().hasHeightForWidth())
        self.invoice_date.setSizePolicy(sizePolicy)
        self.invoice_date.setMaximumSize(QtCore.QSize(120, 20))
        self.invoice_date.setObjectName("invoice_date")
        self.body_header.addWidget(self.invoice_date)
        self.main_layout.addLayout(self.body_header)
        self.body = QtWidgets.QTableWidget(self.Rechnung3000)
        self.body.setObjectName("body")
        self.body.setColumnCount(2)
        self.body.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.body.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.body.setHorizontalHeaderItem(1, item)
        self.main_layout.addWidget(self.body)
        self.main_layout.setStretch(1, 1)
        self.gridLayout.addLayout(self.main_layout, 2, 0, 1, 2)
        self.customer_adress = QtWidgets.QLabel(self.Rechnung3000)
        self.customer_adress.setMinimumSize(QtCore.QSize(185, 107))
        self.customer_adress.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.customer_adress.setObjectName("customer_adress")
        self.gridLayout.addWidget(self.customer_adress, 1, 0, 1, 1)
        self.sum_layout = QtWidgets.QHBoxLayout()
        self.sum_layout.setObjectName("sum_layout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sum_layout.addItem(spacerItem3)
        self.add_pos_bt = QtWidgets.QPushButton(self.Rechnung3000)
        self.add_pos_bt.setMinimumSize(QtCore.QSize(50, 0))
        self.add_pos_bt.setAutoDefault(True)
        self.add_pos_bt.setFlat(False)
        self.add_pos_bt.setObjectName("add_pos_bt")
        self.sum_layout.addWidget(self.add_pos_bt)
        self.remove_pos_bt = QtWidgets.QPushButton(self.Rechnung3000)
        self.remove_pos_bt.setAutoDefault(True)
        self.remove_pos_bt.setDefault(False)
        self.remove_pos_bt.setFlat(False)
        self.remove_pos_bt.setObjectName("remove_pos_bt")
        self.sum_layout.addWidget(self.remove_pos_bt)
        self.sum_label = QtWidgets.QLabel(self.Rechnung3000)
        self.sum_label.setObjectName("sum_label")
        self.sum_layout.addWidget(self.sum_label)
        self.gridLayout.addLayout(self.sum_layout, 3, 0, 1, 2)
        self.save_bt = QtWidgets.QPushButton(self.Rechnung3000)
        self.save_bt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.save_bt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.save_bt.setObjectName("save_bt")
        self.gridLayout.addWidget(self.save_bt, 4, 1, 1, 1)
        self.select_customer = QtWidgets.QComboBox(self.Rechnung3000)
        self.select_customer.setFrame(True)
        self.select_customer.setObjectName("select_customer")
        self.gridLayout.addWidget(self.select_customer, 0, 0, 1, 1)

        # select customer + display data


        self.customers = customers

        inv_num = int(open("data/invoice_number.txt", "r").read())
        self.invoice_nr.setText(str(inv_num+1))
        self.body.horizontalHeader().setStretchLastSection(True)
        self.body.itemChanged.connect(self.cellEdited)
        self.body.setColumnWidth(0,self.body.width()*3.5)

        self.add_pos_bt.clicked.connect(self.addPos)
        self.remove_pos_bt.clicked.connect(self.removePos)

        self.save_bt.clicked.connect(self.savePDF)

        self.select_customer.currentIndexChanged.connect(self.updateCustomerData)
        for customer in self.customers:
            self.select_customer.addItem(customer["name"])


        self.retranslateUi(Rechnung3000,selectedIndex)
        QtCore.QMetaObject.connectSlotsByName(self.Rechnung3000)

    def retranslateUi(self, Rechnung3000,selectedIndex):
        _translate = QtCore.QCoreApplication.translate
        self.Rechnung3000.setWindowTitle(_translate("Rechnung3000", "Rechnung3000"))
        self.invoice_nr_label.setText(_translate("Rechnung3000", "Nr."))
        self.customer_nr.setText(_translate("Rechnung3000", "KundenNr."))
        item = self.body.horizontalHeaderItem(0)
        item.setText(_translate("Rechnung3000", "Leistung"))
        item = self.body.horizontalHeaderItem(1)
        item.setText(_translate("Rechnung3000", "Preis"))
        self.customer_adress.setText(_translate("Rechnung3000", "Address"))
        self.add_pos_bt.setText(_translate("Rechnung3000", "+"))
        self.remove_pos_bt.setText(_translate("Rechnung3000", "–"))
        self.sum_label.setText(_translate("Rechnung3000", "Gesamt 000,00€"))
        self.save_bt.setText(_translate("Rechnung3000", "Save"))

        self.updateCustomerData(selectedIndex)
        self.select_customer.setCurrentIndex(selectedIndex)
        self.invoice_date.setText(datetime.now().strftime("%d.%m.%Y"))


    def updateCustomerData(self,index):
        _c=self.customers[index]["data"]
        self.active_customer = self.customers[index]
        customer_adress=""+self.customers[index]["name"]+"\n"+_c["street"]+"\n"+_c["zip"]+" "+_c["city"]
        self.customer_adress.setText(customer_adress)
        self.customer_nr.setText('KundenNr.: {:0>3}'.format(_c["number"]))

    def addPos(self):
        self.body.insertRow(self.body.rowCount())

    def removePos(self):
        self.body.removeRow(self.body.rowCount()-1)
        self.cellEdited()

    def setCustomers(self,customers):
        self.customers=customers
        self.select_customer.clear()
        for customer in self.customers:
            self.select_customer.addItem(customer["name"])

    def saveTxt(self):
        if self.body.rowCount()<1 or self.sum_label.text()=='Gesamt 000,00€':
            print('no values')
            return

        d=""
        d+=self.customer_adress.text()
        d+='\n\n\nRechnung\n'

        for x in range(self.body.rowCount()):
            lei = self.body.item(x,0).text() if self.body.item(x,0) else '-'
            prei = self.body.item(x,1).text() if self.body.item(x,1) else '0'
            num = re.findall(r'\d+', prei)[0] if re.findall(r'\d+', prei) else 0

            d+=str(x)+'. '+lei +' '+'{:,.2f}€'.format(float(num))+'\n'

        d+='\n'+self.sum_label.text()
        f = open("data/invoices/R_"+self.active_customer["short"]+"_"+self.invoice_nr.toPlainText()+".txt", "w")
        f.write(d)
        f.close()

        f = open("data/invoice_number.txt", "w")
        f.write(self.invoice_nr.toPlainText())
        f.close()
        print('saved!')

    def savePDF(self):
        if self.body.rowCount()<1 or self.sum_label.text()=='Gesamt 000,00€':
            print('no values')
            return

        pdf = PDF(orientation='P', unit='mm', format='A4')
        invoicedata = {
            'number':self.invoice_nr.toPlainText(),
            'client': self.customer_adress.text(),
            'invoiceHeader': ('NR. {}'.format(self.invoice_nr.toPlainText()),self.customer_nr.text(),self.invoice_date.toPlainText()),
            'invoiceData':[
                ("Pos.", "Leistung", "Gesamtpreis")
            ],
            'sum': self.sum_label.text().replace('€','E')
        }

        for x in range(self.body.rowCount()):

            lei = self.body.item(x,0).text() if self.body.item(x,0) else '-'
            prei = self.body.item(x,1).text() if self.body.item(x,1) else '0'
            num = re.findall(r'\d+', prei)[0] if re.findall(r'\d+', prei) else 0
            num = '{:,.2f}E'.format(float(num))

            r=('{:0>2}'.format(x+1),lei,num)

            invoicedata['invoiceData'].append(r)

        pdf.newInvoice(invoicedata)
        pdf.output("data/invoices/R_"+self.active_customer["short"]+"_"+self.invoice_nr.toPlainText()+".pdf",'F')

        f = open("data/invoice_number.txt", "w")
        f.write(self.invoice_nr.toPlainText())
        f.close()
        print('saved!')
        self.Rechnung3000.reject()

    def cellEdited(self):
        amount=0.00;
        for x in range(self.body.rowCount()):
            d = self.body.item(x,1).text() if self.body.item(x,1) else '0'
            num = re.findall(r'\d+', d)[0] if re.findall(r'\d+', d) else 0
            amount+=float(num)
        print(amount)
        self.sum_label.setText('Gesamt: {:,.2f}€'.format(amount))