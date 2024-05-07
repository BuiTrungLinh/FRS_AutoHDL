import sys
import time
from Library import dlrmus
import os.path
from Library import connection as con
from Library.service_port import get_scanner_current_information
from MetaData import common_data as comdata

sp = None

if __name__ == '__main__':
    connect_port = con.connect_port()
    sp = connect_port[0]
    dictPort = connect_port[1]
    # issue - recheck again, cannot catch data
    idenStr = str(sp.send_command('011C'))
    current_build = get_scanner_current_information(idenStr, comdata.Identification.Application_ROM_ID)
    # current_hwid = sp.send_command(comdata.SPCommand.get_hwid)
    current_hwid = '900'
    # load GUI menu for 900 product
    # Path release build
    path_file_root = r'D:\tmp\CE_Release'
    # dict selected release build
    dict_selected_release = {
        #   4= usbcom
        4: {
            "AppOnly": {
                1: ['DR9401638', 'DR9401643', 'DR9401646'],
                2: ['DR9401638', 'DR9401643', 'DR9401646'],
            },
            "AppCfg": {
                1: ['DR9401638', 'DR9401643', 'DR9401646'],
            }
        },
        #   6 = usboem
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
        if interface == 'LAST_BUILD':
            continue
        file_format = '.DAT' if interface == comdata.Interface.usboem else '.S37'
        # call dlrmus
        for file_type in dict_selected_release[interface]:
            for update_type in dict_selected_release[interface][file_type]:
                for build in dict_selected_release[interface][file_type][update_type]:
                    path_file = path_file_root + '\\' + build + '\\' + file_type + '_' + build
                    path_file_latest = path_file_root + '\\' + dict_selected_release[
                        'LAST_BUILD'] + '\\' + file_type + '_' + dict_selected_release['LAST_BUILD']
                    # run cur to cur
                    build_from = path_file_latest
                    build_to = path_file_latest
                    if update_type == comdata.UpdateType.upgrade:
                        build_from = path_file
                    elif update_type == comdata.UpdateType.downgrade:
                        build_to = path_file

                    build_from = build_from + '.S37'
                    build_to = build_to + file_format

                    if os.path.isfile(build_from) and os.path.isfile(build_to):
                        print('=================================')
                        print('Start testcase AAA')
                        dlr = dlrmus.Dlrmus(sp, from_build=build_from, to_build=build_to,
                                            interface=interface, host_port_name=dictPort['current_host_name'])
                        dlr.execute()
                        # class method verify data
                        print('End testcase AAA')
                        print('=================================')
                    else:
                        print('Cannot run testcase xxx because did not found file: ' + build_from
                              + ' or file: ' + build_to)
    sp.close_port()
