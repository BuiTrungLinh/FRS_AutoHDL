import sys
import time
from Library import dlrmus
import os.path
from Library import connection as con
from Library import service_port
from MetaData import common_data as comdata
import GUI.gui_main as gui_main
import Library.testcase as tcs
from MetaData.testcase_data import FormatTcs as gen_tcs_name
from Library import testcase as tcs
from Library import setting as sett

sp = None

if __name__ == '__main__':
    con.connect_port()
    sp = sett.__gServicePort
    current_host_name = sett.__gHostPort
    # current_build = service_port.get_scanner_current_information(sp, comdata.Identification.Application_ROM_ID)
    # load GUI menu for current_hwid product
    # gui = gui_main.MainGUI(sp.send_command(comdata.SPCommand.get_hwid))
    gui = gui_main.startup()
    # Path release build
    path_release_root = gui.path_release
    # dict selected release build
    dict_selected_release = gui.dict_selected_release

    for interface in dict_selected_release:
        if interface == 'LAST_BUILD':
            continue
        obj_testcase = tcs.Testcase
        arg_testcase = {gen_tcs_name.interface: interface}
        file_format = '.DAT' if interface == comdata.Interface.usboem_index else '.S37'
        # call dlrmus
        for file_type in dict_selected_release[interface]:
            file_type_name = comdata.FileType.dict_filetype[file_type]['name']
            arg_testcase[gen_tcs_name.file_type] = file_type_name
            for update_type in dict_selected_release[interface][file_type]:
                arg_testcase[gen_tcs_name.update_type] = 'CurToCur'
                testcase = obj_testcase(arg_testcase)
                is_print_tcsname = False
                for build in dict_selected_release[interface][file_type][update_type]:
                    path_file = path_release_root + '\\' + build + '\\' + file_type_name + '_' + build
                    path_file_latest = path_release_root + '\\' + dict_selected_release[
                        'LAST_BUILD'] + '\\' + file_type_name + '_' + dict_selected_release['LAST_BUILD']
                    # run cur to cur
                    build_from = path_file_latest
                    build_to = path_file_latest
                    # arg_testcase - index = 3
                    arg_testcase[gen_tcs_name.build_from] = 'Current'
                    # arg_testcase - index = 4
                    arg_testcase[gen_tcs_name.build_to] = 'Current'
                    if update_type == comdata.UpdateType.upgrade_index:
                        build_from = path_file
                        # arg_testcase[2] = 'Upgrade'
                        arg_testcase[gen_tcs_name.update_type] = 'Upgrade'
                        # arg_testcase[3] = build
                        arg_testcase[gen_tcs_name.build_from] = build
                    elif update_type == comdata.UpdateType.downgrade_index:
                        build_to = path_file
                        # arg_testcase[2] = 'Downgrade'
                        arg_testcase[gen_tcs_name.update_type] = 'Downgrade'
                        # arg_testcase[4] = build
                        arg_testcase[gen_tcs_name.build_to] = build
                    # gen testcase
                    testcase.gen_testcase()
                    if not is_print_tcsname:
                        print('*** Start testcase "{}"'.format(testcase.testcase_name))
                        is_print_tcsname = True
                    print('---- Start scenario "{}"'.format(testcase.scenario_name))
                    build_from = build_from + '.S37'
                    build_to = build_to + file_format
                    if os.path.isfile(build_from) and os.path.isfile(build_to):
                        dlr = dlrmus.Dlrmus(from_build=build_from, to_build=build_to, interface=interface)
                        # dlr.execute()
                        a = ''
                        # class method verify data
                    else:
                        print('Warning!!!: Cannot run testcase "{}" with scenario "{}" because did not found file: {} '
                              'or file {}'
                              .format(testcase.testcase_name, testcase.scenario_name, build_from, build_to))
                    print('---- End scenario "{}"'.format(testcase.scenario_name))
                print('*** End testcase "{}"'.format(testcase.testcase_name))
                print('=================================')
                is_print_tcsname = False
    sp.close_port()
