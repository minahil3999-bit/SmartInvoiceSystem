import pdfplumber


class PDFReader:

    def __init__(self):
        pass

    def extract_text(self, pdf_path):

        try:

            full_text = ""

            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        full_text += page_text + "\n"

            return full_text

        except Exception as e:

            return f"ERROR : {e}"