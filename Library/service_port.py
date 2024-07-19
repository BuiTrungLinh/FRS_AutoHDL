from MetaData import common_data as comdata
from MetaData.common_data import GlobalVar as gvar
import time


def format_sp_command(cmd, data_type):
    print('Set command: ' + cmd)
    output_str = ""
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
        decimal_array.append(check_digit)

        for d in decimal_array:
            output_str += chr(d)

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
        infor_list = tmp_combine[10:-9].split('\\x03\\x02')
        self.dict_data = {}
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
        self.dict_data['MCF_Version'] = sp.send_command(comdata.SPCommand.sp_read_cfg
                                                        + comdata.SPCommand.cfg_mcf_version).decode("utf-8")
        self.dict_data['Current_HW_ID'] = sp.send_command(comdata.SPCommand.sp_get_hwid).hex()


def get_enhanced_statistics():
    # 0x01<index:2> - read the statistics information for statistics specified by index returning:
    # <index:2><id:2><value:4><null terminated string descriptor if available>
    total_number = int.from_bytes(gvar.gSERVICE_PORT.send_command(comdata.SPCommand.sp_get_statistics_enhanced_number), "big")
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
    # Sending 02A3 to get all in internal
    internal = gvar.gSERVICE_PORT.send_command(comdata.SPCommand.sp_get_internal_file).upper()
    main_string = '0x0D}Number of files: 42{0x0D}1:/ user7.cfg A:W----- 8:34:55 6-24-2024 Size: 5279 /opt/frs/userdata/user7.cfg{0x0D}{0x0A}1:/ user3.cfg A:W----- 8:34:54 6-24-2024 Size: 5290 /opt/frs/userdata/user3.cfg{0x0D}{0x0A}1:/ stats.cfg A:W----- 8:16:15 7-19-2024 Size: 2328 /opt/frs/userdata/stats.cfg{0x0D}{0x0A}1:/ user13.cfg A:W----- 5:28:6 4-14-2024 Size: 5291 /opt/frs/userdata/user13.cfg{0x0D}{0x0A}1:/ factry13.cfg A:W----- 22:35:56 4-12-2024 Size: 5286 /opt/frs/userdata/factry13.cfg{0x0D}{0x0A}1:/ ocr.cfg A:W----- 15:28:18 3-21-2023 Size: 2048 /opt/frs/userdata/ocr.cfg{0x0D}{0x0A}1:/ user5.cfg A:W----- 8:34:51 6-24-2024 Size: 5285 /opt/frs/userdata/user5.cfg{0x0D}{0x0A}1:/ factry2.cfg A:W----- 14:7:21 5-9-2024 Size: 5287 /opt/frs/userdata/factry2.cfg{0x0D}{0x0A}1:/ user8.cfg A:W----- 8:34:53 6-24-2024 Size: 5290 /opt/frs/userdata/user8.cfg{0x0D}{0x0A}1:/ docker_pull.cfg A:W----- 8:25:8 6-6-2024 Size: 2048 /opt/frs/userdata/docker_pull.cfg{0x0D}{0x0A}1:/ lost+found A:W---D- 19:15:33 4-6-2023 Size: 12288 /opt/frs/userdata/lost+found{0x0D}{0x0A}1:/ user6.cfg A:W----- 8:30:54 6-27-2024 Size: 5165 /opt/frs/userdata/user6.cfg{0x0D}{0x0A}1:/ user4.cfg A:W----- 8:34:54 6-24-2024 Size: 5286 /opt/frs/userdata/user4.cfg{0x0D}{0x0A}1:/ docker_init.cfg A:W----- 8:25:8 6-6-2024 Size: 2048 /opt/frs/userdata/docker_init.cfg{0x0D}{0x0A}1:/ extract A:W---D- 14:7:25 5-9-2024 Size: 1024 /opt/frs/userdata/extract{0x0D}{0x0A}1:/ central.cfg A:W----- 3:2:11 5-10-2024 Size: 115 /opt/frs/userdata/central.cfg{0x0D}{0x0A}1:/ factry0.cfg A:W----- 14:7:19 5-9-2024 Size: 5289 /opt/frs/userdata/factry0.cfg{0x0D}{0x0A}1:/ user2.cfg A:W----- 8:34:51 6-24-2024 Size: 5285 /opt/frs/userdata/user2.cfg{0x0D}{0x0A}1:/ out_of_sync_current A:W----- 7:38:0 7-2-2024 Size: 5302 /opt/frs/userdata/out_of_sync_current{0x0D}{0x0A}1:/ factry3.cfg A:W----- 14:7:22 5-9-2024 Size: 5292 /opt/frs/userdata/factry3.cfg{0x0D}{0x0A}1:/ user1.cfg A:W----- 8:34:52 6-24-2024 Size: 5271 /opt/frs/userdata/user1.cfg{0x0D}{0x0A}1:/ factry6.cfg A:W----- 8:34:56 6-24-2024 Size: 5165 /opt/frs/userdata/factry6.cfg{0x0D}{0x0A}1:/ ule.cfg A:W----- 14:7:24 5-9-2024 Size: 16384 /opt/frs/userdata/ule.cfg{0x0D}{0x0A}1:/ factry5.cfg A:W----- 14:7:20 5-9-2024 Size: 5287 /opt/frs/userdata/factry5.cfg{0x0D}{0x0A}1:/ docker_run.cfg A:W----- 8:25:8 6-6-2024 Size: 2048 /opt/frs/userdata/docker_run.cfg{0x0D}{0x0A}1:/ current.cfg A:W----- 7:38:0 7-2-2024 Size: 5302 /opt/frs/userdata/current.cfg{0x0D}{0x0A}1:/ factry7.cfg A:W----- 14:7:24 5-9-2024 Size: 5281 /opt/frs/userdata/factry7.cfg{0x0D}{0x0A}1:/ factry1.cfg A:W----- 14:7:21 5-9-2024 Size: 5273 /opt/frs/userdata/factry1.cfg{0x0D}{0x0A}1:/ POWERUP.WAV A:W----- 3:26:34 10-24-2023 Size: 192048 /opt/frs/userdata/POWERUP.WAV{0x0D}{0x0A}1:/ info.cfg A:W----- 8:11:57 7-2-2024 Size: 200 /opt/frs/userdata/info.cfg{0x0D}{0x0A}1:/ network_conf A:W---D- 2:45:14 6-27-2024 Size: 1024 /opt/frs/userdata/network_conf{0x0D}{0x0A}1:/network_conf 50-frs-eth0-static-mac.link A:W----- 2:45:14 6-27-2024 Size: 62 /opt/frs/userdata/network_conf/50-frs-eth0-static-mac.link{0x0D}{0x0A}1:/network_conf network_paired_devices.xml A:W----- 8:30:53 6-27-2024 Size: 286 /opt/frs/userdata/network_conf/network_paired_devices.xml{0x0D}{0x0A}1:/network_conf scanner_information.xml A:W----- 8:30:54 6-27-2024 Size: 339 /opt/frs/userdata/network_conf/scanner_information.xml{0x0D}{0x0A}1:/ dwm A:W---D- 8:25:11 6-6-2024 Size: 1024 /opt/frs/userdata/dwm{0x0D}{0x0A}1:/dwm active_configuration.json A:W----- 8:25:11 6-6-2024 Size: 14513 /opt/frs/userdata/dwm/active_configuration.json{0x0D}{0x0A}1:/dwm default_configuration.json A:W----- 8:25:11 6-6-2024 Size: 14513 /opt/frs/userdata/dwm/default_configuration.json{0x0D}{0x0A}1:/ factry4.cfg A:W----- 14:7:23 5-9-2024 Size: 5288 /opt/frs/userdata/factry4.cfg{0x0D}{0x0A}1:/ user0.cfg A:W----- 8:34:50 6-24-2024 Size: 5288 /opt/frs/userdata/user0.cfg{0x0D}{0x0A}1:/ directry.cfg A:W----- 8:30:54 6-27-2024 Size: 32 /opt/frs/userdata/directry.cfg{0x0D}{0x0A}1:/ factry8.cfg A:W----- 14:7:22 5-9-2024 Size: 5292 /opt/frs/userdata/factry8.cfg{0x0D}{0x0A}1:/ zero.wav A:W----- 4:38:29 10-23-2023 Size: 224048 /opt/frs/userdata/zero.wav{0x0D}{0x0A}'.upper()
    sub_string = ".WAV"
    start_index = 0
    for i in range(len(main_string)):
        j = main_string.find(sub_string, start_index)
        if j != -1:
            print('========================')
            print(start_index)
            start_index = j + 1
    # ToDo
    return
