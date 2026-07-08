from datetime import datetime


class InvoiceValidator:

    def __init__(self, database):
        self.database = database

    def is_empty(self, value):

        return value in ["", "Not Found", None]

    def is_valid_date(self, date_string):

        if self.is_empty(date_string):
            return False

        formats = [
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%Y-%m-%d"
        ]

        for fmt in formats:

            try:
                datetime.strptime(date_string, fmt)
                return True

            except ValueError:
                pass

        return False

    def is_number(self, value):

        if self.is_empty(value):
            return False

        try:
            float(value.replace(",", ""))

            return True

        except ValueError:

            return False

    def validate(self, invoice):

        errors = []

        if self.is_empty(invoice["invoice_number"]):
            errors.append("Invoice Number Missing")

        if self.is_empty(invoice["vendor_name"]):
            errors.append("Vendor Name Missing")

        if not self.is_valid_date(invoice["invoice_date"]):
            errors.append("Invalid Invoice Date")

        if not self.is_valid_date(invoice["due_date"]):
            errors.append("Invalid Due Date")

        if not self.is_number(invoice["tax_amount"]):
            errors.append("Invalid Tax Amount")

        if not self.is_number(invoice["total_amount"]):
            errors.append("Invalid Total Amount")

        if self.database.invoice_exists(invoice["invoice_number"]):
            errors.append("Duplicate Invoice Number")

        if len(errors) == 0:

            invoice["validation_status"] = "Valid"

        else:

            invoice["validation_status"] = "Invalid"

        return errors