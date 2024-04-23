import sys
from PyQt5 import QtWidgets
from interfaces.interfaz1 import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(("Producto", "Precio", "Cantidad", "Descripción"))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        
    def showWarningMessage(self, title:str, message:str):
        # show a warning message with the title and message passed in a QMessageBox
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    


    def addTableRow(self):
        
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        # I want to make that the two headers labels each uses 50% of the table width

        producto = self.ui.l_producto.text()
        precio = self.ui.spn_precio.value()
        descripcion = self.ui.l_descrip.text()
        cantidad = self.ui.spn_cantidad.value()

        if not producto or not precio or not cantidad:
            self.showWarningMessage("Error", "Tienes campos vacíos")
            return
        # I want to add product and price to the table
        rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)
        self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(producto))
        self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(precio)))
        # add descripcion to the table
        self.ui.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(cantidad)))
        self.ui.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(descripcion))
        # add cantidad to the table
        # now update the row count and column count
        self.ui.tableWidget.setRowCount(rowPosition + 1)

    def generateFile(self):
        nro_presupuesto = self.ui.l_presu.text()
        nombre = self.ui.l_nombre.text()
        apellido = self.ui.l_apellido.text()
        direccion = self.ui.l_direccion.text()
        telefono = self.ui.l_telefono.text()
        if not nro_presupuesto or not nombre or not apellido or not direccion or not telefono or self.ui.tableWidget.rowCount() == 0:
            self.showWarningMessage("Error", "Tienes campos vacíos")
            return
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
