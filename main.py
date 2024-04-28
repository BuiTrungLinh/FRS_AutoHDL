import serial
import time
import connection as con

if __name__ == '__main__':

    sp_comport = con.get_service_ports_list()
    if not sp_comport["isFoundSP"]:
        print('Warning: Could not find any Datalogic\'s "ServicePort"')
    else:
        print('Interface: {}, PortName: {}'.format(sp_comport["current_interface"], sp_comport["current_sp_name"]))
        sp = con.Connection(port=sp_comport["current_sp_name"])
        sp.open_port()
        idenStr = str(sp.send_command('011C'))
        print(idenStr)
        # idenList = idenStr.replace('\\x03', '').split('\\x02')
        # for i in idenList:
        #     if i.startswith('A'):
        #         print(i)
        sp.close_port()
