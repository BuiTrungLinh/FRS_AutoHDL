import os.path
import sys

sys.path.insert(0, r'..\..\FRS_AutoHDL')

from MetaData import common_data as comdata
from Library import dlrmus
from Library import connection as con
from setting import print_message_to_console
import setting as sett


def by_host(interface, update_type, file_type, build, path_release_root):
    file_format = '.DAT' if int(interface) == comdata.Interface.usboem_index else '.S37'
    file_type_name = comdata.FileType.dict_filetype[int(file_type)]['name']
    path_file = path_release_root + '\\' + build + '\\' + file_type_name + '_' + build + file_format
    # check pathfile is not existed
    if not os.path.isfile(path_file):
        print_message_to_console('Did not found file: {} !!!'.format(path_file))
        # Todo
        # Do somthing here when loading by host fail: skip testcase or rerun it
        return
    dlr = dlrmus.Dlrmus(to_build=path_file, interface=int(interface)).update_by_host()
    if dlr:
        print_message_to_console(comdata.Message.Succ_Dlrmus_Update_Host.format(build, interface))
    else:
        print_message_to_console(comdata.Message.Error_Dlrmus_Update_Host.format(build, interface))
        # Todo
        # Do somthing here when loading by host fail: skip testcase or rerun it


def by_sp(build, path_release_root):
    path_file = path_release_root + '\\' + build + '\\AppOnly_' + build + '.S37'
    if not os.path.isfile(path_file):
        print_message_to_console('Did not found file: {} !!!'.format(path_file))
        # Todo
        # Do somthing here when loading by SP fail: skip testcase or rerun it
        return
    dlr = dlrmus.Dlrmus(from_build=path_file).update_by_sp()
    if dlr:
        print_message_to_console(comdata.Message.Succ_Dlrmus_Update_SP.format(build))
    else:
        print_message_to_console(comdata.Message.Error_Dlrmus_Update_SP.format(build))
        # Todo
        # Do somthing here when loading by SP fail: skip testcase or rerun it
