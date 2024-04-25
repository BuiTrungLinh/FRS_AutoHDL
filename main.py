import os
import subprocess
from MetaData import common as common_data

import connection as con

if __name__ == '__main__':
    subprocess.run("Tools\\DLRMUs\\dlrmus.exe -a ServicePort")
    # SP = con.get_service_ports_list()
    # if not SP["isFoundSP"]:
    #     print('Warning: Could not find any Datalogic\'s "ServicePort"')
    # else:
    #     print('Interface: {}, PortName: {}'.format(SP["current_interface"], SP["current_sp_name"]))
    #     sp_port = con.Connection(port=SP["current_sp_name"])
    #     sp_port.open_port()
    #     idenStr = sp_port.send_command('011C').decode('utf-8', errors='ignore')
    #     idenList = idenStr.replace('\\x03', '').split('\\x02')
    #     for i in idenList:
    #         if i.startswith('A'):
    #             print(i)
    #     sp_port.close_port()
