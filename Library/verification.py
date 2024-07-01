import json

from Library.service_port import GetScannerIHS
from MetaData.common_data import Message as msg
from Library import service_port
from Library import setting as sett
from MetaData.common_data import SWInfor
from MetaData.common_data import PathFiles


def verify_iden():
    sett.print_message_to_console(msg.Noti_Verify_Iden)
    dict_sw_infor = read_sw_infor()
    obser_ihs = GetScannerIHS(sett.__gServicePort).dict_data
    expected_ihs = {'Application_ROM_ID': dict_sw_infor[SWInfor.Application_ROM_ID],
                    'Revision_ECLevel': dict_sw_infor[SWInfor.Revision_ECLevel],
                    'Configuration_ID': sett.__gbefore_scanner_ihs['Configuration_ID'],
                    'Serial_Number': sett.__gbefore_scanner_ihs['Serial_Number'],
                    'Model_Number': sett.__gbefore_scanner_ihs['Model_Number'],
                    'Main_Board_Serial_Number': sett.__gbefore_scanner_ihs['Main_Board_Serial_Number']}
    # add expected into dict, obser into dict, compare
    # build, eclevel, cfg name,
    obser_dict_stat = service_port.get_enhanced_statistics(sett.__gServicePort)
    expected_dict_stat = {'Power On Time': '',
                          'Custom Data': '',
                          '': ''}
    # Power On Time Before Download, Power On Time After Download
    # Hardware ID Before Download, Hardware ID After Download
    # Custom Data Before Download, Custom Data After Download


def verify_config():
    sett.print_message_to_console(msg.Noti_Verify_Cfg)
    # check all changed cfgs in .text file acording to IFs current, save intto dict file
    # check each command-value in scanner
    return


def verify_eventlog():
    sett.print_message_to_console(msg.Noti_Verify_Event)
    # sending sp command to get event log, make sure there are required events
    return


def verify_combination():
    sett.print_message_to_console(msg.Noti_Verify_ULE)
    # verify .wav file, ule

    sett.print_message_to_console(msg.Noti_Verify_Wav)
    # verify .wav file, ule
    return


def compare_data(expected, obser):
    return False if expected != obser else True


def read_sw_infor():
    with open(PathFiles.path_sw_release) as json_file:
        return json.load(json_file)
