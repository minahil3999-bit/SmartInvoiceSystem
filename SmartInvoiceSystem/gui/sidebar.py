import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, width=220)

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="Smart Invoice",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=30)

        ctk.CTkButton(
            self,
            text="Dashboard",
            command=parent.show_dashboard
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            self,
            text="Upload Invoice",
            command=parent.show_upload
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            self,
            text="Search",
            command=parent.show_search
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            self,
            text="Reports",
            command=parent.show_reports
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            self,
            text="Logs",
            command=parent.show_logs
        ).pack(fill="x", padx=20, pady=5)