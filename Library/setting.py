import time
from robot.libraries.BuiltIn import BuiltIn
from MetaData import common_data as comdata
import Library.service_port as serviceport
from Library import connection as con

global __gbefore_scanner_ihs, \
    __gstatistics_enhanced, \
    __gServicePort, \
    __gHostPort, \
    __gCurrentInterface


def print_message_to_console(msg=''):
    BuiltIn().log_to_console(msg)


def prepare_before(interface):
    current_scanner_if = 1
    match serviceport.GetScannerIHS(__gServicePort).Scanner_Interface_Number:
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
    # setting baudrate, databits, stopbits, parity for scanner, prepare before updating by host
    serviceport.set_interface(__gServicePort, interface)
    # Update current_host_name, current_sp_name, sp if current IFs != previous IFs
    if interface != current_scanner_if:
        con.connect_port()
    # clear event_log
    __gServicePort.send_command(comdata.SPCommand.sp_erase_event)
    # erase ULE
    __gServicePort.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_erase_ule)
    # erase customdata
    __gServicePort.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_erase_customdata)
    # erase .wav file
    serviceport.erase_sound_file()
    # save and reset
    __gServicePort.send_command(comdata.SPCommand.sp_save)
    __gServicePort.send_command(comdata.SPCommand.sp_reset)
    time.sleep(5)
    # get ihs before to running HDL
    __gbefore_scanner_ihs = serviceport.GetScannerIHS(__gServicePort).dict_data
    # get statistics before to running HDL
    __gbefore_statistics_enhanced = serviceport.get_enhanced_statistics(__gServicePort)


def execute_setup():
    con.connect_port()


def execute_teardown():
    return
