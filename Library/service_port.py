from MetaData import common_data as comdata
from MetaData.common_data import GlobalVar as gvar
import time


def format_sp_command(cmd, data_type):
    print('Set command: ' + cmd)
    output_str = b''
    if (len(cmd) % 2) == 0:
        command_len = int(len(cmd) / 2)

        hex_len = "{:08x}".format(command_len + 1)
        output_array = [data_type]
        for x in range(4):
            output_array.append(hex_len[(x * 2): (x * 2 + 2)])

        for x in range(command_len):
            output_array.append(cmd[:2])
            cmd = cmd[2:]

        decimal_array = []
        sumint = 0
        for x in range(len(output_array)):
            an_integer = int(output_array[x], 16)
            decimal_array.append(an_integer)
            sumint += an_integer

        check_digit = 256 - (sumint % 256)
        if hex(check_digit)[-2:] == '00': check_digit = 00

        decimal_array.append(check_digit)

        for d in decimal_array:
            # output_str += chr(d)
            output_str += d.to_bytes(1, 'big')

        return output_str
    else:
        print("Invalid command")

    return output_str


def set_interface(sp, interface):
    baudrate = ''
    databits = ''
    stopbits = ''
    parity = ''
    sp_interface = ''
    if interface == comdata.Interface.rs232std_index:
        sp_interface = comdata.RS232STD.interface_type
        baudrate = comdata.RS232STD.baudrate
        databits = comdata.RS232STD.databits
        stopbits = comdata.RS232STD.stopbits
        parity = comdata.RS232STD.parity
    elif interface == comdata.Interface.rs232wn_index:
        sp_interface = comdata.RS232WN.interface_type
        baudrate = comdata.RS232WN.baudrate
        databits = comdata.RS232WN.databits
        stopbits = comdata.RS232WN.stopbits
        parity = comdata.RS232WN.parity
    elif interface == comdata.Interface.rs232sc_index:
        sp_interface = comdata.RS232SC.interface_type
        baudrate = comdata.RS232SC.baudrate
        databits = comdata.RS232SC.databits
        stopbits = comdata.RS232SC.stopbits
        parity = comdata.RS232SC.parity
    elif interface == comdata.Interface.usbcom_index:
        sp_interface = comdata.USBCOM.interface_type
    elif interface == comdata.Interface.usbcomsc_index:
        sp_interface = comdata.USBCOMSC.interface_type
    elif interface == comdata.Interface.usboem_index:
        sp_interface = comdata.USBOEM.interface_type
    sp.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_interface + sp_interface)
    sp.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_baudrate + baudrate)
    sp.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_databits + databits)
    sp.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_stopbits + stopbits)
    sp.send_command(comdata.SPCommand.sp_write_cfg + comdata.SPCommand.cfg_parity + parity)
    sp.send_command(comdata.SPCommand.sp_save)
    sp.send_command(comdata.SPCommand.sp_reset)
    time.sleep(10)


