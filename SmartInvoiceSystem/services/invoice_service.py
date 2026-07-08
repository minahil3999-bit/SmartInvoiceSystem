from invoice_processing.pdf_reader import PDFReader
from invoice_processing.extractor import InvoiceExtractor
from invoice_processing.validator import InvoiceValidator
from utils.logger import Logger

class InvoiceService:

    def __init__(self, database):

        self.database = database

        self.reader = PDFReader()

        self.extractor = InvoiceExtractor()

        self.validator = InvoiceValidator(database)

    def process_invoice(self, pdf_path):

        text = self.reader.extract_text(pdf_path)
        Logger.info(f"PDF Uploaded : {pdf_path}")

        if text.startswith("ERROR"):
            Logger.error(text)
            return {

                "success": False,

                "message": text

            }

        invoice = self.extractor.extract(text)

        errors = self.validator.validate(invoice)

        if errors:

            Logger.warning(f"Validation Failed : {invoice['invoice_number']}")

            return {

                "success": False,

                "invoice": invoice,

                "errors": errors

            }

        self.database.save_invoice(invoice)
        Logger.info(f"Invoice Saved : {invoice['invoice_number']}")

        return {

            "success": True,

            "invoice": invoice

        }