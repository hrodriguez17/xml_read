import tkinter
from tkinter import filedialog
import os

def get_file_paths():
    while True:
        try:
            root = tkinter.Tk()
            root.withdraw()
            root.attributes('-topmost', 'true')


            print("find the file:\n")
            curr_dir = os.getcwd()
            tempdir = filedialog.askopenfilename(parent=root, initialdir=curr_dir,
                                                 title='Please select a directory',
                                                 filetypes=(("Excel Files", "*.xlsx"), ("All files", "*.*")))
            # os.chdir(os.path.dirname(os.path.abspath(curr_dir)))
            if len(tempdir) > 0:
                print(f"You chose: {tempdir}")
                # get_scope_name(tempdir)
            else:
                print("Error: Please Try Again")
            instruments_file_path.append(tempdir)
            break
        except ValueError:
            print("Please try again.")

def get_file_paths_multi(amounts):
    while True:
        try:
            root = tkinter.Tk()
            root.withdraw()
            root.attributes('-topmost', 'true')
            file_paths = []
            subroutine_amount = amounts
            print("amount!", subroutine_amount)
            curr_dir = os.getcwd()
            for _ in range(subroutine_amount):

                print("ummmmm find the file:\n")
                # curr_dir = os.getcwd()
                tempdir = filedialog.askopenfilename(parent=root, initialdir=curr_dir,
                                                     title='Please select a directory',
                                                     filetypes=(("Text files", "*.txt *.csv *.doc *.docx *.xlsx"
                                                                 ), ("All files", "*.*")))
                # os.chdir(os.path.dirname(os.path.abspath(curr_dir)))
                if len(tempdir) > 0:
                    print(f"You chose: {tempdir}")
                    file_paths.append(tempdir)
                    # get_scope_name()
                else:
                    print("Error: Please Try Again")

        except ValueError:
            print("Please try again.")

def give_path():
    return instruments_file_path[0]

def get_pid_file_paths(amounts):
    while True:
        try:
            root = tkinter.Tk()
            root.withdraw()
            root.attributes('-topmost', 'true')
            file_paths = []
            subroutine_amount = amounts
            print("amount!", subroutine_amount)
            curr_dir = os.getcwd()
            for _ in range(subroutine_amount):

                print("ummmmm find the file:\n")
                # curr_dir = os.getcwd()
                tempdir = filedialog.askopenfilename(parent=root, initialdir=curr_dir,
                                                     title='Please select a directory',
                                                     filetypes=(("Text files", "*.txt *.csv *.doc *.docx *.xlsx"
                                                                 ), ("All files", "*.*")))
                # os.chdir(os.path.dirname(os.path.abspath(curr_dir)))
                if len(tempdir) > 0:
                    print(f"You chose: {tempdir}")

                    # get_scope_name()
                else:
                    print("Error: Please Try Again")
                pid_file_path.append(tempdir)
                break
        except ValueError:
            print("Please try again.")

def get_pid_file_paths_multi(amounts):
    while True:
        try:
            root = tkinter.Tk()
            root.withdraw()
            root.attributes('-topmost', 'true')
            subroutine_amount = int(amounts)

            for _ in range(subroutine_amount):
                print("find the file:\n")
                curr_dir = os.getcwd()
                tempdir = filedialog.askopenfilename(parent=root, initialdir=curr_dir,
                                                     title='Please select a directory',
                                                     filetypes=(("Project Files", "*.L5X"), ("All files", "*.*")))
                # os.chdir(os.path.dirname(os.path.abspath(curr_dir)))
                if len(tempdir) > 0:
                    print(f"You chose: {tempdir}")

                    # get_scope_name()
                else:
                    print("Error: Please Try Again")
            pid_file_path.append(tempdir)
            break
        except ValueError:
            print("Please try again.")

def give_pid_path():
    return pid_file_path

instruments_file_path = []
pid_file_path = []
# def get_scope_name():
#         try:
#             scope_input = input("Where in the scope is this Diagram located? (Please use exact name) "
#                                 "ie: 'MainProgram':\n")
#             scope_names.append(scope_input)
#         except ValueError:
#             print("That's not an int! Please try again.")