from http.cookiejar import month

import customtkinter as ctk
from tkinter import messagebox

from database.db import Database
from reports.report_generator import ReportGenerator


class ReportPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.database = Database()
        self.report = ReportGenerator(self.database)

        title = ctk.CTkLabel(
            self,
            text="Reports & Export",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=20)

        ctk.CTkButton(
            button_frame,
            text="Export Excel",
            width=180,
            command=self.export_excel
        ).grid(row=0, column=0, padx=10, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Export CSV",
            width=180,
            command=self.export_csv
        ).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Vendor Summary",
            width=180,
            command=self.vendor_summary
        ).grid(row=1, column=0, padx=10, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Monthly Summary",
            width=180,
            command=self.monthly_summary
        ).grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Tax Summary",
            width=180,
            command=self.tax_summary
        ).grid(row=2, column=0, columnspan=2, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Vendor Chart",
            width=180,
            command=self.vendor_chart
        ).grid(row=3, column=0, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Monthly Chart",
            width=180,
            command=self.monthly_chart
        ).grid(row=3, column=1, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Payment Chart",
            width=180,
            command=self.payment_chart
        ).grid(row=4, column=0, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Tax Chart",
            width=180,
            command=self.tax_chart
        ).grid(row=4, column=1, pady=10)



        self.output = ctk.CTkTextbox(
            self,
            width=900,
            height=400
        )

        self.output.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

    def export_excel(self):

        self.report.export_excel()

        messagebox.showinfo(
            "Success",
            "Excel Report Exported Successfully."
        )

    def export_csv(self):

        self.report.export_csv()

        messagebox.showinfo(
            "Success",
            "CSV Report Exported Successfully."
        )

    def vendor_summary(self):

        self.output.delete("1.0", "end")

        summary = self.report.vendor_summary()

        self.output.insert(
            "end",
            "Vendor Summary\n\n"
        )

        for vendor, amount in summary.items():
            self.output.insert("end",f"{vendor} : Rs {amount:,.2f}\n")

    def monthly_summary(self):

        self.output.delete("1.0", "end")

        summary = self.report.monthly_summary()
        months = {
            1:"January",
            2:"February",
            3:"March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

        self.output.insert(
            "end",
            "Monthly Summary\n\n"
        )

        for month, amount in summary.items():
            self.output.insert("end",f"{months.get(month,month)}:Rs {amount:,.2f}")


    def tax_summary(self):

        self.output.delete("1.0", "end")

        tax = self.report.tax_summary()

        self.output.insert(
            "end",
            f"Total Tax Collected : Rs {tax:,.2f}"
        )

    def vendor_chart(self):
        self.report.vendor_chart()

    def monthly_chart(self):
        self.report.monthly_chart()

    def payment_chart(self):
        self.report.payment_chart()

    def tax_chart(self):
        self.report.tax_chart()