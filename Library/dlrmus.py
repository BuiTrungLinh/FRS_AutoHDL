import subprocess
import time

import Library.service_port as serviceport
from Library.setting import print_message_to_console
from MetaData.common_data import Dlrmus as comdlr
from MetaData import common_data as comdata
from Library import connection as con
from Library import setting as sett


class Dlrmus:

    def __init__(self, from_build='', to_build='', interface=0):
        self.sp = sett.__gServicePort
        self.from_build = from_build
        self.to_build = to_build
        self.interface = interface
        self.host_port_name = sett.__gHostPort[3:]
        self.path_file_dlrmus = comdata.PathFiles.path_file_dlrmus
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
    def update_by_host(self):
        # 1 = RS232STD
        current_scanner_if = 1
        match serviceport.GetScannerIHS(self.sp).Scanner_Interface_Number:
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
        print_message_to_console('Host: Update scanner to build "{}" via host.'.format(self.to_build))
        print_message_to_console(cmd_dlrmus_host)
        subprocess.run(cmd_dlrmus_host)
        # check build is load done
        # Code something here ...s
        # check current status of DLRMUS, if 100%, copy log, verify scanner
        return True

    def update_by_sp(self):
        cmd_dlrmus_sp = (self.path_file_dlrmus + ' '
                         + comdlr.p_select_interface + ' '
                         + comdlr.i_ServicePort + ' '
                         + comdlr.p_select_path_file + ' '
                         + self.from_build)
        # close sp because dlrmus is using it
        self.sp.close_port()
        print_message_to_console('SP: Load build "{}" to scanner.'.format(self.from_build))
        print_message_to_console(cmd_dlrmus_sp)
        subprocess.run(cmd_dlrmus_sp)
        time.sleep(5)
        self.sp.open_port()
        # check build is load done
        # Code something here ...s
        return True
