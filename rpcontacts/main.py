# -*- coding: utf-8 -*-
# rpcontacts\main.py


"""This module provides the RP Contacts Application."""

import sys

from PyQt6.QtWidgets import QApplication

from .database import createConnection

from .views import window

def main():
    """RP Contacts main function."""
    
    # Create the application
    app = QApplication(sys.argv)
    
    # Connect to database before creating any window
    if not createConnection("contacts.db"):
        sys.exit(1)

    # Create the main window
    win = window()
    win.show()

    # Run the event loop 
    sys.exit(app.exec())