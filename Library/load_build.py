import os.path
import sys
sys.path.insert(0, r'..\..\FRS_AutoHDL')

from MetaData import common_data as comdata
import Library.setting as sett
import Library.dlrmus as dlrmus


def by_host(interface, file_type, build, path_release_root):
    # Conversion Interface
    interface = interface.replace('-', '').replace(' ', '').upper()
    interface_index = 0
    for ifs in comdata.Interface.dict_interface:
        if interface == comdata.Interface.dict_interface[ifs]['name'].upper():
            interface_index = ifs
            break
    # Conversion File Type
    file_type = file_type.replace('-', '').replace(' ', '').upper()
    file_type_name = ''
    for ft in comdata.FileType.dict_filetype:
        if file_type == comdata.FileType.dict_filetype[ft]['name'].upper():
            file_type_name = comdata.FileType.dict_filetype[ft]['name']
            break
    file_format = '.DAT' if comdata.Interface.usboem_index == interface_index else '.S37'
    path_file = path_release_root + '\\' + build + '\\' + file_type_name + '_' + build + file_format
    # check pathfile is not existed
    if not os.path.isfile(path_file):
        return [False, 'Did not found file: {} !!!'.format(path_file)]
    dlrmus.Dlrmus(to_build=path_file, interface=interface_index).update_by_host()
    return [True, comdata.Message.Done_Dlrmus_Update_Host.format(build)]


def by_sp(build, path_release_root):
    path_file = path_release_root + '\\' + build + '\\AppOnly_' + build + '.S37'
    if not os.path.isfile(path_file):
        return [False, 'Did not found file: {} !!!'.format(path_file)]
    return dlrmus.Dlrmus(from_build=path_file).update_by_sp()
