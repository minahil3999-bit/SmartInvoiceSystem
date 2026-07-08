import customtkinter as ctk
from tkinter import messagebox

from database.db import Database


class SearchPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.database = Database()

        # ==========================
        # Title
        # ==========================
        title = ctk.CTkLabel(
            self,
            text="Search Invoices",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # ==========================
        # Search Entry
        # ==========================
        self.search_entry = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Enter Invoice Number or Vendor Name"
        )
        self.search_entry.pack(pady=10)

        # ==========================
        # Buttons Frame
        # ==========================
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        search_btn = ctk.CTkButton(
            button_frame,
            text="Search",
            command=self.search
        )
        search_btn.grid(row=0, column=0, padx=10)

        paid_btn = ctk.CTkButton(
            button_frame,
            text="Mark As Paid",
            command=self.mark_paid
        )
        paid_btn.grid(row=0, column=1, padx=10)

        delete_btn = ctk.CTkButton(
            button_frame,
            text="Delete Invoice",
            fg_color="red",
            hover_color="darkred",
            command=self.delete_invoice
        )
        delete_btn.grid(row=0, column=2, padx=10)

        # ==========================
        # Result Box
        # ==========================
        self.result_box = ctk.CTkTextbox(
            self,
            width=900,
            height=450,
            font=("Consolas", 14)
        )

        self.result_box.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        # Show all invoices on startup
        self.show_all()

    # ==========================================
    # Show All Invoices
    # ==========================================

    def show_all(self):

        self.result_box.delete("1.0", "end")

        invoices = self.database.get_all_invoices()

        if not invoices:

            self.result_box.insert(
                "end",
                "No invoices found."
            )

            return

        self.display_results(invoices)

    # ==========================================
    # Search
    # ==========================================

    def search(self):

        keyword = self.search_entry.get().strip()

        self.result_box.delete("1.0", "end")

        if keyword == "":

            self.show_all()

            return

        invoices = self.database.search_by_invoice(keyword)

        if len(invoices) == 0:

            invoices = self.database.search_by_vendor(keyword)

        if len(invoices) == 0:

            self.result_box.insert(
                "end",
                "No invoice found."
            )

            return

        self.display_results(invoices)

    # ==========================================
    # Display Results
    # ==========================================

    def display_results(self, invoices):

        for invoice in invoices:

            self.result_box.insert(
                "end",
                f"""
==============================================================

Invoice Number : {invoice[1]}

Vendor Name    : {invoice[2]}

Customer Name  : {invoice[3]}

Invoice Date   : {invoice[4]}

Due Date       : {invoice[5]}

Tax Amount     : {invoice[6]}

Total Amount   : {invoice[7]}

Currency       : {invoice[8]}

Payment Status : {invoice[9]}

Validation     : {invoice[11]}

==============================================================

"""
            )

    # ==========================================
    # Mark Invoice As Paid
    # ==========================================

    def mark_paid(self):

        invoice_number = self.search_entry.get().strip()

        if invoice_number == "":

            messagebox.showwarning(
                "Warning",
                "Enter Invoice Number."
            )

            return

        self.database.update_payment_status(
            invoice_number,
            "Paid"
        )

        messagebox.showinfo(
            "Success",
            "Payment Status Updated."
        )

        self.search()

    # ==========================================
    # Delete Invoice
    # ==========================================

    def delete_invoice(self):

        invoice_number = self.search_entry.get().strip()

        if invoice_number == "":

            messagebox.showwarning(
                "Warning",
                "Enter Invoice Number."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm",
            "Delete this invoice?"
        )

        if confirm:

            self.database.delete_invoice(
                invoice_number
            )

            self.search_entry.delete(0, "end")

            self.result_box.delete("1.0", "end")

            messagebox.showinfo(
                "Success",
                "Invoice Deleted Successfully."
            )

            self.show_all()