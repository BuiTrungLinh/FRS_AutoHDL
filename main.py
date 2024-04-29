import sys
import time
from Library import dlrmus
import os.path
from Library import connection as con

from MetaData import common_data as comdata

sp = None


def get_scanner_current_information(data, info):
    iden_str = data
    iden_str = str(
        r'\x02ADR9401648\x03\x02R0024\x03\x02CDEFAULT\x03\x02SCE_DEV01_900i\x03\x02MNONE\x03\x02mNONE\x03\x02I05\x03\x02B0000\x03\x02t3.10\x03\x02V2.3.7.16\x03\x02F01.05\x03\x04')
    iden_list = iden_str.replace('\\x03', '').split('\\x02')
    for data in iden_list:
        if data.startswith(info):
            return data[1:]


def set_interface(interface):
    baudrate = ''
    databits = ''
    stopbits = ''
    parity = ''
    if interface == comdata.Interface.rs232std:
        interface = comdata.RS232STD.interface_type
        baudrate = comdata.RS232STD.baudrate
        databits = comdata.RS232STD.databits
        stopbits = comdata.RS232STD.stopbits
        parity = comdata.RS232STD.parity
    elif interface == comdata.Interface.rs232wn:
        interface = comdata.RS232WN.interface_type
        baudrate = comdata.RS232WN.baudrate
        databits = comdata.RS232WN.databits
        stopbits = comdata.RS232WN.stopbits
        parity = comdata.RS232WN.parity
    elif interface == comdata.Interface.rs232sc:
        interface = comdata.RS232SC.interface_type
        baudrate = comdata.RS232SC.baudrate
        databits = comdata.RS232SC.databits
        stopbits = comdata.RS232SC.stopbits
        parity = comdata.RS232SC.parity
    elif interface == comdata.Interface.usbcom:
        interface = comdata.USBCOM.interface_type
    elif interface == comdata.Interface.usbcomsc:
        interface = comdata.USBCOMSC.interface_type
    elif interface == comdata.Interface.usboem:
        interface = comdata.USBOEM.interface_type
    sp.send_command('0010' + comdata.SPCommand.set_interface + interface)
    sp.send_command('0010' + comdata.SPCommand.set_baudrate + baudrate)
    sp.send_command('0010' + comdata.SPCommand.set_databits + databits)
    sp.send_command('0010' + comdata.SPCommand.set_stopbits + stopbits)
    sp.send_command('0010' + comdata.SPCommand.set_parity + parity)
    sp.send_command(comdata.SPCommand.save)
    sp.send_command(comdata.SPCommand.reset)
    time.sleep(5)


if __name__ == '__main__':
    sp_comport = con.get_service_ports_list()
    if not sp_comport["isFoundSP"]:
        print('Warning: Could not find any Datalogic\'s "ServicePort"')
        sys.exit()

    print('Interface: {}, PortName: {}'.format(sp_comport["current_interface"], sp_comport["current_sp_name"]))
    sp = con.Connection(port=sp_comport["current_sp_name"])
    sp.open_port()
    # issue - recheck again, cannot catch data
    # idenStr = str(sp.send_command('011C'))
    current_build = get_scanner_current_information('', comdata.Identification.Application_ROM_ID)
    # current_hwid = sp.send_command(comdata.SPCommand.get_hwid)
    current_hwid = '900'
    # load GUI menu for 900 product
    # Path release build
    path_file_root = r'D:\tmp\CE_Release'
    # dict selected release build
    dict_selected_release = {
        #   1= rs232std
        1: {
            "AppOnly": {
                1: ['DR9401638', 'DR9401643', 'DR9401646'],
                2: ['DR9401638', 'DR9401643', 'DR9401646'],
            },
            "AppCfg": {
                1: ['DR9401638', 'DR9401643', 'DR9401646'],
            }
        },
        #   2 rs232wn
        6: {
            "AppOnly": {
                1: ['DR9401638', 'DR9401643', 'DR9401646'],
            },
            "AppCfg": {
                1: ['DR9401638', 'DR9401643', 'DR9401646'],
                2: ['DR9401638', 'DR9401643', 'DR9401646'],
            }
        },
        "LAST_BUILD": "DR9401648"
    }

    for interface in dict_selected_release:
        file_format = ''
        if interface == 'LAST_BUILD':
            continue
        # setting baudrate, databits, stopbits, parity for scanner
        # set_interface(interface)
        file_format = '.DAT' if interface == comdata.Interface.usboem else '.S37'
        # call dlrmus
        for file_type in dict_selected_release[interface]:
            for update_type in dict_selected_release[interface][file_type]:
                for build in dict_selected_release[interface][file_type][update_type]:
                    path_file = path_file_root + '\\' + build + '\\' + file_type + '_' + build + file_format
                    path_file_latest = path_file_root + '\\' + dict_selected_release[
                        'LAST_BUILD'] + '\\' + file_type + '_' + dict_selected_release['LAST_BUILD'] + file_format
                    build_from = ''
                    build_to = ''
                    if update_type == comdata.UpdateType.upgrade:
                        build_from = path_file
                        build_to = path_file_latest
                    elif update_type == comdata.UpdateType.downgrade:
                        build_from = path_file_latest
                        build_to = path_file
                    else:
                        build_from = path_file_latest
                        build_to = path_file_latest

                    if os.path.isfile(build_from) and os.path.isfile(build_to):
                        print('=================================')
                        print('Start testcase AAA')
                        dlr = dlrmus.Dlrmus(from_build=build_from, to_build=build_to, interface=interface)
                        dlr.execute()
                        # class method verify data
                        print('End testcase AAA')
                        print('=================================')
                    else:
                        print('Cannot run testcase xxx because did not found file: ' + build_from
                              + 'or file: ' + build_to)
    sp.close_port()
