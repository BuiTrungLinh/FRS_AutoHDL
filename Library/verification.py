from Library import global_var
from Library.setting import print_message_to_console
from Library.service_port import GetScannerIHS
from MetaData.common_data import Message as msg
from MetaData.common_data import Identification as iden
from MetaData.common_data import SPCommand as sp_cmd


class Verification:
    def __init__(self, sp=None):
        self.sp = sp

    def verify_iden(self):
        print_message_to_console(msg.Noti_Verify_Iden)
        obser = GetScannerIHS(self.sp).dict_data
        expected = {'Application_ROM_ID': '',
                    'Revision_ECLevel': '',
                    'Configuration_ID': '',
                    'Internal_Scale': '',
                    'Remote_Display_Version': '',
                    'Serial_Number': '',
                    'Model_Number': '',
                     'Main_Board_Serial_Number': ''}
        # add expected into dict, obser into dict, compare
        # build, eclevel, cfg name,

        # Power On Time Before Download, Power On Time After Download
        # Serial Number Before Download, Serial Number After Download
        # Board Serial Number Before Download, Board Serial Number After Download
        # Model Number Before Download, Model Number After Download
        # Feature Key Before Download, Feature Key After Download
        # Hardware ID Before Download, Hardware ID After Download
        # Custom Data Before Download, Custom Data After Download
        return

    def verify_config(self):
        print_message_to_console(msg.Noti_Verify_Cfg)
        # check all changed cfgs in .text file acording to IFs current, save intto dict file
        # check each command-value in scanner
        return

    def verify_eventlog(self):
        print_message_to_console(msg.Noti_Verify_Event)
        # sending sp command to get event log, make sure there are required events
        return

    def verify_combination(self):
        print_message_to_console(msg.Noti_Verify_ULE)
        # verify .wav file, ule

        print_message_to_console(msg.Noti_Verify_Wav)
        # verify .wav file, ule
        return


def compare_data(expected, obser):
    return False if expected != obser else True