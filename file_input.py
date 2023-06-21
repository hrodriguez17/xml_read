import tkinter
from tkinter import filedialog
import os


def get_diagram():
    while True:
        try:
            diagram_input = int(input("Which Diagram is this for?(Only Number; Do not include PID-):\n"))
            if diagram_input < 10000:
                return "{0:0>4}".format(diagram_input)
            else:
                print("Number too high!")
        except ValueError:
            print("That's not an int! Please try again.")


def get_subroutines():
    while True:
        try:
            sub_input = int(input("How Many Subroutines is this Diagram split into within the PLC?:\n"))
            if sub_input < 10:
                return sub_input
            else:
                print("Number too high!")
        except ValueError:
            print("That's not an int! Please try again.")


def get_file_paths():
    while True:
        try:
            root = tkinter.Tk()
            root.withdraw()
            root.attributes('-topmost', 'true')
            file_paths = []
            subroutine_amount = get_subroutines()

            for _ in range(subroutine_amount):
                print("find the file:\n")
                curr_dir = os.getcwd()
                tempdir = filedialog.askopenfilename(parent=root, initialdir=curr_dir,
                                                     title='Please select a directory',
                                                     filetypes=(("Text files", "*.txt *.csv *.doc *.docx *.xlsx"
                                                                 ), ("All files", "*.*")))
                os.chdir(os.path.dirname(os.path.abspath(curr_dir)))
                if len(tempdir) > 0:
                    print(f"You chose: {tempdir}")
                    file_paths.append(tempdir)
                    get_scope_name()
                else:
                    print("Error: Please Try Again")
            return file_paths
        except ValueError:
            print("Please try again.")


def get_scope_name():
        try:
            scope_input = input("Where in the scope is this Diagram located? (Please use exact name) "
                                "ie: 'MainProgram':\n")
            scope_names.append(scope_input)
        except ValueError:
            print("That's not an int! Please try again.")


scope_names = []