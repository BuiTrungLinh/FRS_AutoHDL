import subprocess
from MetaData.common_data import Dlrmus as comdlr
from MetaData import common_data as comdata

class Dlrmus():

    def __init__(self, from_build='', to_build='', interface=0):
        self.from_build = from_build
        self.to_build = to_build
        self.interface = interface
        self.path_file_dlrmus = r'../Tools/DLRMUs/dlrmus.exe'

    # Sample Method
    def execute(self):
        match self.interface:
            case comdata.Interface.rs232std:
                self.interface = comdata.Dlrmus.i_RS232_STD
            case comdata.Interface.rs232wn:
                self.interface = comdata.Dlrmus.i_RS232_WN
            case comdata.Interface.rs232sc:
                self.interface = comdata.Dlrmus.i_RS232_SC
            case comdata.Interface.usbcom:
                self.interface = comdata.Dlrmus.i_USBCOM
            case comdata.Interface.usbcomsc:
                self.interface = comdata.Dlrmus.i_USBCOM_SC
            case comdata.Interface.usboem:
                self.interface = comdata.Dlrmus.i_USBOEM
            case _:
                self.interface = comdata.Dlrmus.i_RS232_STD
        print('from build: ' + self.from_build + ' to build ' + self.to_build + ' with interface ' + self.interface)
        # load from_build into scanner by ServicePort method
        cmd_dlrmus = (self.path_file_dlrmus + ' '
                      + comdlr.p_select_interface + ' '
                      + comdlr.i_ServicePort + ' '
                      + comdlr.p_select_path_file + ' '
                      + self.from_build)
        # subprocess.run(cmd_dlrmus)
        # check build is load success

        # setting baudrate, databits, stopbits, parity for scanner, prepare before updating by host
        # set_interface(interface)

        # prepare something before HDL such as clear log file, bla bla

        # load to_build into scanner by HDL method
        # subprocess.run(self.path_file_dlrmus)

        # check current status of DLRMUS, if 100%, copy log, verify scanner