import tkinter as tk
from tkinter import messagebox, ttk
from webbrowser import get

from MetaData import common_data as comdata
import json


class MainGUI:
    def __init__(self):
        with open('MetaData/software_release.json') as json_file:
            dict_software = json.load(json_file)
        self.product = ''
        self.dict_software = dict_software
        self.current_dict_release = {}
        self.path_release = ''
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

        # Frame body contains: interface_frame, filetype_frame, updatetype_frame, release_frame
        body_frame = tk.Frame(self.root)
        body_frame.grid(row=1, column=0, padx=10, pady=5)

        dict_current_interface = None
        match self.combo_select_product.current():
            case comdata.Product.Apollo_index:
                self.current_dict_release = dict_software[comdata.Product.Apollo_name]
                dict_current_interface = comdata.Product.Apollo_interface
            case comdata.Product.Curie_index:
                self.current_dict_release = dict_software[comdata.Product.Curie_name]
                dict_current_interface = comdata.Product.Curie_interface
            case comdata.Product.Fresco_index:
                self.current_dict_release = dict_software[comdata.Product.Fresco_name]
                dict_current_interface = comdata.Product.Fresco_interface

        interface_frame = tk.Frame(body_frame, width=180, height=185, bg="purple")
        interface_frame.grid(row=0, column=0)
        # create dict of check_boxes
        self.check_boxes_ifs = {item: tk.IntVar() for item in dict_current_interface}
        for interface in dict_current_interface:
            tmp = tk.Checkbutton(interface_frame, text=dict_current_interface[interface]["name"],
                                 variable=self.check_boxes_ifs[interface], font=('Arial', 10), onvalue=1, offvalue=0)
            tmp.pack(padx=10, pady=10)

        filetype_frame = tk.Frame(body_frame, width=180, height=185, bg="purple")
        filetype_frame.grid(row=0, column=1)
        self.check_boxes_filetype = {item: tk.IntVar() for item in comdata.FileType.dict_filetype}
        for filetype in comdata.FileType.dict_filetype:
            tmp = tk.Checkbutton(filetype_frame, text=comdata.FileType.dict_filetype[filetype]["name"],
                                 variable=self.check_boxes_filetype[filetype], font=('Arial', 10))
            tmp.pack(padx=10, pady=10)

        updatetype_frame = tk.Frame(body_frame, width=180, height=185, bg="purple")
        updatetype_frame.grid(row=0, column=2)
        self.check_boxes_updatetype = {item: tk.IntVar() for item in comdata.UpdateType.dict_updatetype}
        for updatetype in comdata.UpdateType.dict_updatetype:
            tmp = tk.Checkbutton(updatetype_frame, text=comdata.UpdateType.dict_updatetype[updatetype]["name"],
                                 variable=self.check_boxes_updatetype[updatetype], font=('Arial', 10))
            tmp.pack(padx=10, pady=10)

        release_frame = tk.Frame(body_frame, width=180, height=185, bg="purple")
        release_frame.grid(row=0, column=3)
        tmp_row = 0
        self.check_boxes_release = {}
        for mr in self.current_dict_release:
            label_mr = tk.Label(release_frame, text='--- {}'.format(mr), font=('Arial', 15))
            label_mr.grid(row=tmp_row, column=0, pady=10)
            if mr == 'Latest Build' or mr == 'Feature Build':
                label_mr.config(text='{}: {}'.format(mr, self.current_dict_release[mr]))
                label_mr.grid(columnspan=2)
                tmp_row = tmp_row + 1
                continue
            self.check_boxes_release[mr] = {item: tk.IntVar() for item in self.current_dict_release[mr]}
            for rc in self.current_dict_release[mr]:
                tmp_row = tmp_row + 1
                checkbox_rc = tk.Checkbutton(release_frame, text='{} {}'.format(rc, self.current_dict_release[mr][rc]),
                                             variable=self.check_boxes_release[mr][rc], font=('Arial', 10))
                checkbox_rc.grid(row=tmp_row, column=1, pady=5)
            tmp_row = tmp_row + 1

        located_frame = tk.Frame(self.root)
        located_frame.grid(row=2, column=0, padx=10, pady=5)
        self.label_located = tk.Label(located_frame, text='Located Release:', font=('Arial', 10))
        self.label_located.grid(row=1, column=1, padx=5, pady=5)
        self.textbox_located = tk.Text(located_frame, height=1, width=50, font=('Arial', 15))
        self.textbox_located.grid(row=1, column=2, padx=5, pady=5)

        def show_msg():
            self.dict_selected_release = {}
            filetype = {}
            updatetype = {}
            release = []
            for item in self.check_boxes_ifs:
                if self.check_boxes_ifs[item].get() == 1:
                    for item_filetype in self.check_boxes_filetype:
                        if self.check_boxes_filetype[item_filetype].get() == 1:
                            for item_updatetype in self.check_boxes_updatetype:
                                if self.check_boxes_updatetype[item_updatetype].get() == 1:
                                    release.clear()
                                    for item_release_mr in self.current_dict_release:
                                        if item_release_mr not in ['Latest Build', 'Feature Build']:
                                            for item_release_rc in self.current_dict_release[item_release_mr]:
                                                if self.check_boxes_release[item_release_mr][item_release_rc].get() == 1:
                                                    release.append(
                                                        self.current_dict_release[item_release_mr][item_release_rc])
                                            updatetype[item_updatetype] = release
                            filetype[item_filetype] = updatetype
                    self.dict_selected_release[item] = filetype
            path_release = self.textbox_located.get("1.0", tk.END)
            # if not path_release.strip():
            #     messagebox.showinfo(title='Error-Message', message='Please enter file path!!!')
            # else:
            #     # self.path_release = path_release
            #     self.path_release = r'D:\tmp\CE_Release'
            #     for item in self.check_boxes_ifs:
            #         print(item)
            # if self.check_state.get() == 0:
            #     print(self.textbox.get('1.0', tk.END))
            # else:
            #     messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))
            #     self.dict_selected_release = {
            #         #   4= usbcom
            #         4: {
            #             "AppOnly": {
            #                 1: ['DR9401638', 'DR9401643', 'DR9401646'],
            #                 2: ['DR9401638', 'DR9401643', 'DR9401646'],
            #             },
            #             "AppCfg": {
            #                 1: ['DR9401638', 'DR9401643', 'DR9401646'],
            #             }
            #         },
            #         #   6 = usboem
            #         6: {
            #             "AppOnly": {
            #                 1: ['DR9401638', 'DR9401643', 'DR9401646'],
            #             },
            #             "AppCfg": {
            #                 1: ['DR9401638', 'DR9401643', 'DR9401646'],
            #                 2: ['DR9401638', 'DR9401643', 'DR9401646'],
            #             }
            #         },
            #         "LAST_BUILD": "DR9401648"
            #     }

        footer_frame = tk.Frame(self.root, width=300, height=200)
        footer_frame.grid(row=3, column=0, padx=10, pady=5)
        self.button_execute = tk.Button(footer_frame, text='Execute!', font=('Arial', 18), command=show_msg)
        self.button_execute.grid(row=0, column=0, padx=10, pady=10)
        #
        self.button_refresh = tk.Button(footer_frame, text='Refresh', font=('Arial', 18), command=self.clear)
        self.button_refresh.grid(row=0, column=1, padx=10, pady=10)

        cmd_frame = tk.Frame(self.root, height=100, width=200, bg="black")
        cmd_frame.grid(row=4, column=0, padx=10, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # show GUI
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)
        self.checkbox.deselect()


MainGUI()


def startup():
    MainGUI()
