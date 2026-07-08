import pandas as pd
from utils.logger import Logger
import matplotlib.pyplot as plt
import os
os.makedirs("exports",exist_ok=True)
class ReportGenerator:

    def __init__(self, database):

        self.database = database

    def load_data(self):

        query = """

            SELECT *

            FROM invoices

        """

        return pd.read_sql_query(
            query,
            self.database.connection
        )

    def export_excel(self):
        df = self.load_data()

        df.to_excel(

            "exports/Invoice_Report.xlsx",

            index=False

        )
        Logger.info("Excel Report Exported")

    def export_csv(self):
        df = self.load_data()

        df.to_csv(

            "exports/Invoice_Report.csv",

            index=False

        )
        Logger.info("CSV Report Exported")

    def vendor_summary(self):
        df = self.load_data()

        return df.groupby(

            "vendor_name"

        )["total_amount"].sum()

    def monthly_summary(self):
        df = self.load_data()

        if df.empty:
            return pd.Series(dtype=float)

        # Convert DD-MM-YYYY to datetime
        df["invoice_date"] = pd.to_datetime(
            df["invoice_date"],
            format="%d-%m-%Y",
            errors="coerce"
        )

        # Remove invalid dates
        df = df.dropna(subset=["invoice_date"])

        summary = df.groupby(
            df["invoice_date"].dt.month
        )["total_amount"].sum()

        return summary

    def tax_summary(self):
        df = self.load_data()

        return df["tax_amount"].sum()

    def vendor_chart(self):
        summary = self.vendor_summary()

        plt.figure(figsize=(8, 5))

        plt.bar(summary.index, summary.values)

        plt.title("Vendor-wise Invoice Amount")

        plt.xlabel("Vendor")

        plt.ylabel("Amount")

        plt.xticks(rotation=30)

        plt.tight_layout()

        plt.show()

    def monthly_chart(self):

        summary = self.monthly_summary()

        if summary.empty:
            print("No data available.")
            return

        months = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]

        x = [months[m - 1] for m in summary.index]

        plt.figure(figsize=(8, 5))
        plt.plot(x, summary.values, marker="o")
        plt.title("Monthly Revenue")
        plt.xlabel("Month")
        plt.ylabel("Revenue (PKR)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def payment_chart(self):
        query = """

            SELECT payment_status,
                   COUNT(*)

            FROM invoices

            GROUP BY payment_status

        """

        df = self.load_data()

        status = df.groupby(
            "payment_status"
        ).size()

        plt.figure(figsize=(6, 6))

        plt.pie(
            status,
            labels=status.index,
            autopct="%1.1f%%"
        )

        plt.title("Payment Status")

        plt.show()

    def tax_chart(self):
        df = self.load_data()

        vendor_tax = df.groupby(
            "vendor_name"
        )["tax_amount"].sum()

        plt.figure(figsize=(8, 5))

        plt.bar(
            vendor_tax.index,
            vendor_tax.values
        )

        plt.title("Tax by Vendor")

        plt.xticks(rotation=30)

        plt.tight_layout()

        plt.show()