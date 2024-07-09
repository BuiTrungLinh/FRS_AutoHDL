class GlobalVar:
    gBEFORE_SCANNER_IHS = None
    gBEFORE_STATISTICS_ENHANCED = None
    gPRODUCT_ID = None
    gSERVICE_PORT = None
    gHOST_PORT = None
    gCURRENT_INTERFACE = None


class Interface:
    rs232std_index = 1
    rs232wn_index = 2
    rs232sc_index = 3
    usbcom_index = 4
    usbcomsc_index = 5
    usboem_index = 6
    dict_interface = {
        1: {
            'name': 'RS232STD',
            "full_name": "RS232-STD"
        },
        2: {
            'name': 'RS232WN',
            "full_name": "RS232-WN"
        },
        3: {
            'name': 'RS232SC',
            "full_name": "RS232-SC"
        },
        4: {
            'name': 'USBCOM',
            "full_name": "USB-COM"
        },
        5: {
            'name': 'USBCOMSC',
            "full_name": "USB-COM-SC"
        },
        6: {
            'name': 'USBOEM',
            "full_name": "USB-OEM"
        },
    }


class UpdateType:
    upgrade_index = 1
    downgrade_index = 2
    curtocur_index = 3
    upgrade_name = 'Upgrade'
    downgrade_name = 'Downgrade'
    curtocur_name = 'Cur-To-Cur'
    dict_updatetype = {
        1: {
            "name": "Upgrade"
        },
        2: {
            "name": "Downgrade"
        },
        3: {
            "name": "Cur-To-Cur"
        }
    }


class FileType:
    apponly_index = 1
    appcfg_index = 2
    cfgonly_index = 3
    othercfg_index = 4
    dict_filetype = {
        1: {
            'name': 'AppOnly',
            "full_name": "App-Only"
        },
        2: {
            'name': 'AppCfg',
            "full_name": "App-Cfg"
        },
        3: {
            'name': 'CfgOnly',
            "full_name": "Cfg-Only"
        },
        4: {
            'name': 'OtherCfg',
            "full_name": "Other-Cfg"
        },
    }


class RS232STD:
    # 115200 none 8 1
    interface_type = '05'
    baudrate = '08'
    parity = '00'
    databits = '01'
    stopbits = '00'


class RS232WN:
    # 115200 odd 8 1
    interface_type = '12'
    baudrate = '08'
    parity = '02'
    databits = '01'
    stopbits = '00'


class RS232SC:
    # 115200 odd 7 1
    interface_type = '20'
    baudrate = '08'
    parity = '02'
    databits = '00'
    stopbits = '00'


class USBCOM:
    interface_type = '47'


class USBCOMSC:
    interface_type = '1E'


class USBOEM:
    interface_type = '45'


class Dlrmus:
    # i_ = interface, p_ = param, v_ is value
    i_RS232_STD = "RS232Scanner"
    i_RS232_WN = "RS232Scanner"
    i_RS232_SC = "SCRS232Scanner"
    i_USBCOM = "RS232Scanner"
    i_USBCOM_SC = "SC-COM"
    i_USBOEM = "USBScanner"
    i_ServicePort = "ServicePort"
    p_select_interface = "-a"
    p_select_path_file = "-f"
    p_custom_log_filename = "-l"
    p_select_comport = "-c"
    p_start_baudrate = "-b"
    v_baudrate_115200 = '115200'


class PathFiles:
    # path_file_dlrmus = r'..\Tools\DLRMUs\dlrmus.exe'
    path_file_dlrmus = r'D:\1.DevelopmentTool\PycharmProjects\FRS_AutoHDL\Tools\DLRMUs\dlrmus.exe'
    path_sw_release = r'MetaData/software_release.json'
    path_sw_infor = r'../MetaData/software_information.json'


