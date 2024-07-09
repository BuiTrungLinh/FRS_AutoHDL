import os.path
import sys
sys.path.insert(0, r'..\..\FRS_AutoHDL')

from MetaData import common_data as comdata
import Library.setting as sett
import Library.dlrmus as dlrmus
import Library.verification as ver


def by_host(interface, file_type, build, path_release_root):
    ver.verify_iden()
    # Conversion Interface
    interface = interface.replace('-', '').replace(' ', '').upper()
    interface_index = 0
    interface_name = ''
    for ifs in comdata.Interface.dict_interface:
        if interface == ifs['name'].upper():
            interface_index = ifs
            interface_name = ifs['full_name']
            break
    # Conversion File Type
    file_type = file_type.replace('-', '').replace(' ', '').upper()
    file_type_name = ''
    for ft in comdata.FileType.dict_filetype:
        if file_type == ft['name'].upper():
            file_type_name = ft['name']
            break
    file_format = '.DAT' if comdata.Interface.usboem_index == interface_index else '.S37'
    path_file = path_release_root + '\\' + build + '\\' + file_type_name + '_' + build + file_format
    # check pathfile is not existed
    if not os.path.isfile(path_file):
        sett.print_message_to_console('Did not found file: {} !!!'.format(path_file))
        # Todo
        # Do somthing here when loading by host fail: skip testcase or rerun it
        return
    dlr = dlrmus.Dlrmus(to_build=path_file, interface=interface_index).update_by_host()
    if dlr:
        sett.print_message_to_console(comdata.Message.Succ_Dlrmus_Update_Host.format(build, interface_name))
    else:
        sett.print_message_to_console(comdata.Message.Error_Dlrmus_Update_Host.format(build, interface_name))
        # Todo
        # Do somthing here when loading by host fail: skip testcase or rerun it


def by_sp(build, path_release_root):
    path_file = path_release_root + '\\' + build + '\\AppOnly_' + build + '.S37'
    if not os.path.isfile(path_file):
        sett.print_message_to_console('Did not found file: {} !!!'.format(path_file))
        # Todo
        # Do somthing here when loading by SP fail: skip testcase or rerun it
        return
    dlr = dlrmus.Dlrmus(from_build=path_file).update_by_sp()
    if dlr:
        sett.print_message_to_console(comdata.Message.Succ_Dlrmus_Update_SP.format(build))
    else:
        sett.print_message_to_console(comdata.Message.Error_Dlrmus_Update_SP.format(build))
        # Todo
        # Do somthing here when loading by SP fail: skip testcase or rerun it
