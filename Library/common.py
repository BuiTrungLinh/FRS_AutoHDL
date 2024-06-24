from robot.libraries.BuiltIn import BuiltIn
import logging

def print_message_to_console(msg=''):
    BuiltIn().log_to_console(msg)