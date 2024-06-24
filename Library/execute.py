import os.path
import sys
sys.path.insert(0, r'..\..\FRS_AutoHDL')

from robot.libraries.BuiltIn import BuiltIn
from MetaData import common_data as comdata
from Library import dlrmus
from Library import connection as con
from common import print_message_to_console


def exe_hostdownload(interface, update_type, file_type, build, last_build, path_release_root):
    connect_port = con.connect_port()
    sp = connect_port[0]
    dictPort = connect_port[1]
    file_format = '.DAT' if int(interface) == comdata.Interface.usboem_index else '.S37'
    file_type_name = comdata.FileType.dict_filetype[int(file_type)]['name']
    path_file = path_release_root + '\\' + build + '\\' + file_type_name + '_' + build
    path_file_latest = path_release_root + '\\' + last_build + '\\' + file_type_name + '_' + last_build
    # run cur to cur
    build_from = path_file_latest
    build_to = path_file_latest
    if int(update_type) == comdata.UpdateType.upgrade_index:
        build_from = path_file
    elif int(update_type) == comdata.UpdateType.downgrade_index:
        build_to = path_file
    build_from = build_from + '.S37'
    build_to = build_to + file_format
    if os.path.isfile(build_from) and os.path.isfile(build_to):
        dlr = dlrmus.Dlrmus(sp, from_build=build_from, to_build=build_to,
                            interface=int(interface), host_port_name=dictPort['current_host_name'])
        dlr.execute()
        # class method verify data
    else:
        print_message_to_console('Cannot run testcase because did not found file: {} \n or file: {}'
                      .format(build_from, build_to))


def execute_sp():
    return
