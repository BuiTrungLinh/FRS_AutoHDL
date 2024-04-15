from serial.threaded import LineReader, ReaderThread
import serial
import serial.tools.list_ports as Port_list
import time
import traceback
import sys


class PrintLines(LineReader):
    def __init__(self):
        super().__init__()
        self.TERMINATOR = b'\r'
        self.buffer = bytearray()
        self.label_data = ''

    def connection_made(self, transport):
        super(PrintLines, self).connection_made(transport)
        sys.stdout.write('port opened\n')

    def data_received(self, data):
        self.buffer.extend(data)
        if len(self.buffer) > 1:
            packet = self.buffer.split(self.TERMINATOR, 1)[0]
            super().handle_packet(packet)
            self.buffer = bytearray()

    def handle_line(self, data):
        sys.stdout.write('line received: {!r}\n'.format(data))
        self.label_data = data

    def connection_lost(self, exc):
        if exc:
            traceback.print_exc(exc)
        sys.stdout.write('port closed\n')


class Connection(object):
    def __init__(self, port='', baudrate=115200, parity='N'):
        self.port = port
        self.baudrate = baudrate
        self.parity = 'N'
        self.ser = None
        self.readerThread = None
        self.protocol = None

    def open_port(self):
        self.ser = serial.serial_for_url(url=self.port, baudrate=self.baudrate, parity=self.parity, timeout=1)
        self.readerThread = ReaderThread(self.ser, PrintLines)
        self.readerThread.start()
        transport, self.protocol = self.readerThread.connect()

    def close_port(self):
        if self.readerThread.is_alive():
            self.readerThread.close()
            del self.readerThread, self.ser, self.protocol

    def send_command(self, command):
        self.protocol.write_line(format_sp_command(command))


def format_sp_command(cmd):
    return cmd


def calculate_check_digit(cmd):
    return cmd


def get_service_ports_list():
    current_interface = ''
    current_sp_name = ''
    isFoundSP = False
    for port in Port_list.comports():
        # print('hwid: {}, desc: {}, name: {}'.format(port.hwid, port.description, port.name))
        current_sp_name = port.name
        # 1529 = 05F9 (DEC to HEX)
        if port.vid == int('05F9', 16):
            isFoundSP = True
            # 16384 = 4000 (DEC to HEX)
            if port.pid == int('4000', 16):
                current_interface = 'RS232'
                break
            # 16390 = 4006 (DEC to HEX)
            elif port.pid == int('4006', 16) and port.location is None:
                current_interface = 'USBCOM'
                break
            # 16395 = 400B (DEC to HEX)
            elif port.pid == int('400B', 16) and port.location is None:
                current_interface = 'USBCOM-SC'
                break
            # CE: 1605, AP: 1517, FR: 1515 and 1516
            elif port.pid in list[int('1605', 16), int('1515', 16), int('1516', 16), int('1517', 16)]:
                current_interface = 'USBOEM'
                break

    dictPort = {
        "current_interface": current_interface,
        "current_sp_name": current_sp_name,
        "isFoundSP": isFoundSP,
    }

    return dictPort


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    SP = get_service_ports_list()
    if not SP["isFoundSP"]:
        print('Warning: Could not find any Datalogic\'s "ServicePort"')
    else:
        print('Interface: {}, PortName: {}'.format(SP["current_interface"], SP["current_sp_name"]))
        sp_port = Connection(port=SP["current_sp_name"])
        sp_port.open_port()
        sp_port.send_command('\x81\x00\x00\x00\x03\x00\x1C\x60')
        sp_port.close_port()
