from data import NATIONALITY_LIST, JOB_ROLE_LIST
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import sqlite3
import tkinter
import openpyxl
import os

GREEN = "#61A064"
BLUE = "#237FC9"
FONT = ("Arial", 15, "bold")

radio_button_val = ""

class App:
    def __init__(self):
        self.radiostate = None
        self.database = {}
        self.window = None
        self.create_layout()

    def submit_to_excel(self):
        self.get_data("Excel")

    def submit_to_sql(self):
        self.get_data("Sql")

    def get_data(self, mode):
        first_name_data = self.database["first_name_entry"].get().title()
        second_name_data = self.database["second_name_entry"].get().title()
        last_name_data = self.database["last_name_entry"].get().title()

        age_data = self.database["age_spinbox"].get()
        gender_data = self.database["gender_combox"].get().title()
        nationality_data = self.database["nationality_combox"].get().title()
        user_job_data = self.database["user_job_combox"].get().title()
        user_status_data= self.database["user_status_combox"].get().title()
        year_exp_data = self.database["year_exp_spinbox"].get()

        all_data = [first_name_data, second_name_data, last_name_data, age_data, gender_data,
                    nationality_data, user_job_data,user_status_data, year_exp_data]

        if mode == "Excel":
            if 0 in all_data or "" in all_data:
                showinfo(title="Information", message="Error. Please Fill the form correctly!")
            else:
                print("Submitted data to Excel")
                excel_file_name = askstring('Confirmation', "Enter file's name:")
                showinfo(title="Information", message="Succeed")

                FILE_PATH = fr"C:\Users\Asus\Documents\Programming\Python Course\data-entry-project\{excel_file_name}.xlsx"

                if not os.path.exists(FILE_PATH):
                    workbook = openpyxl.Workbook()
                    # Select the active sheet
                    sheet = workbook.active
                    # Add headings to the file
                    headings = ["First Name", "Second Name", "Last Name", "Age", "Gender", "Nationality", "Job Role",
                                "Status", "Year Of Experience"]
                    sheet.append(headings)
                    workbook.save(FILE_PATH)


                workbook = openpyxl.load_workbook(FILE_PATH)
                sheet = workbook.active
                sheet.append(all_data)
                workbook.save(FILE_PATH)

        elif mode == 'Sql':
            if 0 in all_data or "" in all_data:
                showinfo(title="Information", message="Error. Please Fill the form correctly!")
            else:
                print("Submitted data to SQL")
                database_file_name = askstring('Confirmation', "Enter database's name:")
                showinfo(title="Information", message="Succeed")

                # Create Table
                conn = sqlite3.connect(f"{database_file_name}.db")
                create_table_query = '''CREATE TABLE IF NOT EXISTS JOB_ENTRY_DATA
                                    (first_name TEXT, 
                                    second_name TEXT, 
                                    last_name TEXT, 
                                    age INT, 
                                    gender TEXT,
                                    nationality TEXT, 
                                    job_role TEXT, 
                                    status TEXT, 
                                    year_of_experiences INT)'''
                conn.execute(create_table_query)

                # Insert Data
                data_insert_query = '''INSERT INTO JOB_ENTRY_DATA(
                                        first_name, 
                                        second_name, 
                                        last_name, 
                                        age, 
                                        gender, 
                                        nationality, 
                                        job_role, 
                                        status,  
                                        year_of_experiences) 
                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                                    '''
                data_insert_tuple = (first_name_data, second_name_data, last_name_data, age_data, gender_data,
                                     nationality_data, user_job_data, user_status_data, year_exp_data)

                cursor = conn.cursor()
                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()
                conn.close()

    def update_theme(self):
        theme_color = "#090088" if self.radiostate.get() == 1 else "#ecffad"
        self.window.config(bg=theme_color)

        for widget in self.window.winfo_children():
            if isinstance(widget, tkinter.Label):
                widget.config(bg=theme_color)

    def setting(self):
        settings = tkinter.Toplevel() # Create a new window, that seperately with the main window
        settings.title("Setting")
        settings.minsize(width=20, height=20)

        self.radiostate = tkinter.IntVar()

        light_theme_button = tkinter.Radiobutton(settings,
                                                 text="Light Theme",
                                                 variable=self.radiostate,
                                                 value=1,
                                                 command=self.update_theme)
        light_theme_button.grid(column=0, row=0)

        dark_theme_button = tkinter.Radiobutton(settings,
                                                text="Dark Theme",
                                                variable=self.radiostate,
                                                value=2,
                                                command=self.update_theme)
        dark_theme_button.grid(column=0, row=1)

        settings.mainloop()


    def create_layout(self):
        self.window = tkinter.Tk()
        self.window.title("Data Entry Form")
        self.window.config(padx=30, pady=10)

        # Title Label
        title_label = tkinter.Label(text="Data Entry Application", fg=GREEN, font=FONT)
        title_label.grid(column=1, row=0)

