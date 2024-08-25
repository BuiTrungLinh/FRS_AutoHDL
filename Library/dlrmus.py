import os
import shutil
import subprocess
import time
from datetime import datetime

from robot.libraries.BuiltIn import BuiltIn

import Library.service_port as serviceport
import MetaData.common_data as comdata
import Library.setting as sett
from MetaData.common_data import PathFiles


class Dlrmus:

    def __init__(self, from_build='', to_build='', interface=0):
        self.sp = comdata.GlobalVar.gSERVICE_PORT
        self.from_build = from_build
        self.to_build = to_build
        self.interface = interface
        self.host_port_name = comdata.GlobalVar.gHOST_PORT[3:]
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

    # Sample Method
    def update_by_host(self):
        # load to_build into scanner by HDL method
        # add more -c portname if interface is USBCOM, USBCOMSC
        set_host_port_name = ''
        set_parity = ''
        set_baudrate = ''
        # 4 = USBCOM, 5 = USBCOMSC
        if self.interface in [comdata.Interface.usbcomsc_index]:
            set_host_port_name = '-c ' + self.host_port_name + ' '
        # add more -p parity = odd if interface is rs232WN
        # 2 = RS232WN
        if self.interface in [comdata.Interface.rs232wn_index]:
            set_parity = '-p o '
        # 6 = usboem, 4 = usbcom, 5 = USBCOMSC
        if self.interface not in [comdata.Interface.usboem_index, comdata.Interface.usbcom_index,
                                  comdata.Interface.usbcomsc_index]:
            set_baudrate = comdata.Dlrmus.p_start_baudrate + ' ' + comdata.Dlrmus.v_baudrate_115200 + ' '
        cmd_dlrmus_host = (self.path_file_dlrmus + ' '
                           + comdata.Dlrmus.p_select_interface + ' '
                           + self.dlr_interface + ' '
                           + set_host_port_name
                           + set_parity
                           + set_baudrate
                           + comdata.Dlrmus.p_select_path_file + ' '
                           + self.to_build)
        sett.print_message_to_console(cmd_dlrmus_host)
        subprocess.run(cmd_dlrmus_host)
        # copy log file
        # save_log_file('log_name', 'HOST')

    def update_by_sp(self):
        cmd_dlrmus_sp = (self.path_file_dlrmus + ' '
                         + comdata.Dlrmus.p_select_interface + ' '
                         + comdata.Dlrmus.i_ServicePort + ' '
                         + comdata.Dlrmus.p_select_path_file + ' '
                         + self.from_build)
        # close sp because dlrmus is using it
        self.sp.close_port()
        sett.print_message_to_console('SP: Load build "{}" to scanner.'.format(self.from_build))
        sett.print_message_to_console(cmd_dlrmus_sp)
        subprocess.run(cmd_dlrmus_sp)
        time.sleep(5)
        # copy log file
        # save_log_file('log_name', 'SP')
        self.sp.open_port()
        # check build is load done
        obser_build = serviceport.GetScannerIHS(self.sp).dict_data[comdata.Identification.l_Application_ROM_ID]
        exp_build = self.from_build.split(r'\\')[-1].split('_')[-1][:-4]
        if obser_build != exp_build:
            return [False, comdata.Message.Error_Dlrmus_Update_SP.format(exp_build)]
        return [True, comdata.Message.Succ_Dlrmus_Update_SP.format(exp_build)]


def save_log_file(log_name, method):
    dt_string = datetime.now().strftime("%d%m%Y_%H%M%S")
    newpath = (PathFiles.path_log_folder + BuiltIn().get_variable_value("${TEST NAME}") + '_'
               + dt_string + r'\\' + method + '_' + log_name)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    # copy files to folder log
    shutil.copy(PathFiles.path_dlrmus_log_folder + log_name, newpath)
