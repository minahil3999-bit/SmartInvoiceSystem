import customtkinter as ctk
import os


class LogPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Application Logs",
            font=("Arial", 28, "bold")
        )

        title.pack(pady=20)

        self.box = ctk.CTkTextbox(
            self,
            width=900,
            height=500
        )

        self.box.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        self.load_logs()

    def load_logs(self):

        self.box.delete("1.0", "end")

        if not os.path.exists("logs/application.log"):

            self.box.insert(
                "end",
                "No Logs Found."
            )

            return

        with open(
            "logs/application.log",
            "r",
            encoding="utf-8"
        ) as file:

            self.box.insert(
                "end",
                file.read()
            )