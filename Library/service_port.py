from MetaData import common_data as comdata
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
    if interface == comdata.Interface.rs232std:
        sp_interface = comdata.RS232STD.interface_type
        baudrate = comdata.RS232STD.baudrate
        databits = comdata.RS232STD.databits
        stopbits = comdata.RS232STD.stopbits
        parity = comdata.RS232STD.parity
    elif interface == comdata.Interface.rs232wn:
        sp_interface = comdata.RS232WN.interface_type
        baudrate = comdata.RS232WN.baudrate
        databits = comdata.RS232WN.databits
        stopbits = comdata.RS232WN.stopbits
        parity = comdata.RS232WN.parity
    elif interface == comdata.Interface.rs232sc:
        sp_interface = comdata.RS232SC.interface_type
        baudrate = comdata.RS232SC.baudrate
        databits = comdata.RS232SC.databits
        stopbits = comdata.RS232SC.stopbits
        parity = comdata.RS232SC.parity
    elif interface == comdata.Interface.usbcom:
        sp_interface = comdata.USBCOM.interface_type
    elif interface == comdata.Interface.usbcomsc:
        sp_interface = comdata.USBCOMSC.interface_type
    elif interface == comdata.Interface.usboem:
        sp_interface = comdata.USBOEM.interface_type
    sp.send_command(comdata.SPCommand.write + comdata.SPCommand.set_interface + sp_interface)
    sp.send_command(comdata.SPCommand.write + comdata.SPCommand.set_baudrate + baudrate)
    sp.send_command(comdata.SPCommand.write + comdata.SPCommand.set_databits + databits)
    sp.send_command(comdata.SPCommand.write + comdata.SPCommand.set_stopbits + stopbits)
    sp.send_command(comdata.SPCommand.write + comdata.SPCommand.set_parity + parity)
    sp.send_command(comdata.SPCommand.save)
    sp.send_command(comdata.SPCommand.reset)
    time.sleep(5)


def get_scanner_current_information(data, info):
    iden_str = data
    iden_str = str(
        r'\x02ADR9401648\x03\x02R0024\x03\x02CDEFAULT\x03\x02SCE_DEV01_900i\x03\x02MNONE\x03\x02mNONE\x03\x02I05\x03\x02B0000\x03\x02t3.10\x03\x02V2.3.7.16\x03\x02F01.05\x03\x04')
    iden_list = iden_str.replace('\\x03', '').split('\\x02')
    for data in iden_list:
        if data.startswith(info):
            return data[1:]
