import customtkinter as ctk


class DashboardCard(ctk.CTkFrame):

    def __init__(self, parent, title, value):

        super().__init__(parent)

        self.configure(width=220, height=120)

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text=title,
            font=("Arial",18)
        ).pack(pady=(20,5))

        ctk.CTkLabel(
            self,
            text=value,
            font=("Arial",28,"bold")
        ).pack()