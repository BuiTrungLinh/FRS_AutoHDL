import time
from robot.libraries.BuiltIn import BuiltIn
import Library.service_port as serviceport
import Library.connection as con
import MetaData.common_data as comdata
from MetaData.common_data import GlobalVar as GVar
from MetaData.common_data import SPCommand as SpCMD


def __init__(service_port, host_port, current_ifs):
    GVar.gSERVICE_PORT = service_port
    GVar.gHOST_PORT = host_port
    GVar.gCURRENT_INTERFACE = current_ifs


def execute_setup(product_id):
    GVar.gPRODUCT_ID = product_id
    con.connect_port()


def execute_teardown():
    # clear event_log
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_erase_event)
    # erase ULE
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_write_cfg + SpCMD.cfg_erase_ule)
    # erase customdata
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_write_cfg + SpCMD.cfg_erase_customdata)
    # erase overide file
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_erase_custom_file)
    # Erase config name
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_write_cfg + SpCMD.cfg_config_file_id + SpCMD.val_config_file_id)
    # Todo
    # erase .wav file
    serviceport.erase_sound_file()
    # save and reset
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_save)
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_reset)
    time.sleep(5)
    GVar.gSERVICE_PORT.close_port()


def execute_before_hdl(interface_name):
    current_scanner_if = 1
    match serviceport.GetScannerIHS(GVar.gSERVICE_PORT).Scanner_Interface_Number:
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
    interface = 1
    for ifs in comdata.Interface.dict_interface:
        if interface_name.replace('-', '').replace(' ', '').upper() == comdata.Interface.dict_interface[ifs]['name']:
            interface = ifs
    serviceport.set_interface(GVar.gSERVICE_PORT, interface)
    # Update current_host_name, current_sp_name, sp if current IFs != previous IFs
    if interface != current_scanner_if:
        con.connect_port()
    # clear event_log
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_erase_event)
    # erase ULE
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_write_cfg + SpCMD.cfg_erase_ule)
    # erase customdata
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_write_cfg + SpCMD.cfg_erase_customdata)
    # erase overide file
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_erase_custom_file)
    # update config name
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_write_cfg + SpCMD.cfg_config_file_id + SpCMD.val_config_file_id)
    # erase .wav file
    serviceport.erase_sound_file()
    # save and reset
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_save)
    GVar.gSERVICE_PORT.send_command(SpCMD.sp_reset)
    time.sleep(7)
    # get ihs before to running HDL
    GVar.gBEFORE_SCANNER_IHS = serviceport.GetScannerIHS(GVar.gSERVICE_PORT).dict_data
    # get statistics before to running HDL
    GVar.gBEFORE_STATISTICS_ENHANCED = serviceport.get_enhanced_statistics()


def print_message_to_console(msg=''):
    BuiltIn().log_to_console(msg)
