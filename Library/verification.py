import json
import sys

from Library.service_port import GetScannerIHS
from MetaData.common_data import Message as msg
from Library import service_port
from Library import setting as sett
from MetaData.common_data import SWInfor
from MetaData.common_data import PathFiles
from MetaData.common_data import GlobalVar as gvar
from MetaData.common_data import Product as product
from MetaData.common_data import Event_Log as com_event
from MetaData.common_data import ConfigName
from MetaData.common_data import FileType


def get_obser_ihs():
    # === OBSERVATION IHS
    # get current ihs
    obser_ihs = {}
    current_dict_ihs = GetScannerIHS(gvar.gSERVICE_PORT).dict_data
    obser_i = {'Application_ROM_ID': current_dict_ihs['Application_ROM_ID'],
               'Revision_ECLevel': current_dict_ihs['Revision_ECLevel'],
               'Formatter_Version': current_dict_ihs['Formatter_Version'],
               'VL_Version': current_dict_ihs['VL_Version'],
               'MCF_Version': current_dict_ihs['MCF_Version'],
               'FPGA_Version_ID': current_dict_ihs['FPGA_Version_ID'],
               'Configuration_File_ID': current_dict_ihs['Configuration_ID'],
               'Serial_Number': current_dict_ihs['Serial_Number'],
               'Model_Number': current_dict_ihs['Model_Number'],
               'Main_Board_Serial_Number': current_dict_ihs['Main_Board_Serial_Number'],
               'Current_HW_ID': current_dict_ihs['Current_HW_ID']
               }
    obser_ihs.update(obser_i)
    current_dict_stat = service_port.get_enhanced_statistics()
    obser_ihs.update(current_dict_stat)
    return obser_ihs


def get_expected_ihs(exp_build, file_type):
    Configuration_File_ID = ''
    for ft in FileType.dict_filetype:
        if file_type == FileType.dict_filetype[ft]['name'].upper():
            Configuration_File_ID = FileType.dict_filetype[ft]['name']
            break
    expected_ihs = {}
    # get software infor
    dict_sw_infor = read_sw_infor(exp_build)
    expected_i = {'Application_ROM_ID': dict_sw_infor[SWInfor.Application_ROM_ID],
                  'Revision_ECLevel': dict_sw_infor[SWInfor.Revision_ECLevel],
                  'Formatter_Version': dict_sw_infor[SWInfor.Formatter_Version],
                  'VL_Version': dict_sw_infor[SWInfor.VL_Version],
                  'MCF_Version': dict_sw_infor[SWInfor.MCF_Version],
                  'FPGA_Version_ID': dict_sw_infor[SWInfor.FPGA_Version_ID],
                  'Configuration_File_ID': Configuration_File_ID,
                  'Serial_Number': gvar.gBEFORE_SCANNER_IHS['Serial_Number'],
                  'Model_Number': gvar.gBEFORE_SCANNER_IHS['Model_Number'],
                  'Main_Board_Serial_Number': gvar.gBEFORE_SCANNER_IHS['Main_Board_Serial_Number'],
                  'Current_HW_ID': gvar.gBEFORE_SCANNER_IHS['Current_HW_ID']
                  }
    expected_ihs.update(expected_i)
    expected_s = gvar.gBEFORE_STATISTICS_ENHANCED
    expected_ihs.update(expected_s)
    return expected_ihs


def get_obser_eventlog():
    # sett.print_message_to_console(msg.Noti_Verify_Event)
    # sending sp command to get event log, make sure there are required events
    dict_event_parse = {}
    dict_raw_event = service_port.get_event_log()
    # Event[index number] Ior R (informational or reset event),
    # M[module number of event]:<module name>, F[error code]: <error text>, D: error data, A: additional error data,
    # H: hour error occurred, count: <number of times error occurred>, <CR><LF>
    for evt_index in dict_raw_event:
        tmp_lst = dict_raw_event[evt_index].split(" ")
        Error_Code = ''
        for item in tmp_lst:
            if item.startswith(com_event.s_Error_Code):
                Error_Code = item.split(':')[1]
                break
        tmp_event = {
            'Error_Code': Error_Code,
            'Raw_Event': dict_raw_event[evt_index]
        }
        dict_event_parse[evt_index] = tmp_event
    return dict_event_parse


def get_expected_eventlog():
    # Expected event log is defined in common_data
    list_expected_event = com_event.expected_hdl_event
    if gvar.gPRODUCT_ID == product.Product['Curie']['Product_Name']:
        list_expected_event = list_expected_event + com_event.CE_add_expected_hdl_event
    elif gvar.gPRODUCT_ID == product.Product['Fresco']['Product_Name']:
        list_expected_event = list_expected_event + com_event.FR_add_expected_hdl_event
    elif gvar.gPRODUCT_ID == product.Product['Apollo']['Product_Name']:
        list_expected_event = list_expected_event + com_event.AP_add_expected_hdl_event
    return list_expected_event


def verify_config():
    sett.print_message_to_console(msg.Noti_Verify_Cfg)
    # check all changed cfgs in .text file acording to IFs current, save intto dict file
    # check each command-value in scanner
    return


def verify_combination():
    sett.print_message_to_console(msg.Noti_Verify_ULE)
    # verify .wav file, ule

    sett.print_message_to_console(msg.Noti_Verify_Wav)
    # verify .wav file, ule
    return


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
