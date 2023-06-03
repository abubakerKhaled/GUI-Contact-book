# -*- coding: utf-8 -*-


"""This module provides the view to manage the contacts table."""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QTableView,
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMessageBox,
)

from .model import contactsModel

class window(QMainWindow):
    """Main Window."""
    def __init__(self, parent = None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactModel = contactsModel()
        self.setupUI()
    # Open the Add Dialog
    def openAddDialog(self):
        """Open the add contact dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()
    # Delete Contact Method
    def deleteContact(self):
        """Delete the selected contact from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return 
        
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to delete the selected contact?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        
        if messageBox == QMessageBox.StandardButton.Ok:
            self.contactModel.deleteContact(row)
    
    def clearContacts(self):
        """Remove all contacts from the database."""
        messageBox = QMessageBox.warning(
            self, 
            "Warning!",
            "Do you want to remove all your contacts?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        
        if messageBox == QMessageBox.StandardButton.Ok:
            self.contactModel.clearContacts()
    
    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.contactModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.resizeColumnsToContents()
        # self.table.hideColumn(-1)
    
        # Create buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearContacts)

        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        # layout.stretch(0)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

class AddDialog(QDialog):
    """Add contact dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        
        self.setupUI()


    def setupUI(self):
        """Setup the add contact dialog's GUI."""
        # Create line edits for data fields
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")
        self.phone_numberField = QLineEdit()
        self.phone_numberField.setObjectName("Phone Number")

        # Lay out the data fields
        layout = QFormLayout()
        layout.addRow("Name: ", self.nameField)
        layout.addRow("Job: ", self.jobField)
        layout.addRow("Email: ", self.emailField)
        layout.addRow("Phone Number: ", self.phone_numberField)
        self.layout.addLayout(layout)

        # Add standard buttons to the dialog and connect them
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)
    
    def accept(self) -> None:
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.nameField, self.jobField, self.emailField, self.phone_numberField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None # Reset .data
                return 
            
            self.data.append(field.text())
            if not self.data:
                return 
            
        return super().accept()
    
