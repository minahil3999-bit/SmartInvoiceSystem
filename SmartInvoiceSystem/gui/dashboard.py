import customtkinter as ctk
from gui.sidebar import Sidebar
from gui.cards import DashboardCard
from gui.upload_page import UploadPage
from database.db import Database
from gui.search_page import SearchPage
from gui.log_page import LogPage
from gui.report_page import ReportPage

class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.pack(fill="both", expand=True)
        self.database = Database()

        # =========================
        # Sidebar
        # =========================
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        # =========================
        # Content Area
        # =========================
        self.content = ctk.CTkFrame(self)
        self.content.pack(
            side="right",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # Show Upload Page by default
        self.show_dashboard()

    # ===================================
    # Remove Current Page
    # ===================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ===================================
    # Dashboard Page
    # ===================================

    def show_dashboard(self):

        self.clear_content()

        heading = ctk.CTkLabel(
            self.content,
            text="Dashboard",
            font=("Arial", 28, "bold")
        )

        heading.pack(anchor="w", pady=20)

        cards_frame = ctk.CTkFrame(self.content)
        cards_frame.pack(fill="x", pady=10)

        DashboardCard(
            cards_frame,
            "Total Invoices",
            str(self.database.get_total_invoices())
        ).pack(side="left", padx=10)

        DashboardCard(
            cards_frame,
            "Total Vendors",
            str(self.database.get_total_vendors())
        ).pack(side="left", padx=10)

        DashboardCard(
            cards_frame,
            "Pending Payments",
            str(self.database.get_pending_payments())
        ).pack(side="left", padx=10)

        DashboardCard(
            cards_frame,
            "Validation Errors",
            str(self.database.get_validation_errors())
        ).pack(side="left", padx=10)

        DashboardCard(
            cards_frame,
            "Total Amount",
            f"Rs {self.database.get_total_amount():,.2f}"
        ).pack(side="left", padx=10)

    # ===================================
    # Upload Page
    # ===================================

    def show_upload(self):

        self.clear_content()

        upload_page = UploadPage(self.content)

        upload_page.pack(
            fill="both",
            expand=True
        )

    def show_search(self):
        self.clear_content()

        SearchPage(self.content).pack(
            fill="both",
            expand=True
        )

    def show_logs(self):
        self.clear_content()

        LogPage(self.content).pack(
            fill="both",
            expand=True
        )

    def show_reports(self):
        self.clear_content()

        ReportPage(self.content).pack(
            fill="both",
            expand=True
        )