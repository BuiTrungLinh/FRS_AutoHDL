import os.path
import sys
sys.path.insert(0, r'..\FRS_AutoHDL')

from MetaData import common_data as comdata
from MetaData.testcase_data import FormatTcs as gen_tcs_name
from Library import dlrmus
from Library import connection as con


def exe_hostdownload(interface, update_type, file_type_name, build, last_build, path_release_root):
    connect_port = con.connect_port()
    sp = connect_port[0]
    dictPort = connect_port[1]
    # obj_testcase = tcs.Testcase
    # arg_testcase = {gen_tcs_name.interface: interface}
    file_format = '.DAT' if int(interface) == comdata.Interface.usboem_index else '.S37'
    # call dlrmus
    # arg_testcase[gen_tcs_name.file_type] = file_type_name
    # arg_testcase[gen_tcs_name.update_type] = 'CurToCur'
    # testcase = obj_testcase(arg_testcase)

    path_file = path_release_root + '\\' + build + '\\' + file_type_name + '_' + build
    path_file_latest = path_release_root + '\\' + last_build + '\\' + file_type_name + '_' + last_build
    # run cur to cur
    build_from = path_file_latest
    build_to = path_file_latest
    # arg_testcase - index = 3
    # arg_testcase[gen_tcs_name.build_from] = 'Current'
    # arg_testcase - index = 4
    # arg_testcase[gen_tcs_name.build_to] = 'Current'
    if int(update_type) == comdata.UpdateType.upgrade_index:
        build_from = path_file
        # arg_testcase[2] = 'Upgrade'
        # arg_testcase[gen_tcs_name.update_type] = 'Upgrade'
        # arg_testcase[3] = build
        # arg_testcase[gen_tcs_name.build_from] = build
    elif int(update_type) == comdata.UpdateType.downgrade_index:
        build_to = path_file
        # arg_testcase[2] = 'Downgrade'
        # arg_testcase[gen_tcs_name.update_type] = 'Downgrade'
        # arg_testcase[4] = build
        # arg_testcase[gen_tcs_name.build_to] = build
    # gen testcase
    # testcase.gen_testcase()
    build_from = build_from + '.S37'
    build_to = build_to + file_format
    if os.path.isfile(build_from) and os.path.isfile(build_to):
        dlr = dlrmus.Dlrmus(sp, from_build=build_from, to_build=build_to,
                            interface=interface, host_port_name=dictPort['current_host_name'])
        dlr.execute()
        # class method verify data
    else:
        print('Warning!!!: Cannot run testcase because did not found file: {} or file: {}'
              .format(build_from, build_to))

def execute_sp():
    return
