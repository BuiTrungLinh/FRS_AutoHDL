import subprocess
import time

import Library.service_port as serviceport
from MetaData.common_data import Dlrmus as comdlr
from MetaData import common_data as comdata
from Library import connection as con


class Dlrmus:

    def __init__(self, sp, from_build='', to_build='', interface=0, host_port_name=''):
        self.sp = sp
        self.from_build = from_build
        self.to_build = to_build
        self.interface = interface
        self.host_port_name = host_port_name[3:]
        # self.path_file_dlrmus = r'..\Tools\DLRMUs\dlrmus.exe'
        self.path_file_dlrmus = r'D:\1.DevelopmentTool\PycharmProjects\FRS_AutoHDL\Tools\DLRMUs\dlrmus.exe'
        match interface:
            case comdata.Interface.rs232std_index:
                self.dlr_interface = comdata.Dlrmus.i_RS232_STD
            case comdata.Interface.rs232wn_index:
                self.dlr_interface = comdata.Dlrmus.i_RS232_WN
            case comdata.Interface.rs232sc_index:
                self.dlr_interface = comdata.Dlrmus.i_RS232_SC
            case comdata.Interface.usbcom_index:
                self.dlr_interface = comdata.Dlrmus.i_USBCOM
            case comdata.Interface.usbcomsc_index:
                self.dlr_interface = comdata.Dlrmus.i_USBCOM_SC
            case comdata.Interface.usboem_index:
                self.dlr_interface = comdata.Dlrmus.i_USBOEM
            case _:
                self.dlr_interface = comdata.Dlrmus.i_RS232_STD

    # Sample Method
    def execute(self):
        # 1 = RS232STD
        current_scanner_if = 1
        match serviceport.get_scanner_current_information(self.sp, comdata.Identification.Scanner_Interface_Number):
            case comdata.RS232STD.interface_type:
                current_scanner_if = comdata.Interface.rs232std_index
            case comdata.RS232WN.interface_type:
                current_scanner_if = comdata.Interface.rs232wn_index
            case comdata.RS232SC.interface_type:
                current_scanner_if = comdata.Interface.rs232sc_index
            case comdata.USBCOM.interface_type:
                current_scanner_if = comdata.Interface.usbcom_index
            case comdata.USBCOMSC.interface_type:
                current_scanner_if = comdata.Interface.usbcomsc_index
            case comdata.USBOEM.interface_type:
                current_scanner_if = comdata.Interface.usboem_index

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
        # subprocess.run(cmd_dlrmus_sp)
        time.sleep(5)
        self.sp.open_port()
        # check build is load success
        # setting baudrate, databits, stopbits, parity for scanner, prepare before updating by host
        serviceport.set_interface(self.sp, self.interface)
        # Update current_host_name, current_sp_name, sp if current IFs != previous IFs
        if self.interface != current_scanner_if:
            current_scanner_if = self.interface
            re_connect = con.connect_port()
            self.__init__(re_connect[0], interface=self.interface, host_port_name=re_connect[1]['current_host_name'])

        # prepare something before HDL such as clear event_log
        self.sp.send_command(comdata.SPCommand.erase_event)

        # load to_build into scanner by HDL method
        # add more -c portname if interface is USBCOM, USBCOMSC
        set_host_port_name = ''
        set_parity = ''
        set_baudrate = ''
        if self.interface == comdata.Interface.usbcom_index or self.interface == comdata.Interface.usbcomsc_index:
            set_host_port_name = '-c ' + self.host_port_name + ' '
        # add more -p parity = odd if interface is rs232WN
        if self.interface == comdata.Interface.rs232wn_index:
            set_parity = '-p o '
        if self.interface not in [comdata.Interface.usboem_index, comdata.Interface.usbcom_index]:
            set_baudrate = comdlr.p_start_baudrate + ' ' + comdlr.v_baudrate_115200 + ' '
        cmd_dlrmus_host = (self.path_file_dlrmus + ' '
                           + comdlr.p_select_interface + ' '
                           + self.dlr_interface + ' '
                           + set_host_port_name
                           + set_parity
                           + set_baudrate
                           + comdlr.p_select_path_file + ' '
                           + self.to_build)
        print(cmd_dlrmus_host)
        subprocess.run(cmd_dlrmus_host)

        # check current status of DLRMUS, if 100%, copy log, verify scanner
        return 'logfile'