class SPCommand:
    # SP COMMAND =======
    sp_aaa = '011B'
    sp_get_identification = "011C"
    sp_save = "0012"
    sp_reset = "001A"
    sp_erase_event = "0024"
    sp_good_beep = "001C"
    sp_get_statistics_enhanced_number = "013100"
    sp_get_statistics_enhanced_index = "013101"
    sp_get_event_log_entry_enhanced_translated = "022C"
    sp_get_hwid = "024008"
    sp_erase_custom_file = "1520"
    sp_write_cfg = "0010"
    sp_read_cfg = "0011"

    # CONFIG TAG =======
    cfg_config_file_id = "0060"
    cfg_erase_ule = "7FF800000000"
    cfg_erase_customdata = "7FF700000000"
    cfg_ule = "7FF8"
    cfg_customdata = "7FF7"
    cfg_mcf_version = '0009'
    cfg_interface = "0001"
    # 	00=None, 01=Even, 02=Odd
    cfg_parity = "001F"
    #   01=9600, 08=115200
    cfg_baudrate = "001D"
    # 	00=Seven data bits, 01=Eight data bits
    cfg_databits = "009B"
    #   00=one, 01=two
    cfg_stopbits = "0022"

    # VALUE DEFAULT
    val_config_file_id = "2A2A4E4F54205345542A"


class SWInfor:
    Application_ROM_ID = 'App'
    Revision_ECLevel = 'EC'
    Formatter_Version = 'Formatter'
    VL_Version = 'EVL'
    MCF_Version = 'MCF'
    FPGA_Version_ID = 'XBurst0'


class Identification:
    Application_ROM_ID = "A"
    Revision_ECLevel = "R"
    Configuration_ID = "C"
    Internal_Scale = "W"
    Remote_Display_Version = "D"
    Serial_Number = "S"
    Model_Number = "M"
    Main_Board_Serial_Number = "m"
    Scanner_Interface_Number = "I"
    VL_Version = "V"
    Bootloader_ROM_ID = "B"
    FPGA_Version_ID = "F"
    IPE_Application_ROM_ID = "P"
    USB_Loader_Version_ID = "l"
    SDRAM_Configuration_File_ID = "Q"
    EAS_Version = "E"
    Interface_Application_ROM_ID = "U"
    Interface_Bootloader_ROM_ID = "u"


class Health:
    Internal_Scale_Status = "s"
    Remote_Display_Status = "d"
    EAS_Status = "e"
    USB_Handheld_Connected = "H"
    USB_Serial_Dongle_Connected = "D"
    IPE_0_Vertical = "0"
    IPE_1_Horizontal = "1"
    IPE_2_DWM = "2"
    Scale_Sentry = "S"


class Statistics:
    # s: short
    s_Power_on_time_in_hours = "P"
    s_Number_of_labels_read = "L"
    s_Scale_Calibration_attempts = "c"
    s_Scale_zero_attempts = "z"
    s_Custom_Data = "C"
    s_Successful_EAS_deactivations_ = "e"
    s_Number_of_manual_EAS_deactivations = "E"
    s_Number_of_EAS_manual_runtime_errors = "Y"
    s_Total_Resets = "R"
    s_Error_Resets = "r"
    s_Vertical_IPE_forced_resets = "V"
    s_Horizontal_IPE_forced_resets = "H"
    s_DWM_IPE_forced_resets = "D"
    s_Vertical_IPE_excessive_resets = "v"
    s_Horizontal_IPE_excessive_resets = "h"
    s_DWM_IPE_excessive_resets = "d"
    s_Scale_sentry_activations = "S"
    s_POS_initiated_zero_requests = "Z"
    s_Enforced_zero_events = "X"

    # l: long
    l_Power_on_time_in_hours = "Power on time in hours"
    l_Number_of_labels_read = "Number_of_labels_read"
    l_Scale_Calibration_attempts = "Scale_Calibration_attempts"
    l_Scale_zero_attempts = "Scale_zero_attempts"
    l_Custom_Data = "Custom_Data"
    l_Successful_EAS_deactivations_ = "Successful_EAS_deactivations_"
    l_Number_of_manual_EAS_deactivations = "Number_of_manual_EAS_deactivations"
    l_Number_of_EAS_manual_runtime_errors = "Number_of_EAS_manual_runtime_errors"
    l_Total_Resets = "Total_Resets"
    l_Error_Resets = "Error_Resets"
    l_Vertical_IPE_forced_resets = "Vertical_IPE_forced_resets"
    l_Horizontal_IPE_forced_resets = "Horizontal_IPE_forced_resets"
    l_DWM_IPE_forced_resets = "DWM_IPE_forced_resets"
    l_Vertical_IPE_excessive_resets = "Vertical_IPE_excessive_resets"
    l_Horizontal_IPE_excessive_resets = "Horizontal_IPE_excessive_resets"
    l_DWM_IPE_excessive_resets = "d"
    l_Scale_sentry_activations = "S"
    l_POS_initiated_zero_requests = "Z"
    l_Enforced_zero_events = "X"


