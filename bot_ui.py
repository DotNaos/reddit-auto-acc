import csv
import tkinter as tk
import customtkinter as ctk
from driver import Driver


class BotUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

        self.title("Bot UI")
        self.geometry("500x500")
        self.resizable(True, True)

        self.show_ui()

        self.mainloop()

    def show_ui(self):
        # sidebar on the left
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)


        side_bar = ctk.CTkFrame(self.master)
        # side_bar.pack(padx=10, pady=5, fill=tk.BOTH)
        side_bar.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10, )

        start_instance_btn = ctk.CTkButton(side_bar, text="Start Instance", command=self.start_instance)
        start_instance_btn.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        save_account_btn = ctk.CTkButton(side_bar, text="Save Account", command=self.save_account)
        save_account_btn.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        stop_ui_btn = ctk.CTkButton(side_bar, text="Stop UI", command=self.stop_ui)
        stop_ui_btn.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        main_view = ctk.CTkFrame(self.master)
        main_view.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

    def start_instance(self):
        self.driver = Driver()

    def save_account(self):
        self.driver.end()

    def stop_ui(self):
        self.destroy()

    def read_mails_and_users(self):
        # read csv file
        with open('mails.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            rows = []
            for row in reader:
                # if row is empty then skip
                if not row:
                    continue

                email, username = row

                # print email and username
                print('Email: %s' % email)
                print('Username: %s' % username)

                # append email and username to rows
                rows.append(row)

            return rows