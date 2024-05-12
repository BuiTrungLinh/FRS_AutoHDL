import tkinter as tk
from tkinter import messagebox, ttk
from MetaData import common_data as comdata
import json


class MainGUI:
    def __init__(self, product):
        with open('../MetaData/software_release.json') as json_file:
            dict_software = json.load(json_file)

        self.product = product
        self.dict_software = dict_software
        self.current_dict_software = {}
        self.path_release = ''
        self.dict_selected_release = {}
        if product == b'\t\x00':
            print('Curie')
        elif product == b'':
            print('Apollo')
        elif product == b'\t':
            print('Fresco')

        self.root = tk.Tk()
        self.root.title('AutoHDL')
        self.root.config(bg="skyblue")

        # Create Frame header
        header_frame = tk.Frame(self.root)
        header_frame.grid(row=0, column=0, padx=10, pady=5)
        # Frame header - Title
        self.label = tk.Label(header_frame, text='Select Testcase', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        # Frame header - Combobox
        self.combo = ttk.Combobox(
            header_frame,
            state="readonly",
            values=["Apollo (9550i)", "Curie (900i)", "Fresco (9600i/9900i)"],
            font=('Arial', 18),
            justify='center')
        self.combo.current(0)
        self.combo.pack(padx=10, pady=10)

        # Frame body contains: interface_frame, filetype_frame, updatetype_frame, release_frame
        body_frame = tk.Frame(self.root)
        body_frame.grid(row=1, column=0, padx=10, pady=5)

        match self.combo.current():
            case comdata.Product.Apollo_index:
                self.current_dict_software = dict_software[comdata.Product.Apollo_name]
            case comdata.Product.Curie_index:
                self.current_dict_software = dict_software[comdata.Product.Apollo_name]
            case comdata.Product.Fresco_index:
                self.current_dict_software = dict_software[comdata.Product.Apollo_name]

        interface_frame = tk.Frame(body_frame, width=180, height=185, bg="purple")
        interface_frame.grid(row=0, column=0)
        # for machine in enable:
        #     enable[machine] = Variable()
        #     l = Checkbutton(self.root, text=machine, variable=enable[machine])
        #     l.pack()
        # self.checkbox = tk.Checkbutton(self.root, text='Show Msg', font=('Arial', 18), variable=self.check_state)
        # self.checkbox.pack(padx=10, pady=10)
        # self.check_state = tk.IntVar()

        filetype_frame = tk.Frame(body_frame, width=180, height=185, bg="purple")
        filetype_frame.grid(row=0, column=1)

        updatetype_frame = tk.Frame(body_frame, width=180, height=185, bg="purple")
        updatetype_frame.grid(row=0, column=2)

        release_frame = tk.Frame(body_frame, width=180, height=185, bg="purple")
        release_frame.grid(row=0, column=3)

        self.label_located = tk.Label(body_frame, text='Located Release:', font=('Arial', 10))
        self.label_located.grid(row=1, column=0, padx=5, pady=5)
        self.textbox_located = tk.Text(body_frame, height=2, font=('Arial', 15))
        self.textbox_located.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

        footer_frame = tk.Frame(self.root, width=300, height=200)
        footer_frame.grid(row=2, column=0, padx=10, pady=5)
        self.button_execute = tk.Button(footer_frame, text='Execute!', font=('Arial', 18), command=self.show_msg)
        self.button_execute.grid(row=0, column=0, padx=10, pady=10)
        #
        self.button_refresh = tk.Button(footer_frame, text='Refresh', font=('Arial', 18), command=self.clear)
        self.button_refresh.grid(row=0, column=1, padx=10, pady=10)

        cmd_frame = tk.Frame(self.root, height=100, width=200, bg="black")
        cmd_frame.grid(row=3, column=0, padx=10, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # show GUI
        self.root.mainloop()

    def show_msg(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))
            self.path_release = r'D:\tmp\CE_Release'
            self.dict_selected_release = {
                #   4= usbcom
                4: {
                    "AppOnly": {
                        1: ['DR9401638', 'DR9401643', 'DR9401646'],
                        2: ['DR9401638', 'DR9401643', 'DR9401646'],
                    },
                    "AppCfg": {
                        1: ['DR9401638', 'DR9401643', 'DR9401646'],
                    }
                },
                #   6 = usboem
                6: {
                    "AppOnly": {
                        1: ['DR9401638', 'DR9401643', 'DR9401646'],
                    },
                    "AppCfg": {
                        1: ['DR9401638', 'DR9401643', 'DR9401646'],
                        2: ['DR9401638', 'DR9401643', 'DR9401646'],
                    }
                },
                "LAST_BUILD": "DR9401648"
            }

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)
        self.checkbox.deselect()


MainGUI('')


def startup(product):
    with open('../MetaData/software_release.json') as json_file:
        data = json.load(json_file)
    MainGUI(product, data)
