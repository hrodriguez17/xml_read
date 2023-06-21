from tkinter import *
from store_preset_rung import *
from main import *
from create_new_pid import *
root = Tk()

def preset_rung_screen():
    # Clear the window
    for widget in root.winfo_children():
        widget.grid_forget()

    labels = ['Preset Rung Name', 'Preset Rung Neutral Text', 'Comments', 'Parameter Objects']
    entries = []
    lbl_option = Label(root, text='Please Choose Preset:')
    lbl_option.grid(row=0, column=0, sticky=N+W)
    options = read_preset_rung_dict()
    listbox = Listbox(root, selectmode='single')
    for option in options:
        listbox.insert(END, option)
    listbox.grid(row=0, column=1, sticky= W+E)

    for i, label in enumerate(labels):
        lbl = Label(root, text=label)
        lbl.grid(row=i+1, column=0, sticky=W)
        entry = Entry(root)
        entry.grid(row=i+1, column=1, sticky=W + E)
        entries.append(entry)

    def change_label_text():
        info_raw = give_pid_path()
        info = info_raw[0]
        lbl3.config(text = info)

    def submit():
        routines = give_pid_path()
        print("theser are the routines!", routines)
        for routine in routines:
            tree = get_routine(routine)
            print("test!!!!", routine)
            dump_files(tree)
            selected_options = [listbox.get(x) for x in listbox.curselection()]
            # print("selected!!!!", selected_options[0])
            if selected_options[0] == 'Create New':
                print("Selected options:", selected_options[0])
                print("Submitted")
                rung_dict = {entries[0].get().strip(): entries[1].get()}
                rung_comments = entries[2].get()
                rung_parameters = entries[3].get()
                print('submit()', entries[0].get())
                save_preset_rung_dict(rung_dict, rung_comments, rung_parameters)
                info_send = [rung_dict.keys(), rung_dict.values(), rung_comments, rung_parameters]
                insert_rung(tree, info_send)

                write_routine(tree, routine)
                print('wrote')
            else:
                rung_dict = selected_options[0]
                rung_text = read_preset_rung_instructions(selected_options)
                rung_comments = read_preset_rung_comments(str(selected_options[0]))
                rung_parameters = read_preset_rung_parameters(selected_options[0])
                info_send = [rung_dict, rung_text, rung_comments, rung_parameters]
                insert_rung(tree, info_send)

                write_routine(tree, routine)
                print('wrote')

            # rung_parameters = entries[3].get().split(",")
        for entry in entries:
            entry.delete(0, END)

    lblr = Label(root, text='How Many Routines in P&IDs:')
    lblr.grid(row=5, column=0, sticky=W)
    entry1 = Entry(root)
    entry1.grid(row=5, column=1, sticky=W + E)
    lbl1 = Label(root, text='Please Select P&IDs File Path:')
    lbl1.grid(row=6, column=0, sticky=W)
    submit_button = Button(root, text='Find File Directory...', command=lambda: [get_pid_file_paths_multi(entry1.get()), change_label_text()])
    submit_button.grid(row=6, column=1, sticky=W + E)
    lbl2 = Label(root, text='Selected Instrument File Path:')
    lbl2.grid(row=7, column=0, sticky=W)
    lbl3 = Label(root, text='')
    lbl3.grid(row=7, column=1, sticky=W)
    inty = entry1.get()
    submit_rung_button = Button(root, text='Submit', command=submit)
    submit_rung_button.grid(row=7, column=1, sticky=W + E)

    for i in range(len(labels)):
        root.rowconfigure(i, weight=1)
        root.columnconfigure(1, weight=1)
    root.rowconfigure(len(labels), weight=1)

    submit_rung_button.config(command=lambda: [submit()])



# Create three buttons
def modify_pid_screen():
    for widget in root.winfo_children():
        widget.grid_forget()

    lbl_option = Label(root, text='Please Choose Preset:')
    lbl_option.grid(row=0, column=0, sticky=N + W)
    submit_button = Button(root, text='Insert Rung', command=preset_rung_screen)
    submit_button.grid(row=1, column=0, sticky=W + E)

def create_pid_screen():
    def change_label_text():
        info = give_path()
        lbl3.config(text = info)

    for widget in root.winfo_children():
        widget.grid_forget()
    lbl = Label(root, text='P&ID Routine Name:')
    lbl.grid(row= 1, column=0, sticky=W)
    entry = Entry(root)
    entry.grid(row=1, column=1, sticky=W + E)
    lbl1 = Label(root, text='Please Select Instrument List:')
    lbl1.grid(row=2, column=0, sticky=W)
    submit_button = Button(root, text='Find File Directory...', command=lambda: [get_file_paths(), change_label_text()])
    submit_button.grid(row=2, column=1, sticky=W + E)
    lbl2 = Label(root, text='Selected Instrument File Path:')
    lbl2.grid(row=3, column=0, sticky=W)
    lbl3 = Label(root, text='')
    lbl3.grid(row=3, column=1, sticky=W)





lbl_option = Label(root, text='Please Choose Option:')
lbl_option.grid(row=0, column=0, sticky=N + W)
submit_button = Button(root, text='Create New P&ID', command=create_pid_screen)
submit_button.grid(row=1, column=0, sticky=W + E)
submit_button2 = Button(root, text='Modify P&ID', command=modify_pid_screen)
submit_button2.grid(row=2, column=0, sticky=W + E)

# Set the weights for rows and columns
for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(0, weight=1)


width = 450 # Width
height = 450 # Height
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.mainloop()

def add_pid(path):
    pid_file_path.append(path)


pid_file_path = []