class GetScannerIHS:
    def __init__(self, sp):
        idenStr = str(sp.send_command(comdata.SPCommand.sp_get_identification))
        healthStr = ''
        statisticsStr = ''
        tmp_combine = idenStr + healthStr + statisticsStr
        infor_list = tmp_combine[tmp_combine.find('\\x02A') + 4:tmp_combine.rfind('\\x03\\x04')].split('\\x03\\x02')
        self.dict_data = {}
        try:
            for data in infor_list:
                match data[0]:
                    case comdata.Identification.Application_ROM_ID:
                        self.Application_ROM_ID = data[1:]
                        self.dict_data['Application_ROM_ID'] = data[1:]
                    case comdata.Identification.Revision_ECLevel:
                        self.Revision_ECLevel = data[1:]
                        self.dict_data['Revision_ECLevel'] = data[1:]
                    case comdata.Identification.Configuration_ID:
                        self.Configuration_ID = data[1:]
                        self.dict_data['Configuration_ID'] = data[1:]
                    case comdata.Identification.Internal_Scale:
                        self.Internal_Scale = data[1:]
                        self.dict_data['Internal_Scale'] = data[1:]
                    case comdata.Identification.Remote_Display_Version:
                        self.Remote_Display_Version = data[1:]
                        self.dict_data['Remote_Display_Version'] = data[1:]
                    case comdata.Identification.Serial_Number:
                        self.Serial_Number = data[1:]
                        self.dict_data['Serial_Number'] = data[1:]
                    case comdata.Identification.Model_Number:
                        self.Model_Number = data[1:]
                        self.dict_data['Model_Number'] = data[1:]
                    case comdata.Identification.Main_Board_Serial_Number:
                        self.Main_Board_Serial_Number = data[1:]
                        self.dict_data['Main_Board_Serial_Number'] = data[1:]
                    case comdata.Identification.Scanner_Interface_Number:
                        self.Scanner_Interface_Number = data[1:]
                        self.dict_data['Scanner_Interface_Number'] = data[1:]
                    case comdata.Identification.VL_Version:
                        self.VL_Version = data[1:]
                        self.dict_data['VL_Version'] = data[1:]
                    case comdata.Identification.Bootloader_ROM_ID:
                        self.Bootloader_ROM_ID = data[1:]
                        self.dict_data['Bootloader_ROM_ID'] = data[1:]
                    case comdata.Identification.FPGA_Version_ID:
                        self.FPGA_Version_ID = data[1:]
                        self.dict_data['FPGA_Version_ID'] = data[1:]
                    case comdata.Identification.IPE_Application_ROM_ID:
                        self.IPE_Application_ROM_ID = data[1:]
                        self.dict_data['IPE_Application_ROM_ID'] = data[1:]
                    case comdata.Identification.USB_Loader_Version_ID:
                        self.USB_Loader_Version_ID = data[1:]
                        self.dict_data['USB_Loader_Version_ID'] = data[1:]
                    case comdata.Identification.SDRAM_Configuration_File_ID:
                        self.SDRAM_Configuration_File_ID = data[1:]
                        self.dict_data['SDRAM_Configuration_File_ID'] = data[1:]
                    case comdata.Identification.EAS_Version:
                        self.EAS_Version = data[1:]
                        self.dict_data['EAS_Version'] = data[1:]
                    case comdata.Identification.Interface_Application_ROM_ID:
                        self.Interface_Application_ROM_ID = data[1:]
                        self.dict_data['Interface_Application_ROM_ID'] = data[1:]
                    case comdata.Identification.Interface_Bootloader_ROM_ID:
                        self.Interface_Bootloader_ROM_ID = data[1:]
                        self.dict_data['Interface_Bootloader_ROM_ID'] = data[1:]
                    case comdata.Identification.Formatter_Version:
                        self.Formatter_Version = data[1:]
                        self.dict_data['Formatter_Version'] = data[1:]
        except:
            self.dict_data = {}
        self.dict_data['MCF_Version'] = sp.send_command(comdata.SPCommand.sp_read_cfg
                                                        + comdata.SPCommand.cfg_mcf_version).decode("utf-8")
        self.dict_data['Current_HW_ID'] = sp.send_command(comdata.SPCommand.sp_get_hwid).hex()


def get_enhanced_statistics():
    # 0x01<index:2> - read the statistics information for statistics specified by index returning:
    # <index:2><id:2><value:4><null terminated string descriptor if available>
    total_number = int.from_bytes(gvar.gSERVICE_PORT.send_command(comdata.SPCommand.sp_get_statistics_enhanced_number),
                                  "big")
    dict_stat = {}
    for index in range(total_number - 1):
        str_index = str(hex(index).split('x')[-1])
        value = ('0' * (4 - len(str_index))) + str_index
        stat = gvar.gSERVICE_PORT.send_command(comdata.SPCommand.sp_get_statistics_enhanced_index + value)
        if 'Linux Application' in stat[8:-1].decode("utf-8"):
            continue
        dict_stat[index] = {'id': int.from_bytes(stat[2:4], "big"), 'value': int.from_bytes(stat[4:8], "big"),
                            'des': stat[8:-1].decode("utf-8")}
    return dict_stat


def get_event_log():
    # 022C: 	Get Event Log Entry N Enhanced Translated
    value = 0
    dict_event = {}
    while True:
        event_raw = gvar.gSERVICE_PORT.send_command(comdata.SPCommand.sp_get_event_log + f'{value:02}').decode("utf-8")
        if event_raw == "\x00":
            break
        dict_event[value] = event_raw
        value = value + 1
    return dict_event


def erase_sound_file():
    # Sending 02A3 to get all files in internal
    internal = str(gvar.gSERVICE_PORT.send_command(comdata.SPCommand.sp_get_internal_file)).upper()
    sub_string = ".WAV"
    # if not found any .wav file, exit
    if internal.find(sub_string) == -1:
        return
    start_index = 0
    # delete each .wav file in internal
    for i in range(len(internal)):
        j = internal.find(sub_string, start_index)
        if j != -1:
            sub_tmp = internal[start_index:j + 4]
            sub_sub_tmp = sub_tmp[sub_tmp.rfind('/'):].strip()
            wav_file = sub_sub_tmp[1:].strip()
            # clear all wav file with upper and lower
            gvar.gSERVICE_PORT.send_command(comdata.SPCommand.sp_erase_find_internal + '"' + wav_file.upper() + '"')
            gvar.gSERVICE_PORT.send_command(comdata.SPCommand.sp_erase_find_internal + '"' + wav_file.lower() + '"')
            start_index = j + 4
    # recheck make sure wav file is deleted
    erase_sound_file()
