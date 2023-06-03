# -*- coding: utf-8 -*-

# rpcontacts/database.py

from PyQt6.QtSql import (
    QSqlDatabase,
    QSqlQuery,
)
from PyQt6.QtWidgets import QMessageBox
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# def _createContactsTable():
#     """Create the contacts table in the database."""
#     createTableQuery = QSqlQuery()
#     return createTableQuery.exec(
#         """
#         CREATE TABLE IF NOT EXISTS contacts (
#             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
#             name VARCHAR(40) NOT NULL,
#             job VARCHAR(50),
#             email VARCHAR(40) NOT NULL,
#             phone_number VARCHAR(20) NOT NULL
#             )
#             """
#     )


def createConnection(databaseName):
    """Create and open a databse connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if connection.open():
        # print("Database is now opened.")
        query = QSqlQuery(connection)
        query.exec(
            """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
            )
            """
        )
        insertDataQuery = QSqlQuery()
        insertDataQuery.prepare(
            """INSERT INTO contacts (
                    name, 
                    job, 
                    email,
                    phone_number
                )
                VALUES (?, ?, ?, ?)
                """
        )
        # data = [
        #     ("Linda", "Technical Lead", "linda@example.com", "0121565896"),
        #     ("Joe", "Senior Web Developer", "joe@example.com", "01256484651"),
        #     ("Lara", "Project Manager", "lara@example.com", "01021654984"),
        #     ("David", "Data Analyst", "david@example.com", "01216548432"),
        #     ("Jane", "Senior Python Developer", "jane@example.com", "0111361545"),
        # ]
        # for name, job, email, phone_number in data:
        #     insertDataQuery.addBindValue(name)
        #     insertDataQuery.addBindValue(job)
        #     insertDataQuery.addBindValue(email)
        #     insertDataQuery.addBindValue(phone_number)
        #     insertDataQuery.exec()

        return True
    QMessageBox.warning(
        None,
        "RP Contact"
        f"Database Error: {connection.lastError().text()}",
    )
    return False
