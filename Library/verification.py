import json
import sys

from Library.service_port import GetScannerIHS
from MetaData.common_data import Message as msg
from Library import service_port
from Library import setting as sett
from MetaData.common_data import SWInfor
from MetaData.common_data import PathFiles
from MetaData.common_data import GlobalVar as gvar
from MetaData.common_data import SPCommand as sp_cmd
from MetaData.common_data import Product as product


def verify_iden():
    sett.print_message_to_console(msg.Noti_Verify_Iden)
    # === OBSERVATION IHS
    # get current ihs
    current_dict_ihs = GetScannerIHS(gvar.gSERVICE_PORT).dict_data
    obser_ihs = {'Application_ROM_ID': current_dict_ihs['Application_ROM_ID'],
                 'Revision_ECLevel': current_dict_ihs['Revision_ECLevel'],
                 'Formatter_Version': current_dict_ihs['Application_ROM_ID'],
                 'VL_Version': current_dict_ihs['VL_Version'],
                 'MCF_Version': current_dict_ihs['MCF_Version'],
                 'FPGA_Version_ID': current_dict_ihs['FPGA_Version_ID'],
                 'Configuration_File_ID': current_dict_ihs['Configuration_ID'],
                 'Serial_Number': current_dict_ihs['Serial_Number'],
                 'Model_Number': current_dict_ihs['Model_Number'],
                 'Main_Board_Serial_Number': current_dict_ihs['Main_Board_Serial_Number'],
                 'Current_HW_ID': current_dict_ihs['Current_HW_ID']
                 }
    # === EXPECTED IHS
    # get software infor
    dict_sw_infor = read_sw_infor(current_dict_ihs['Application_ROM_ID'])
    expected_ihs = {'Application_ROM_ID': dict_sw_infor[SWInfor.Application_ROM_ID],
                    'Revision_ECLevel': dict_sw_infor[SWInfor.Revision_ECLevel],
                    'Formatter_Version': dict_sw_infor[SWInfor.Formatter_Version],
                    'VL_Version': dict_sw_infor[SWInfor.VL_Version],
                    'MCF_Version': dict_sw_infor[SWInfor.MCF_Version],
                    'FPGA_Version_ID': dict_sw_infor[SWInfor.FPGA_Version_ID],
                    'Configuration_File_ID': '',
                    'Serial_Number': gvar.gBEFORE_SCANNER_IHS['Serial_Number'],
                    'Model_Number': gvar.gBEFORE_SCANNER_IHS['Model_Number'],
                    'Main_Board_Serial_Number': gvar.gBEFORE_SCANNER_IHS['Main_Board_Serial_Number'],
                    'Current_HW_ID': gvar.gBEFORE_SCANNER_IHS['Current_HW_ID']
                    }

    # === OBSERVATION STATISTICS
    # get current statistics
    current_dict_stat = service_port.get_enhanced_statistics(gvar.gSERVICE_PORT)
    expected_dict_stat = {'Power On Time': '',
                          'Custom Data': '',
                          '': ''}
    # Power On Time Before Download, Power On Time After Download
    # Custom Data Before Download, Custom Data After Download
    # === EXPECTED STATISTICS


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


def read_sw_infor(build):
    Product_FullName = ''
    for p in product.Product:
        if gvar.gPRODUCT_ID == product.Product[p]['Product_Name']:
            Product_FullName = product.Product[p]['Product_FullName']
            break
    with open(PathFiles.path_sw_infor) as json_file:
        tmp_data = json.load(json_file)

    try:
        return tmp_data[Product_FullName][build]
    except:
        # should be print in log file
        # Todo
        sett.print_message_to_console(msg.Error_No_Data_In_SW_Information_Js.format(build))
        sys.exit()
