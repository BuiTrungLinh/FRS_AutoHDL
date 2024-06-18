import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
from tkinter import filedialog
from webbrowser import get

from MetaData import common_data as comdata
from MetaData.common_data import Message as msg
import json

class MainGUI:
    def __init__(self):
        with open('MetaData/software_release.json') as json_file:
            self.dict_release = json.load(json_file)
        self.path_release = ''
        self.dict_current_release = {}
        self.dict_selected_release = {}

        # Start layout
        self.root = tk.Tk()
        self.root.title('AutoHDL')
        self.root.config(bg="skyblue")
        # self.root.geometry("900x800")

        # Create Frame header
        header_frame = tk.Frame(self.root)
        header_frame.grid(row=0, column=0, padx=10, pady=5)
        # Frame header - Title
        label_title = tk.Label(header_frame, text='Select Testcase', font=('Arial', 18))
        label_title.pack(padx=10, pady=10)
        # Frame header - Combobox
        self.combo_select_product = ttk.Combobox(
            header_frame,
            state="readonly",
            values=["Apollo (9550i)", "Curie (900i)", "Fresco (9600i/9900i)"],
            font=('Arial', 18),
            justify='center')
        self.combo_select_product.current(0)
        self.combo_select_product.pack(padx=10, pady=10)
        # self.combo_select_product.trace('w', self.changed_product)
        self.combo_select_product.bind('<<ComboboxSelected>>', self.changed_product)

        # Frame body contains: interface_frame, filetype_frame, updatetype_frame, release_frame
        self.body_frame = tk.Frame(self.root)
        self.body_frame.grid(row=1, column=0, padx=10, pady=5)

        self.load_body()

        located_frame = tk.Frame(self.root)
        located_frame.grid(row=2, column=0, padx=10, pady=5)
        self.label_located = tk.Label(located_frame, text='Located Release:', font='Arial 10 bold')
        self.label_located.grid(row=1, column=1, padx=5, pady=5)
        self.textbox_located = tk.Text(located_frame, height=1, width=50, font=('Arial', 10))
        self.textbox_located.grid(row=1, column=2, padx=5, pady=5)

        footer_frame = tk.Frame(self.root, width=300, height=200)
        footer_frame.grid(row=3, column=0, padx=10, pady=5)
        self.button_execute = tk.Button(footer_frame, text='Execute!', font=('Arial', 18), command=self.execute_hdl)
        self.button_execute.grid(row=0, column=0, padx=10, pady=10)
        #
        self.button_refresh = tk.Button(footer_frame, text='Refresh', font=('Arial', 18), command=self.clear)
        self.button_refresh.grid(row=0, column=1, padx=10, pady=10)

        cmd_frame = tk.Frame(self.root, height=100, width=200, bg="black")
        cmd_frame.grid(row=4, column=0, padx=10, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # show GUI
        self.root.mainloop()

    def load_body(self):
        # clear all data in body_frame
        for widgets in self.body_frame.winfo_children():
            widgets.destroy()
        # load data in combo_select_product
        dict_current_interface = None
        match self.combo_select_product.current():
            case comdata.Product.Apollo_index:
                self.dict_current_release = self.dict_release[comdata.Product.Apollo_name]
                dict_current_interface = comdata.Product.Apollo_interface
            case comdata.Product.Curie_index:
                self.dict_current_release = self.dict_release[comdata.Product.Curie_name]
                dict_current_interface = comdata.Product.Curie_interface
            case comdata.Product.Fresco_index:
                self.dict_current_release = self.dict_release[comdata.Product.Fresco_name]
                dict_current_interface = comdata.Product.Fresco_interface

        interface_frame = tk.LabelFrame(self.body_frame, text='Interface', font='Arial 10 bold')
        interface_frame.grid(row=0, column=0, padx=10, sticky="NE")
        # create dict of check_boxes
        self.check_boxes_ifs = {item: tk.IntVar() for item in dict_current_interface}
        for interface in dict_current_interface:
            tmp = tk.Checkbutton(interface_frame, text=dict_current_interface[interface]["name"],
                                 variable=self.check_boxes_ifs[interface], font=('Arial', 10), anchor='w')
            tmp.pack(padx=10, pady=10, fill='both')

        filetype_frame = tk.LabelFrame(self.body_frame, text='File-Type', font='Arial 10 bold')
        filetype_frame.grid(row=0, column=1, padx=10, sticky="NE")
        self.check_boxes_filetype = {item: tk.IntVar() for item in comdata.FileType.dict_filetype}
        for filetype in comdata.FileType.dict_filetype:
            tmp = tk.Checkbutton(filetype_frame, text=comdata.FileType.dict_filetype[filetype]["name"],
                                 variable=self.check_boxes_filetype[filetype], font=('Arial', 10), anchor='w')
            tmp.pack(padx=10, pady=10, fill='both')

        updatetype_frame = tk.LabelFrame(self.body_frame, text='Update-Type', font='Arial 10 bold')
        updatetype_frame.grid(row=0, column=2, padx=10, sticky="NE")
        self.check_boxes_updatetype = {item: tk.IntVar() for item in comdata.UpdateType.dict_updatetype}
        for updatetype in comdata.UpdateType.dict_updatetype:
            tmp = tk.Checkbutton(updatetype_frame, text=comdata.UpdateType.dict_updatetype[updatetype]["name"],
                                 variable=self.check_boxes_updatetype[updatetype], font=('Arial', 10), anchor='w')
            tmp.pack(padx=10, pady=10, fill='both')

        release_frame = tk.LabelFrame(self.body_frame, text='Release', font='Arial 10 bold')
        release_frame.grid(row=0, column=3, padx=10, sticky="NE")
        tmp_row = 0
        self.check_boxes_release = {}
        for mr in self.dict_current_release:
            label_mr = tk.Label(release_frame, text='--- {}'.format(mr), font='Arial 10 bold')
            label_mr.grid(row=tmp_row, sticky="W", padx=15)
            if mr == 'Latest Build' or mr == 'Feature Build':
                label_mr.config(text='{}: {}'.format(mr, self.dict_current_release[mr]))
                label_mr.grid(columnspan=2)
                tmp_row = tmp_row + 1
                continue
            self.check_boxes_release[mr] = {item: tk.IntVar() for item in self.dict_current_release[mr]}
            for rc in self.dict_current_release[mr]:
                tmp_row = tmp_row + 1
                checkbox_rc = tk.Checkbutton(release_frame, text='{} {}'.format(rc, self.dict_current_release[mr][rc]),
                                             variable=self.check_boxes_release[mr][rc], font=('Arial', 10))
                checkbox_rc.grid(row=tmp_row, column=1, sticky="W")
            tmp_row = tmp_row + 1

    def changed_product(self, event):
        self.load_body()
        # messagebox.showinfo(title=msg.Error_Title, message=self.combo_select_product.get())

    def execute_hdl(self):
        self.gen_dict_release()

    def gen_dict_release(self):
        filetype = {}
        updatetype = {}
        release = []
        self.path_release = self.textbox_located.get("1.0", tk.END)

        # Check if checkbox does not select
        if 1 not in ([item.get() for item in self.check_boxes_ifs.values()]):
            messagebox.showinfo(title=msg.Error_Title, message=msg.Error_No_Selected_IFs)
            return
        elif 1 not in ([item.get() for item in self.check_boxes_filetype.values()]):
            messagebox.showinfo(title=msg.Error_Title, message=msg.Error_No_Selected_FileType)
            return
        elif 1 not in ([item.get() for item in self.check_boxes_updatetype.values()]):
            messagebox.showinfo(title=msg.Error_Title, message=msg.Error_No_Selected_UpdateType)
            return

        tmp_list = []
        for tmp_item_1 in self.dict_current_release:
            if tmp_item_1 not in ['Latest Build', 'Feature Build']:
                for tmp_item_2 in self.dict_current_release[tmp_item_1]:
                    tmp_list.append((self.check_boxes_release[tmp_item_1][tmp_item_2].get()))
        if 1 not in tmp_list:
            messagebox.showinfo(title=msg.Error_Title, message=msg.Error_No_Selected_Release)
            return

        if not self.path_release.strip():
            messagebox.showinfo(title=msg.Error_Title, message=msg.Error_No_Located_Path)
            return

        for item in self.check_boxes_ifs:
            if self.check_boxes_ifs[item].get() == 1:
                for item_filetype in self.check_boxes_filetype:
                    if self.check_boxes_filetype[item_filetype].get() == 1:
                        for item_updatetype in self.check_boxes_updatetype:
                            if self.check_boxes_updatetype[item_updatetype].get() == 1:
                                release.clear()
                                for item_release_mr in self.dict_current_release:
                                    if item_release_mr not in ['Latest Build', 'Feature Build']:
                                        for item_release_rc in self.dict_current_release[item_release_mr]:
                                            if self.check_boxes_release[item_release_mr][item_release_rc].get() == 1:
                                                release.append(
                                                    self.dict_current_release[item_release_mr][item_release_rc])
                                        updatetype[item_updatetype] = release
                        filetype[item_filetype] = updatetype
                self.dict_selected_release[item] = filetype

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        for item in self.check_boxes_ifs:
            self.check_boxes_ifs[item].set(0)
        for item in self.check_boxes_filetype:
            self.check_boxes_filetype[item].set(0)
        for item in self.check_boxes_updatetype:
            self.check_boxes_updatetype[item].set(0)
        for item in self.check_boxes_release:
            for tmp_item in self.check_boxes_release[item]:
                self.check_boxes_release[item][tmp_item].set(0)
        self.textbox_located.delete("1.0", tk.END)


def startup():
    MainGUI()
