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
        row1 = ctk.CTkFrame(self)
        row1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        side_bar = ctk.CTkFrame(row1)
        # side_bar.pack(padx=10, pady=5, fill=tk.BOTH)
        side_bar.grid(row=0, column=0,
                      sticky=tk.N + tk.S + tk.E + tk.W,
                      padx=10, pady=10)

        start_instance_btn = ctk.CTkButton(side_bar, text="Start Instance", command=self.start_instance)
        start_instance_btn.grid(row=0, column=0,
                                sticky=tk.N + tk.S + tk.E + tk.W,
                                padx=10, pady=10)

        save_account_btn = ctk.CTkButton(side_bar, text="Save Account", command=self.save_account)
        save_account_btn.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        stop_ui_btn = ctk.CTkButton(side_bar, text="Stop UI", command=self.stop_ui)
        stop_ui_btn.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        clear_csv_btn = ctk.CTkButton(side_bar, text="Clear Data", command=self.clear_csv)
        clear_csv_btn.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        main_view = ctk.CTkFrame(row1)
        main_view.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        # show current data
        self.usr_mail = ctk.CTkLabel(main_view, text="Mail: ")
        self.usr_mail.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        self.usr_name = ctk.CTkLabel(main_view, text="Username: ")
        self.usr_name.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

        self.current_data = ctk.CTkFrame(self)
        self.current_data.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.update_data()

    def start_instance(self):
        self.driver = Driver(self)

    def save_account(self):
        self.driver.end()
        self.update_data()
        # clear the current user data
        self.update_user()

    def stop_ui(self):
        self.destroy()

    def update_user(self, mail='', username=''):
        self.usr_mail.configure(text="Mail: %s" % mail)
        self.usr_name.configure(text="Username: %s" % username)

    def update_data(self):
        # show the content of the csv file
        rows = self.read_mails_and_users()
        for i, row in enumerate(rows):
            mail, username = row
            ctk.CTkLabel(self.current_data, text="Mail: %s" % mail).grid(row=i, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)
            ctk.CTkLabel(self.current_data, text="Username: %s" % username).grid(row=i, column=1, sticky=tk.N + tk.S + tk.E + tk.W, padx=10, pady=10)

    def clear_csv(self):
        with open('mails.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

        self.current_data.destroy()
        self.current_data = ctk.CTkFrame(self)
        self.current_data.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.update_data()

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