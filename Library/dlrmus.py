import subprocess
import time

import Library.service_port as serviceport
from MetaData.common_data import Dlrmus as comdlr
from MetaData import common_data as comdata


class Dlrmus():

    def __init__(self, sp, from_build='', to_build='', interface=0, host_port_name=''):
        self.sp = sp
        self.from_build = from_build
        self.to_build = to_build
        self.interface = interface
        self.host_port_name = host_port_name[3:]
        self.path_file_dlrmus = r'Tools\DLRMUs\dlrmus.exe'
        match interface:
            case comdata.Interface.rs232std:
                self.dlr_interface = comdata.Dlrmus.i_RS232_STD
            case comdata.Interface.rs232wn:
                self.dlr_interface = comdata.Dlrmus.i_RS232_WN
            case comdata.Interface.rs232sc:
                self.dlr_interface = comdata.Dlrmus.i_RS232_SC
            case comdata.Interface.usbcom:
                self.dlr_interface = comdata.Dlrmus.i_USBCOM
            case comdata.Interface.usbcomsc:
                self.dlr_interface = comdata.Dlrmus.i_USBCOM_SC
            case comdata.Interface.usboem:
                self.dlr_interface = comdata.Dlrmus.i_USBOEM
            case _:
                self.dlr_interface = comdata.Dlrmus.i_RS232_STD

    # Sample Method
    def execute(self):
        print('from build: ' + self.from_build + ' to build ' + self.to_build + ' with interface ' + self.dlr_interface)
        # load from_build into scanner by ServicePort method
        cmd_dlrmus_sp = (self.path_file_dlrmus + ' '
                         + comdlr.p_select_interface + ' '
                         + comdlr.i_ServicePort + ' '
                         + comdlr.p_select_path_file + ' '
                         + self.from_build)
        # close sp because drmus update by sp
        self.sp.close_port()
        print(cmd_dlrmus_sp)
        subprocess.run(cmd_dlrmus_sp)
        self.sp.open_port()
        # check build is load success

        # setting baudrate, databits, stopbits, parity for scanner, prepare before updating by host
        serviceport.set_interface(self.sp, self.interface)

        # prepare something before HDL such as clear event_log
        self.sp.send_command(comdata.SPCommand.erase_event)

        # load to_build into scanner by HDL method
        # add more -c portname if interface is USBCOM, USBCOMSC
        set_host_port_name = ''
        set_parity = ''
        if self.interface == comdata.Interface.usbcom or self.interface == comdata.Interface.usbcomsc:
            set_host_port_name = '-c ' + self.host_port_name + ' '
        # add more -p parity = odd if interface is rs232WN
        if self.interface == comdata.Interface.rs232wn:
            set_parity = '-p o '
        cmd_dlrmus_host = (self.path_file_dlrmus + ' '
                           + comdlr.p_select_interface + ' '
                           + self.dlr_interface + ' '
                           + set_host_port_name
                           + set_parity
                           + comdlr.p_start_baudrate + ' ' + comdlr.v_baudrate_115200 + ' '
                           + comdlr.p_select_path_file + ' '
                           + self.to_build)
        print(cmd_dlrmus_host)
        subprocess.run(cmd_dlrmus_host)

        # check current status of DLRMUS, if 100%, copy log, verify scanner
        return 'logfile'
