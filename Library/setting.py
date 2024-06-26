from robot.libraries.BuiltIn import BuiltIn
from Library import global_var
from MetaData import common_data as comdata
import Library.service_port as serviceport


def print_message_to_console(msg=''):
    BuiltIn().log_to_console(msg)


def prepare_before():
    sp = global_var.__gServicePort
    # prepare something before HDL such as clear event_log
    sp.send_command(comdata.SPCommand.sp_erase_event)
    sp.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_erase_ule)
    sp.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_erase_customdata)
    sp.send_command(comdata.SPCommand.sp_save)
    sp.send_command(comdata.SPCommand.sp_reset)
    # get data before to running HDL
    global_var.__gbefore_scanner_ihs = serviceport.GetScannerIHS(sp).dict_data
    global_var.__gbefore_statistics_enhanced = serviceport.get_enhanced_statistics(sp)


def prepare_teardown():
    return