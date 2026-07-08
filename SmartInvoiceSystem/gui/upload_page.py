import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

from database.db import Database
from services.invoice_service import InvoiceService


class UploadPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        # ===========================
        # Database & Service
        # ===========================
        self.database = Database()
        self.invoice_service = InvoiceService(self.database)

        self.selected_files = []

        # ===========================
        # Title
        # ===========================
        title = ctk.CTkLabel(
            self,
            text="Upload Invoice",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # ===========================
        # Upload Button
        # ===========================
        upload_btn = ctk.CTkButton(
            self,
            text="Upload PDF",
            command=self.upload_files,
            width=180,
            height=40
        )
        upload_btn.pack(pady=10)

        # ===========================
        # Result Textbox
        # ===========================
        self.file_list = ctk.CTkTextbox(
            self,
            width=850,
            height=450,
            font=("Consolas", 14)
        )

        self.file_list.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

    # ============================================
    # Upload Files
    # ============================================

    def upload_files(self):

        files = filedialog.askopenfilenames(
            title="Select Invoice PDFs",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not files:
            return

        self.selected_files.clear()

        self.file_list.delete("1.0", "end")

        successful = 0

        for file in files:

            if not file.lower().endswith(".pdf"):
                continue

            filename = os.path.basename(file)

            self.selected_files.append(file)

            result = self.invoice_service.process_invoice(file)

            self.file_list.insert(
                "end",
                "=" * 70 + "\n"
            )

            self.file_list.insert(
                "end",
                f"📄 File : {filename}\n"
            )

            self.file_list.insert(
                "end",
                "=" * 70 + "\n\n"
            )

            # ----------------------------
            # Failed Processing
            # ----------------------------

            if not result["success"]:

                if "message" in result:

                    self.file_list.insert(
                        "end",
                        f"❌ {result['message']}\n\n"
                    )

                elif "errors" in result:

                    invoice = result["invoice"]

                    self.file_list.insert(
                        "end",
                        f"Invoice Number : {invoice['invoice_number']}\n"
                    )

                    self.file_list.insert(
                        "end",
                        f"Vendor Name    : {invoice['vendor_name']}\n"
                    )

                    self.file_list.insert(
                        "end",
                        f"Customer Name  : {invoice['customer_name']}\n"
                    )

                    self.file_list.insert(
                        "end",
                        f"Invoice Date   : {invoice['invoice_date']}\n"
                    )

                    self.file_list.insert(
                        "end",
                        f"Due Date       : {invoice['due_date']}\n"
                    )

                    self.file_list.insert(
                        "end",
                        f"Tax Amount     : {invoice['tax_amount']}\n"
                    )

                    self.file_list.insert(
                        "end",
                        f"Total Amount   : {invoice['total_amount']}\n"
                    )

                    self.file_list.insert(
                        "end",
                        f"Currency       : {invoice['currency']}\n"
                    )

                    self.file_list.insert(
                        "end",
                        f"Status         : {invoice['validation_status']}\n\n"
                    )

                    self.file_list.insert(
                        "end",
                        "Validation Errors:\n"
                    )

                    for error in result["errors"]:

                        self.file_list.insert(
                            "end",
                            f"❌ {error}\n"
                        )

                self.file_list.insert(
                    "end",
                    "\n\n"
                )

                continue

            # ----------------------------
            # Success
            # ----------------------------

            successful += 1

            invoice = result["invoice"]

            self.file_list.insert(
                "end",
                f"Invoice Number : {invoice['invoice_number']}\n"
            )

            self.file_list.insert(
                "end",
                f"Vendor Name    : {invoice['vendor_name']}\n"
            )

            self.file_list.insert(
                "end",
                f"Customer Name  : {invoice['customer_name']}\n"
            )

            self.file_list.insert(
                "end",
                f"Invoice Date   : {invoice['invoice_date']}\n"
            )

            self.file_list.insert(
                "end",
                f"Due Date       : {invoice['due_date']}\n"
            )

            self.file_list.insert(
                "end",
                f"Tax Amount     : {invoice['tax_amount']}\n"
            )

            self.file_list.insert(
                "end",
                f"Total Amount   : {invoice['total_amount']}\n"
            )

            self.file_list.insert(
                "end",
                f"Currency       : {invoice['currency']}\n"
            )

            self.file_list.insert(
                "end",
                f"Payment Status : {invoice['payment_status']}\n"
            )

            self.file_list.insert(
                "end",
                f"Validation     : {invoice['validation_status']}\n"
            )

            self.file_list.insert(
                "end",
                "\n✅ Invoice Saved Successfully\n\n"
            )

        messagebox.showinfo(
            "Processing Complete",
            f"Total Selected : {len(self.selected_files)}\n"
            f"Successfully Processed : {successful}\n"
            f"Failed : {len(self.selected_files) - successful}"
        )