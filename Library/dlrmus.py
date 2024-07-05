import subprocess
import time
import Library.service_port as serviceport
import MetaData.common_data as comdata
import Library.setting as sett


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
        if self.interface in [comdata.Interface.usbcom_index, comdata.Interface.usbcomsc_index]:
            set_host_port_name = '-c ' + self.host_port_name + ' '
        # add more -p parity = odd if interface is rs232WN
        # 2 = RS232WN
        if self.interface in [comdata.Interface.rs232wn_index]:
            set_parity = '-p o '
        # 6 = usboem, 4 = usbcom, 5 = USBCOMSC
        if self.interface not in [comdata.Interface.usboem_index, comdata.Interface.usbcom_index, comdata.Interface.usbcomsc_index]:
            set_baudrate = comdata.Dlrmus.p_start_baudrate + ' ' + comdata.Dlrmus.v_baudrate_115200 + ' '
        cmd_dlrmus_host = (self.path_file_dlrmus + ' '
                           + comdata.Dlrmus.p_select_interface + ' '
                           + self.dlr_interface + ' '
                           + set_host_port_name
                           + set_parity
                           + set_baudrate
                           + comdata.Dlrmus.p_select_path_file + ' '
                           + self.to_build)
        sett.print_message_to_console('Host: Update scanner to build "{}" via host.'.format(self.to_build))
        sett.print_message_to_console(cmd_dlrmus_host)
        subprocess.run(cmd_dlrmus_host)
        # check build is load done
        # Code something here ...s
        # check current status of DLRMUS, if 100%, copy log, verify scanner
        return True

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
        self.sp.open_port()
        # check build is load done
        # Code something here ...s
        return True
