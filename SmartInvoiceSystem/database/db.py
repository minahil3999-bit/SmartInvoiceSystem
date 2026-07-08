import sqlite3
from config import DATABASE_NAME
from database.models import CREATE_INVOICE_TABLE
from datetime import datetime
from utils.logger import Logger

class Database:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE_NAME)

        self.cursor = self.connection.cursor()

        self.create_table()

    def get_all_invoices(self):
        self.cursor.execute("""
            SELECT *
            FROM invoices
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def search_by_invoice(self, invoice_number):
        self.cursor.execute("""

            SELECT *

            FROM invoices

            WHERE invoice_number LIKE ?

        """,

                            ('%' + invoice_number + '%',)

                            )

        return self.cursor.fetchall()

    def search_by_vendor(self, vendor):
        self.cursor.execute("""

            SELECT *

            FROM invoices

            WHERE vendor_name LIKE ?

        """,

                            ('%' + vendor + '%',)

                            )

        return self.cursor.fetchall()

    def update_payment_status(self, invoice_number, status):

        self.cursor.execute("""

            UPDATE invoices

            SET payment_status = ?

            WHERE invoice_number = ?

        """,

                            (status, invoice_number)

                            )

        self.connection.commit()
        Logger.info(f"Payment Updated : {invoice_number} -> {status}")

    def delete_invoice(self, invoice_number):
        self.cursor.execute("""

            DELETE FROM invoices

            WHERE invoice_number = ?

        """,

                            (invoice_number,)

                            )

        self.connection.commit()
        Logger.info(f"Invoice Deleted : {invoice_number}")

    def save_invoice(self, invoice):
        self.cursor.execute("""
            INSERT INTO invoices(
                invoice_number,
                vendor_name,
                customer_name,
                invoice_date,
                due_date,
                tax_amount,
                total_amount,
                currency,
                payment_status,
                processing_date,
                validation_status
            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?)

        """,

                            (

                                invoice["invoice_number"],

                                invoice["vendor_name"],

                                invoice["customer_name"],

                                invoice["invoice_date"],

                                invoice["due_date"],

                                float(invoice["tax_amount"]),

                                float(invoice["total_amount"]),

                                invoice["currency"],

                                invoice["payment_status"],

                                datetime.now().strftime("%d-%m-%Y %H:%M:%S"),

                                invoice["validation_status"]

                            ))

        self.connection.commit()
        Logger.info(f"Invoice Stored : {invoice['invoice_number']}")

    def invoice_exists(self, invoice_number):
        self.cursor.execute(
            """
            SELECT invoice_number
            FROM invoices
            WHERE invoice_number = ?
            """,
            (invoice_number,)
        )

        return self.cursor.fetchone() is not None

    def create_table(self):

        self.cursor.execute(CREATE_INVOICE_TABLE)

        self.connection.commit()

    def get_total_invoices(self):
        self.cursor.execute("""

            SELECT COUNT(*)

            FROM invoices

        """)

        return self.cursor.fetchone()[0]

    def get_total_vendors(self):
        self.cursor.execute("""

            SELECT COUNT(DISTINCT vendor_name)

            FROM invoices

        """)

        return self.cursor.fetchone()[0]

    def get_total_amount(self):
        self.cursor.execute("""

            SELECT SUM(total_amount)

            FROM invoices

        """)

        amount = self.cursor.fetchone()[0]

        if amount is None:
            return 0

        return amount

    def get_pending_payments(self):
        self.cursor.execute("""

            SELECT COUNT(*)

            FROM invoices

            WHERE payment_status='Pending'

        """)

        return self.cursor.fetchone()[0]

    def get_validation_errors(self):
        self.cursor.execute("""

            SELECT COUNT(*)

            FROM invoices

            WHERE validation_status='Invalid'

        """)

        return self.cursor.fetchone()[0]

    def close(self):

        self.connection.close()