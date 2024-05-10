import sys
import time
from Library import dlrmus
import os.path
from Library import connection as con
from Library import service_port
from MetaData import common_data as comdata
import GUI.gui_main as gui_main
import Library.testcase as tcs

sp = None

if __name__ == '__main__':
    connect_port = con.connect_port()
    sp = connect_port[0]
    dictPort = connect_port[1]
    current_build = service_port.get_scanner_current_information(sp, comdata.Identification.Application_ROM_ID)
    # load GUI menu for current_hwid product
    gui = gui_main.MainGUI(sp.send_command(comdata.SPCommand.get_hwid))
    # Path release build
    path_release_root = gui.path_release
    # dict selected release build
    dict_selected_release = gui.dict_selected_release

    for interface in dict_selected_release:
        if interface == 'LAST_BUILD':
            continue
        arg_testcase = [interface]
        file_format = '.DAT' if interface == comdata.Interface.usboem else '.S37'
        # call dlrmus
        for file_type in dict_selected_release[interface]:
            arg_testcase.append(file_type)
            for update_type in dict_selected_release[interface][file_type]:
                arg_testcase.append('CurToCur')
                for build in dict_selected_release[interface][file_type][update_type]:
                    path_file = path_release_root + '\\' + build + '\\' + file_type + '_' + build
                    path_file_latest = path_release_root + '\\' + dict_selected_release[
                        'LAST_BUILD'] + '\\' + file_type + '_' + dict_selected_release['LAST_BUILD']
                    # run cur to cur
                    build_from = path_file_latest
                    build_to = path_file_latest
                    # arg_testcase - index = 3
                    arg_testcase.append('Current')
                    # arg_testcase - index = 4
                    arg_testcase.append('Current')
                    if update_type == comdata.UpdateType.upgrade:
                        build_from = path_file
                        arg_testcase[2] = 'Upgrade'
                        arg_testcase[3] = build
                    elif update_type == comdata.UpdateType.downgrade:
                        build_to = path_file
                        arg_testcase[2] = 'Downgrade'
                        arg_testcase[4] = build

                    build_from = build_from + '.S37'
                    build_to = build_to + file_format

                    # gen testcase
                    testcase_name = tcs.gen_testcase(arg_testcase)
                    if os.path.isfile(build_from) and os.path.isfile(build_to):
                        print('=================================')
                        print('Start testcase {}'.format(testcase_name))
                        # dlr = dlrmus.Dlrmus(sp, from_build=build_from, to_build=build_to,
                        #                     interface=interface, host_port_name=dictPort['current_host_name'])
                        # dlr.execute()
                        # class method verify data
                        print('End testcase {}'.format(testcase_name))
                        print('=================================')
                    else:
                        print('Cannot run testcase {} because did not found file: {} or file {}'
                              .format(testcase_name, build_from, build_to))
    sp.close_port()
