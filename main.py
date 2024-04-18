import time

import connection as con

if __name__ == '__main__':
    SP = con.get_service_ports_list()
    if not SP["isFoundSP"]:
        print('Warning: Could not find any Datalogic\'s "ServicePort"')
    else:
        print('Interface: {}, PortName: {}'.format(SP["current_interface"], SP["current_sp_name"]))
        sp_port = con.Connection(port=SP["current_sp_name"])
        sp_port.open_port()
        print(sp_port.send_command('011B'))
        sp_port.close_port()
