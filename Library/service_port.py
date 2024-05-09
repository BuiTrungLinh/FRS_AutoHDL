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
    time.sleep(10)


def get_scanner_current_information(sp, info):
    idenStr = str(sp.send_command(comdata.SPCommand.get_identification))
    healthStr = ''
    statisticsStr = ''
    tmp_combine = idenStr + healthStr + statisticsStr
    infor_list = tmp_combine.replace('\\x03', '').split('\\x02')
    for data in infor_list:
        if data.startswith(info):
            return data[1:]
