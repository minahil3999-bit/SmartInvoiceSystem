import re


class InvoiceExtractor:

    def __init__(self):
        pass

    def find_value(self, pattern, text):

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

        return "Not Found"

    def extract(self, text):

        data = {

            "invoice_number": self.find_value(
                r"Invoice\s*Number\s*[:\-]?\s*(.+)",
                text
            ),

            "vendor_name": self.find_value(
                r"Vendor\s*[:\-]?\s*(.+)",
                text
            ),

            "customer_name": self.find_value(
                r"Customer\s*[:\-]?\s*(.+)",
                text
            ),

            "invoice_date": self.find_value(
                r"Invoice\s*Date\s*[:\-]?\s*(.+)",
                text
            ),

            "due_date": self.find_value(
                r"Due\s*Date\s*[:\-]?\s*(.+)",
                text
            ),

            "tax_amount": self.find_value(
                r"Tax(?:\s*Amount)?\s*[:\-]?\s*([\d,.]+)",
                text
            ),

            "total_amount": self.find_value(
                r"Total(?:\s*Amount)?\s*[:\-]?\s*([\d,.]+)",
                text
            ),

            "currency": self.find_value(
                r"Currency\s*[:\-]?\s*(.+)",
                text
            ),

            "payment_status": "Pending"

        }

        return data