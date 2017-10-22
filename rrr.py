#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pprint

# symbol
# entry price
# stop price
# target price
# shares

# arr = []

# data = {}

# data['symbol'] = input("Symbol: ")
# data['entry'] = float(input("Entry Price: "))
# data['stop'] = float(input("Stop Price: "))
# data['target'] = float(input("Target Price: "))
# data['shares'] = int(input("Shares: "))

# data['risk_per_share'] = round(data['entry'] - data['stop'],2)
# data['reward_per_share'] = round(data['target'] - data['entry'],2)
# data['rrr'] = round(data['reward_per_share']/data['risk_per_share'],2)
# data['risk_dollars'] = data['shares']*data['risk_per_share']
# data['reward_dollars'] = data['shares']*data['reward_per_share']

# pprint.pprint(data)

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        symbolLabel = QLabel("Symbol:")
        entryLabel = QLabel("Entry:")
        stopLabel = QLabel("Stop:")
        targetLabel = QLabel("Target:")
        sharesLabel = QLabel("Shares:")

        self.symbolLine = QLineEdit()
        self.entryLine = QLineEdit()
        self.stopLine = QLineEdit()
        self.targetLine = QLineEdit()
        self.sharesLine = QLineEdit()

        self.submitButton = QPushButton("&Submit")

        buttonLayout1 = QVBoxLayout()

        symbolLayout = QHBoxLayout()
        symbolLayout.addWidget(symbolLabel)
        symbolLayout.addWidget(self.symbolLine)
        buttonLayout1.addLayout(symbolLayout)

        entryLayout = QHBoxLayout()
        entryLayout.addWidget(entryLabel)
        entryLayout.addWidget(self.entryLine)
        buttonLayout1.addLayout(entryLayout)

        stopLayout = QHBoxLayout()
        stopLayout.addWidget(stopLabel)
        stopLayout.addWidget(self.stopLine)
        buttonLayout1.addLayout(stopLayout)

        targetLayout = QHBoxLayout()
        targetLayout.addWidget(targetLabel)
        targetLayout.addWidget(self.targetLine)
        buttonLayout1.addLayout(targetLayout)

        sharesLayout = QHBoxLayout()
        sharesLayout.addWidget(sharesLabel)
        sharesLayout.addWidget(self.sharesLine)
        buttonLayout1.addLayout(sharesLayout)


        buttonLayout1.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.submitContact)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(("Symbol","Entry","Stop","Target","Shares","RiskPerShare","RewardPerShare","RRR","Risk Dollars","Reward Dollars"))
        buttonLayout1.addWidget(self.tableWidget)

        mainLayout = QGridLayout()
        mainLayout.setColumnStretch(0,1)
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Risk Reward Calculator")
        self.setGeometry(0, 0, 1100, 500)

    def submitContact(self):
        data = {}
        data['symbol'] = self.symbolLine.text()
        data['entry'] = float(self.entryLine.text())
        data['stop'] = float(self.stopLine.text())
        data['target'] = float(self.targetLine.text())
        data['shares'] = int(self.sharesLine.text())
        data['risk_per_share'] = round(data['entry'] - data['stop'],2)
        data['reward_per_share'] = round(data['target'] - data['entry'],2)
        data['rrr'] = round(data['reward_per_share']/data['risk_per_share'],2)
        data['risk_dollars'] = data['shares']*data['risk_per_share']
        data['reward_dollars'] = data['shares']*data['reward_per_share']
        pprint.pprint(data)

        if data['symbol'] == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please enter a symbol.")
            return
        else:
        	self.tableWidget.insertRow(0)
        	self.tableWidget.setItem(0,0, QTableWidgetItem(data['symbol']))
        	self.tableWidget.setItem(0,1, QTableWidgetItem(str(data['entry'])))
        	self.tableWidget.setItem(0,2, QTableWidgetItem(str(data['stop'])))
        	self.tableWidget.setItem(0,3, QTableWidgetItem(str(data['target'])))
        	self.tableWidget.setItem(0,4, QTableWidgetItem(str(data['shares'])))
        	self.tableWidget.setItem(0,5, QTableWidgetItem(str(data['risk_per_share'])))
        	self.tableWidget.setItem(0,6, QTableWidgetItem(str(data['reward_per_share'])))
        	self.tableWidget.setItem(0,7, QTableWidgetItem(str(data['rrr'])))
        	self.tableWidget.setItem(0,8, QTableWidgetItem(str(data['risk_dollars'])))
        	self.tableWidget.setItem(0,9, QTableWidgetItem(str(data['reward_dollars'])))

            # QMessageBox.information(self, "Success!",
            #                         "Hello %s!" % data['symbol'])

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())