class Message:
    # Error message
    Error_Title = 'Error-Message'
    Error_No_Selected_IFs = 'Please select at least 1 interface!'
    Error_No_Selected_FileType = 'Please select at least 1 file-type!'
    Error_No_Selected_UpdateType = 'Please select at least 1 update-type!'
    Error_No_Selected_Release = 'Please select at least 1 release!'
    Error_No_Located_Path = 'Please enter the path containing release!'
    Error_No_Data_In_SW_Information_Js = 'No found build {} in Software Information Json file!'
    # Notification
    Noti_Verify_Cfg = '----------------Start Verifying Config Valueset----------------'
    Noti_Verify_Iden = '----------------Start Verifying Identification----------------'
    Noti_Verify_Event = '----------------Start Verifying Event-Log----------------'
    Noti_Verify_ULE = '----------------Start Verifying ULE----------------'
    Noti_Verify_Wav = '----------------Start Verifying WAV-file----------------'
    # Dlrmus
    Succ_Dlrmus_Update_SP = 'Updated {} build to the scanner by ServicePort successfully'
    Succ_Dlrmus_Update_Host = 'Updated {} build to the scanner by Host {} successfully'
    Error_Dlrmus_Update_SP = 'ERR: Failed update of {} build for scanner through ServicePort'
    Error_Dlrmus_Update_Host = 'ERR: Failed update of {} build for scanner through Host {}'


class Product:
    Product = {
        'Curie': {
            'Product_FullName': 'Curie',
            'Product_Name': '900i',
            'Product_ID': '1605',
            'Interface': {
                1: {
                    "name": "RS232-STD",
                    "index": "1"
                },
                2: {
                    "name": "RS232-WN",
                    "index": "2"
                },
                3: {
                    "name": "USB-COM",
                    "index": "3"
                },
                4: {
                    "name": "USB-OEM",
                    "index": "4"
                },
                5: {
                    "name": "USB-KBD",
                    "index": "5"
                }
            }
        },
        'Apollo': {},
        'Fresco': {},
    }

    Apollo_index = 0
    Curie_index = 1
    Fresco_index = 2
    Apollo_name = 'Apollo'
    Curie_name = 'Curie'
    Fresco_name = 'Fresco'
    Apollo_interface = {
        1: {
            "name": "RS232-STD",
            "index": "1"
        },
        2: {
            "name": "RS232-WN",
            "index": "2"
        },
        3: {
            "name": "RS232-SC",
            "index": "3"
        },
        4: {
            "name": "USB-COM",
            "index": "4"
        },
        5: {
            "name": "USB-COM-SC",
            "index": "5"
        },
        6: {
            "name": "USB-OEM",
            "index": "6"
        }
    }
    Curie_interface = {
        1: {
            "name": "RS232-STD",
            "index": "1"
        },
        2: {
            "name": "RS232-WN",
            "index": "2"
        },
        3: {
            "name": "USB-COM",
            "index": "3"
        },
        4: {
            "name": "USB-OEM",
            "index": "4"
        },
        5: {
            "name": "USB-KBD",
            "index": "5"
        }
    }
    Fresco_interface = {
        1: {
            "name": "RS232-STD",
            "index": "1"
        },
        2: {
            "name": "RS232-WN",
            "index": "2"
        },
        3: {
            "name": "RS232-SC",
            "index": "3"
        },
        4: {
            "name": "USB-COM",
            "index": "4"
        },
        5: {
            "name": "USB-COM-SC",
            "index": "5"
        },
        6: {
            "name": "USB-OEM",
            "index": "6"
        }
    }
