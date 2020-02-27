from tkinter import *
from tkinter import ttk
import pickle
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.first_frame = None
        self.configure(bg='light yellow')
        self.title("Employee Management System")
        self.switch_frame(LoginPage)

    def switch_frame(self, frame):
        new_frame = frame(self)
        if self.first_frame is not None:
           self.first_frame.destroy()
        self.first_frame = new_frame
        self.first_frame.grid()
#login or registration form  appeared in employ management system

class LoginPage(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.geometry("450x300+350+80")
        self.window.configure(bg='pink')
        self.configure(bg='pink')

        #labels for login page were created
        self.lb_login_page = Label(self, text='User login', font='Times 17 bold', fg='Black', bg='pink')
        self.lb_user = Label(self, text='Username:', font='Times 15', bg='pink')
        self.lb_pass = Label(self, text='Password:', font='Times 15', bg='pink')

     # Using grid geometry manager to insert label in the window.
        self.lb_login_page.grid(row=0, column=0)
        self.lb_user.grid(row=1, column=0)
        self.lb_pass.grid(row=3, column=0)

        # Creating Entry boxes in
        self.ent_username = Entry(self)
        self.ent_password = Entry(self, show='*')

        # Using grid geometry manager to insert entry box in the window.
        self.ent_username.grid(row=1, column=1)
        self.ent_password.grid(row=3, column=1)

        # Creating Buttons for login and signup buttons:
        self.btn_login = Button(self, text='Login', command=self.login)
        self.btn_register = Button(self, text='Sign Up', command=lambda: window.switch_frame(RegisterPage))

        # Using grid geometry manager to insert button in the window.
        self.btn_login.grid(row=4, column=1, pady=5)
        self.btn_register.grid(row=6, column=1, pady=5)

        self.lb_status = Label(self, text='', bg='pink', font='Times 15')
        self.lb_status.grid(row=4, column=0)
    def login(self):
        try:
            file = open('user.pkl', 'rb')
            user_file_data = pickle.load(file)
            file.close()

            username = self.ent_username.get()
            password = self.ent_password.get()

            if user_file_data.get(username, 0) == 0:
                self.lb_status.configure(text='Invalid username or password')
                return

            if user_file_data[username]['password'] != password:
                self.lb_status.configure(text='Invalid username or password')
                return
            self.reset()
            self.window.switch_frame(DashboardPage)

        except FileNotFoundError:
            file = open('user.pkl', 'wb')
            pickle.dump({}, file)
            file.close()

    def reset(self):
        self.ent_username.delete(0, 'end')
        self.ent_password.delete(0, 'end')


class RegisterPage(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.geometry("450x300")
        self.window.configure(bg='light green')
        self.configure(bg='light green')

        # register page is created:
        self.lb_nameuser = Label(self, text='Username:', bg='light green', font='Times 13')
        self.lb_new_password = Label(self, text='New Password:', bg='light green', font='Times 13')
        self.lb_confirm_new = Label(self, text='Confirm Password:', bg='light green', font='Times 13')
        self.lb_nameuser.grid(row=1, column=0)
        self.lb_new_password.grid(row=3, column=0)
        self.lb_confirm_new.grid(row=5, column=0)
        # entry system in registration:
        self.ent_nameuser = Entry(self)
        self.ent_new_password = Entry(self)
        self.ent_confirm_new = Entry(self)

        self.ent_nameuser.grid(row=1, column=1)
        self.ent_new_password.grid(row=3, column=1)
        self.ent_confirm_new.grid(row=5, column=1)

        # Creating Buttons
        self.btn_reset = Button(self, text='Reset', command=self.reset)
        self.btn_back_to_login = Button(self, text='Back', command=lambda: window.switch_frame(LoginPage))
        self.btn_summit = Button(self, text='Submit', command=self.summit)

        # Using grid geometry manager to insert button in the window.
        self.btn_reset.grid(row=8, column=0, pady=5)
        self.btn_back_to_login.grid(row=9, column=0, pady=5)
        self.btn_summit.grid(row=10, column=0, pady=5)

        self.lb_status = Label(self, text='', bg='light green', font='Times 12')
        self.lb_status.grid(row=7, column=0)

    def summit(self):
        try:
            file = open('user.pkl', 'rb')
            user_file_data = pickle.load(file)
            file.close()

            if  self.ent_nameuser.get() == '' \
                     or self.ent_new_password.get() == '':
                self.lb_status.configure(text='Fill all boxes')
                return
            elif self.ent_new_password.get() != self.ent_confirm_new.get():
                self.lb_status.configure(text='Non matching password.')
                return
            user_data = {'password': self.ent_new_password.get()}

            nameuser = self.ent_nameuser.get()
            if user_file_data.get(nameuser, 0) != 0:
                self.lb_status.configure(text='User exists. Use another name.')
                return

            self.lb_status.configure(text='')
            user_file_data[nameuser] = user_data

            file = open('user.pkl', 'wb')
            pickle.dump(user_file_data, file)
            file.close()

            self.reset()
            self.lb_status.configure(text='Account created successfully.')

        except FileNotFoundError:
            file = open('user.pkl', 'wb')
            pickle.dump({}, file)
            file.close()

    def reset(self):
        self.ent_nameuser.delete(0, 'end')
        self.ent_new_password.delete(0, 'end')
        self.ent_confirm_new.delete(0, 'end')


class DashboardPage(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.geometry("400x250")
        self.window.configure(bg='light blue')
        self.configure(bg='light blue')

        # label
        self.lb_dashboard = Label(self, text='Dash Board', bg='light blue', font='Times 16')
        self.lb_dashboard.grid(row=0, column=0)

        # Creating Buttons
        self.btn_employee_form = Button(self, text='Employee form', command=lambda: window.switch_frame(EmployeePage))
        self.btn_department_form = Button(self, text='Department form',
                                          command=lambda: window.switch_frame(DepartmentPage))
        self.btn_logout = Button(self, text='Log Out', command=lambda: window.switch_frame(LoginPage))

        # Using grid geometry manager to insert button in the window.
        self.btn_employee_form.grid(row=1, column=1, padx=10, pady=10)
        self.btn_department_form.grid(row=2, column=1, padx=10, pady=10)
        self.btn_logout.grid(row=3, column=1, padx=10, pady=10)


class DepartmentPage(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.geometry("500x420")
        self.window.configure(bg='#ffff66')
        self.configure(bg='#ffff66')

        self.upper_frame = Frame(self, bg='#ffff66')
        self.lower_frame = Frame(self, width=400, height=304, bg='#ffff66')
        self.lower_frame.pack_propagate(0)

        self.upper_frame.pack(side=TOP)
        self.lower_frame.pack(side=BOTTOM)

        # Labels
        self.lb_depart_id = Label(self.upper_frame, text='Department Id', bg='#ffff66', font='Times 13')
        self.lb_depart_name = Label(self.upper_frame, text='Department Name', bg='#ffff66', font='Times 13')

        self.lb_depart_id.grid(row=0, column=0)
        self.lb_depart_name.grid(row=1, column=0)

        # Entries
        self.ent_depart_id = Entry(self.upper_frame)
        self.ent_depart_name = Entry(self.upper_frame)

        self.ent_depart_id.grid(row=0, column=1)
        self.ent_depart_name.grid(row=1, column=1)

        # Creating Buttons
        self.btn_add_depart = Button(self.upper_frame, text='Add department', command=self.add_department)
        self.btn_reset = Button(self.upper_frame, text='Reset', command=self.reset)
        self.btn_go_to_dashboard = Button(self.upper_frame, text='Back',
                                          command=lambda: window.switch_frame(DashboardPage))

        # Using grid geometry manager to insert button in the window.
        self.btn_reset.grid(row=2, column=0, padx=10, pady=10)
        self.btn_add_depart.grid(row=2, column=1, padx=10, pady=10)
        self.btn_go_to_dashboard.grid(row=2, column=2, padx=10, pady=10)

        self.lb_status = Label(self.upper_frame, text='', bg='#ffff66', font='Times 12')
        self.lb_status.grid(row=4, column=0)

        self.scrollbar_x = Scrollbar(self.lower_frame, orient=HORIZONTAL)
        self.scrollbar_y = Scrollbar(self.lower_frame, orient=VERTICAL)

        self.depart_table = ttk.Treeview(self.lower_frame, columns=('depart_id', 'depart_name'), height=13,
                                         xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x.pack(side=BOTTOM, fill=X)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)
        self.depart_table.place(x=0, y=0)

        self.depart_table.column('depart_id', width=190)
        self.depart_table.column('depart_name', width=190)

        self.depart_table.heading('depart_id', text='Department ID')
        self.depart_table.heading('depart_name', text='Department Name')

        self.depart_table['show'] = 'headings'

        self.scrollbar_x.configure(command=self.depart_table.xview)
        self.scrollbar_y.configure(command=self.depart_table.yview)

        self.show_department()

    def show_department(self):
        self.depart_table.delete(*self.depart_table.get_children())

        try:
            file = open('department_data.pkl', 'rb')
            department_data = pickle.load(file)
            file.close()

            department = []
            for key in department_data:
                department.append((key, department_data[key]))

            for data in department:
                self.depart_table.insert('', 'end', values=data)

        except FileNotFoundError:
            file = open('department_data.pkl', 'wb')
            pickle.dump({}, file)
            file.close()

    def add_department(self):
        try:
            file = open('department_data.pkl', 'rb')
            department_data = pickle.load(file)
            file.close()

            department_id = self.ent_depart_id.get()
            department_name = self.ent_depart_name.get()

            if department_id == '' or department_name == '':
                self.lb_status.configure(text='Fill all the entries')
                return

            elif department_data.get(department_id, 0) != 0:
                self.lb_status.configure(text='Department id already exists')
                return
            elif department_name in department_data.values():
                self.lb_status.configure(text='Department name already exists')
                return

            department_data.setdefault(department_id, department_name)

            file = open('department_data.pkl', 'wb')
            pickle.dump(department_data, file)
            file.close()

            self.reset()
            self.lb_status.configure(text='Department added successfully.')

            self.show_department()

        except FileNotFoundError:
            file = open('department_data.pkl', 'wb')
            pickle.dump({}, file)
            file.close()

    def reset(self):
        self.ent_depart_id.delete(0, 'end')
        self.ent_depart_name.delete(0, 'end')


class EmployeePage(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.geometry("700x500")
        self.window.configure(bg='light blue')
        self.configure(bg='light blue')

        self.upper_frame = Frame(self, bg='light blue')
        self.lower_frame = Frame(self, width=670, height=245, bg='light blue')
        self.lower_frame.pack_propagate(0)

        self.upper_frame.pack(side=TOP)
        self.lower_frame.pack(side=BOTTOM)

        self.lb_id = Label(self.upper_frame, text='Id No.', bg='light blue', font='Times 13')
        self.lb_fname = Label(self.upper_frame, text='First name:', bg='light blue', font='Times 13')
        self.lb_lname = Label(self.upper_frame, text='Last name:', bg='light blue', font='Times 13')
        self.lb_age = Label(self.upper_frame, text='Age:', bg='light blue', font='Times 13')
        self.lb_number = Label(self.upper_frame, text='Phone number:', bg='light blue', font='Times 13')
        self.lb_address = Label(self.upper_frame, text='Address', bg='light blue', font='Times 13')

        self.lb_id.grid(row=1, column=0)
        self.lb_fname.grid(row=2, column=0)
        self.lb_lname.grid(row=3, column=0)
        self.lb_age.grid(row=4, column=0)
        self.lb_number.grid(row=5, column=0)
        self.lb_address.grid(row=6, column=0)

        self.ent_id = Entry(self.upper_frame)
        self.ent_fname = Entry(self.upper_frame)
        self.ent_lname = Entry(self.upper_frame)
        self.ent_age = Entry(self.upper_frame)
        self.ent_number = Entry(self.upper_frame)
        self.ent_address = Entry(self.upper_frame)

        self.ent_id.grid(row=1, column=1)
        self.ent_fname.grid(row=2, column=1)
        self.ent_lname.grid(row=3, column=1)
        self.ent_age.grid(row=4, column=1)
        self.ent_number.grid(row=5, column=1)
        self.ent_address.grid(row=6, column=1)

        self.scrollbar_x = Scrollbar(self.lower_frame, orient=HORIZONTAL)
        self.scrollbar_y = Scrollbar(self.lower_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(self.lower_frame, columns=('id', 'firstname', 'lastname', 'age', 'number',
                                                                      'address', 'department'),
                                           xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x.pack(side=BOTTOM, fill=X)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)
        self.employee_table.place(x=0, y=0)

        self.employee_table.column('id', width=50)
        self.employee_table.column('firstname', width=100)
        self.employee_table.column('lastname', width=100)
        self.employee_table.column('age', width=100)
        self.employee_table.column('number', width=100)
        self.employee_table.column('address', width=100)
        self.employee_table.column('department', width=100)

        self.employee_table.heading('id', text='ID')
        self.employee_table.heading('firstname', text='First Name')
        self.employee_table.heading('lastname', text='Last Name')
        self.employee_table.heading('age', text='Age')
        self.employee_table.heading('number', text='Number')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('department', text='Department')

        self.employee_table['show'] = 'headings'

        self.scrollbar_x.configure(command=self.employee_table.xview)
        self.scrollbar_y.configure(command=self.employee_table.yview)

        try:
            file = open('department_data.pkl', 'rb')
            department_data = pickle.load(file)
            file.close()

        except FileNotFoundError:
            file = open('department_data.pkl', 'wb')
            pickle.dump({}, file)
            file.close()

            file = open('department_data.pkl', 'rb')
            department_data = pickle.load(file)
            file.close()

        self.options = ['']
        for value in department_data.values():
            self.options.append(value)

        self.lb_choose_depart = Label(self.upper_frame, text='Choose department', bg='light blue', font='Times 13')
        self.lb_choose_depart.grid(row=7, column=0)

        # Options menu
        self.department = StringVar()
        self.department.set('None')
        self.options_department = OptionMenu(self.upper_frame, self.department, *self.options)
        self.options_department.grid(row=7, column=1)

        # Creating Buttons
        self.btn_add = Button(self.upper_frame, text='Add employee', command=self.add_employee)
        self.btn_reset = Button(self.upper_frame, text='Reset', command=self.reset)
        self.btn_back_to_dashboard = Button(self.upper_frame, text='Back',
                                            command=lambda: window.switch_frame(DashboardPage))

        # Using grid geometry manager to insert button in the window.
        self.btn_reset.grid(row=8, column=0, padx=10, pady=10)
        self.btn_add.grid(row=8, column=1, padx=10, pady=10)
        self.btn_back_to_dashboard.grid(row=8, column=2, padx=10, pady=10)

        self.lb_status = Label(self.upper_frame, text='', bg='light blue', font='Times 12')
        self.lb_status.grid(row=9, column=0)
        self.show_employee()

    def show_employee(self):
        self.employee_table.delete(*self.employee_table.get_children())

        try:
            file = open('employee_info.pkl', 'rb')
            employee_info = pickle.load(file)
            file.close()

            employee_list = []
            for key in employee_info:
                employee_list.append((key, employee_info[key]['firstname'],
                                      employee_info[key]['lastname'],
                                      employee_info[key]['age'],
                                      employee_info[key]['number'],
                                      employee_info[key]['address'],
                                      employee_info[key]['department']))

            for data in employee_list:
                self.employee_table.insert('', 'end', values=data)

        except FileNotFoundError:
            file = open('employee_info.pkl', 'wb')
            pickle.dump({}, file)
            file.close()

    def add_employee(self):
        try:
            file = open('employee_info.pkl', 'rb')
            employee_info = pickle.load(file)
            file.close()

            if self.ent_fname.get() == '' or self.ent_lname.get() == '' or \
                    self.ent_age.get() == '' or self.ent_number.get() == '' or self.ent_address.get() == '':
                self.lb_status.configure(text='Fill all the entries')
                return

            elif self.department.get() == 'None' or self.department.get() == '':
                self.lb_status.configure(text='Select department')
                return

            elif not self.ent_age.get().isdigit():
                self.lb_status.configure(text='Age must be number')
                return

            elif int(self.ent_age.get()) > 50:
                self.lb_status.configure(text='Age should be < 50')
                return

            elif not self.ent_number.get().isdigit() and 8 < len(self.ent_number.get()) < 14:
                self.lb_status.configure(text='Contact should contain (8-13)digit.')
                return

            employee_id = self.ent_id.get()
            employee_dict = {'firstname': self.ent_fname.get(),
                             'lastname': self.ent_lname.get(),
                             'age': self.ent_age.get(),
                             'number': self.ent_number.get(),
                             'address': self.ent_address.get(),
                             'department': self.department.get()}

            if employee_info.get(employee_id, 0) != 0:
                self.lb_status.configure(text='Employee already exists.')
                return

            employee_info[employee_id] = employee_dict

            file = open('employee_info.pkl', 'wb')
            pickle.dump(employee_info, file)
            file.close()

            self.reset()
            self.lb_status.configure(text='Employee added successfully.')
            self.show_employee()

        except FileNotFoundError:
            file = open('employee_info.pkl', 'wb')
            pickle.dump({}, file)
            file.close()

    def reset(self):
        self.ent_id.delete(0, 'end')
        self.ent_fname.delete(0, 'end')
        self.ent_lname.delete(0, 'end')
        self.ent_age.delete(0, 'end')
        self.ent_number.delete(0, 'end')
        self.ent_address.delete(0, 'end')


application = App()
application.mainloop()
