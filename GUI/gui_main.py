import tkinter as tk
from tkinter import messagebox

class MainGUI:
    def __init__(self, product):
        self.product = product
        if product == b'\t\x00':
            print('Curie')
        elif product == b'':
            print('Apollo')

        self.path_release = ''
        self.dict_selected_release = {}

        self.root = tk.Tk()
        self.root.title('AutoHDL')

        self.label = tk.Label(self.root, text='Selected Testcase', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 15))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.checkbox = tk.Checkbutton(self.root, text='Show Msg', font=('Arial', 18), variable=self.check_state)
        self.checkbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Execute!', font=('Arial', 18), command=self.show_msg)
        self.button.pack(padx=10, pady=10)

        self.refreshbtn = tk.Button(self.root, text='Refresh', font=('Arial', 18), command=self.clear)
        self.refreshbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
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

# MainGUI()