#+++++++++++++++++++++++++++++++++++++++++++++++USER INFORMATION++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        user_info_frame = tkinter.LabelFrame(self.window, text="User Information")
        user_info_frame.grid(column=1, row=1, pady=10)

    ########################################### FULL NAME ##############################################################
        first_name_label = tkinter.Label(user_info_frame, text="First Name")
        first_name_label.grid(column=0, row=1)

        second_name_label = tkinter.Label(user_info_frame, text="Second Name")
        second_name_label.grid(column=1, row=1)

        last_name_label = tkinter.Label(user_info_frame, text="Last Name")
        last_name_label.grid(column=2, row=1)

        first_name_entry = tkinter.Entry(user_info_frame, width=20)  # First Name Entry
        first_name_entry.grid(column=0, row=2, padx=20, pady=10)

        second_name_entry = tkinter.Entry(user_info_frame, width=20)
        second_name_entry.grid(column=1, row=2, padx=20, pady=10)

        last_name_entry = tkinter.Entry(user_info_frame, width=20)
        last_name_entry.grid(column=2, row=2, padx=20, pady=10)

    ########################################### AGE, GENDER, NATIONALITY ###############################################
        age_label = tkinter.Label(user_info_frame, text="Age")
        age_label.grid(column=0, row=3)

        gender_label = tkinter.Label(user_info_frame, text="Gender")
        gender_label.grid(column=1, row=3)

        nationality_label = tkinter.Label(user_info_frame, text="Nationality")
        nationality_label.grid(column=2, row=3)

        age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=99, width=20)
        age_spinbox.grid(column=0, row=4, padx=20, pady=10)

        gender_combox = ttk.Combobox(user_info_frame, values=["Male", "Female", "Binary"])
        gender_combox.grid(column=1, row=4, padx=20, pady=10)

        nationality_combox = ttk.Combobox(user_info_frame, values=NATIONALITY_LIST)
        nationality_combox.grid(column=2, row=4, padx=20, pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++ JOB INFORMATION ++++++++++++++++++++++++++++++++++++++++++++++++++++++
        job_info_frame = tkinter.LabelFrame(self.window, text="Job Information")
        job_info_frame.grid(column=1, row=2, pady=10)

        user_job_role = tkinter.Label(job_info_frame, text="Job Role")
        user_job_role.grid(column=0, row=1)

        user_job_status = tkinter.Label(job_info_frame, text="Job Status")
        user_job_status.grid(column=1, row=1)

        user_job_exp = tkinter.Label(job_info_frame, text="Year of Experience")
        user_job_exp.grid(column=2, row=1)

        user_job_combox = ttk.Combobox(job_info_frame, values=JOB_ROLE_LIST)
        user_job_combox.grid(column=0, row=2, pady=10, padx=20)

        user_status_combox = ttk.Combobox(job_info_frame, values=["Employed", "Unemployed"])
        user_status_combox.grid(column=1, row=2, pady=10, padx=20)

        year_exp_spinbox = tkinter.Spinbox(job_info_frame, from_=0, to=30)
        year_exp_spinbox.grid(column=2, row=2, padx=20, pady=10)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++++ANOTHER WIDGET++++++++++++++++++++++++++++++++++++++++++++++++++++
        to_excel_button = tkinter.Button(self.window, text="Submit data to Excel", width=77, command=self.submit_to_excel)
        to_excel_button.grid(column=1, row=3)

        to_sql_button = tkinter.Button(self.window, text="Submit data to SQLite", width=77, command=self.submit_to_sql)
        to_sql_button.grid(column=1, row=4)

        setting_button = tkinter.Button(self.window, text="Setting", width=77, command=self.setting)
        setting_button.grid(column=1, row=5)

        self.database = {"first_name_entry":first_name_entry,
                        "second_name_entry":second_name_entry,
                        "last_name_entry":last_name_entry,
                        "age_spinbox":age_spinbox,
                        "gender_combox":gender_combox,
                        "nationality_combox":nationality_combox,
                        "user_job_combox":user_job_combox,
                        "user_status_combox":user_status_combox,
                        "year_exp_spinbox":year_exp_spinbox}


        self.window.mainloop()






