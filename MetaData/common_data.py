class Interface:
    rs232std = 1
    rs232wn = 2
    rs232sc = 3
    usbcom = 4
    usbcomsc = 5
    usboem = 6


class UpdateType:
    upgrade = 1
    downgrade = 2


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

class SPCommand:
    get_identification = "011C"
    save = "0012"
    reset = "001A"
    erase_event = "0024"
    good_beep = "001C"
    get_statistics_log = "0031"
    get_statistics_enhanced_log = "0131"
    get_event_log_entry = "002C"
    get_event_log_entry_enhanced = "012C"
    get_event_log_entry_enhanced_translated = "022C"
    get_hwid = "024008"
    set_interface = "0001"
    # 	00=None, 01=Even, 02=Odd
    set_parity = "001F"
    #   01=9600, 08=115200
    set_baudrate = "001D"
    # 	00=Seven data bits, 01=Eight data bits
    set_databits = "009B"
    #   00=one, 01=two
    set_stopbits = "0022"
    write = "0010"
    read = "0011"


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
    Power_on_time_in_hours = "P"
    Number_of_labels_read = "L"
    Scale_Calibration_attempts = "c"
    Scale_zero_attempts = "z"
    Custom_Data = "C"
    Successful_EAS_deactivations_ = "e"
    Number_of_manual_EAS_deactivations = "E"
    Number_of_EAS_manual_runtime_errors = "Y"
    Total_Resets = "R"
    Error_Resets = "r"
    Vertical_IPE_forced_resets = "V"
    Horizontal_IPE_forced_resets = "H"
    DWM_IPE_forced_resets = "D"
    Vertical_IPE_excessive_resets = "v"
    Horizontal_IPE_excessive_resets = "h"
    DWM_IPE_excessive_resets = "d"
    Scale_sentry_activations = "S"
    POS_initiated_zero_requests = "Z"
    Enforced_zero_events = "X"
