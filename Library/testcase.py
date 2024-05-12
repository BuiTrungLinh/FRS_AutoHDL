from MetaData import common_data as comdata
from MetaData.testcase_data import FormatTcs as gen_tcs_name


class Testcase:
    def __init__(self, arg_tcs):
        self.arg_tcs = arg_tcs
        self.testcase_name = ''
        self.scenario_name = ''
        self.testcase_result = None
        self.scenario_result = None

    def gen_testcase(self):
        # TC_FU_HDL_RS232STD-UPOS_AppOnly_Upgrade
        # Scenario: DR940xx1 to Current
        # Scenario: DR940xx2 to Current
        # Scenario: DR940xx3 to Current
        #
        # TC_FU_HDL_RS232STD-UPOS_AppCfg_CurToCur
        # Scenario: Current to Current
        #
        # TC_FU_HDL_RS232STD-UPOS_OtherCfg_Downgrade
        # Scenario: Current to DR940xx1
        # Scenario: Current to DR940xx2
        # Scenario: Current to DR940xx3
        #
        # TC_FU_HDL_RS232STD-UPOS_CfgOnly_CurToCur
        # Scenario: Current to Current
        match self.arg_tcs[gen_tcs_name.interface]:
            case comdata.Interface.rs232std_index:
                tcs_interface = 'RS232STD'
            case comdata.Interface.rs232wn_index:
                tcs_interface = 'RS232WN'
            case comdata.Interface.rs232sc_index:
                tcs_interface = 'RS232SC'
            case comdata.Interface.usbcom_index:
                tcs_interface = 'USBCOM'
            case comdata.Interface.usbcomsc_index:
                tcs_interface = 'USBCOM-SC'
            case comdata.Interface.usboem_index:
                tcs_interface = 'USBOEM'
            case _:
                tcs_interface = 'RS232STD'

        self.testcase_name = '{}_{}-{}_{}_{}'.format(gen_tcs_name.prefix, tcs_interface, gen_tcs_name.upos,
                                                     self.arg_tcs[gen_tcs_name.file_type],
                                                     self.arg_tcs[gen_tcs_name.update_type])
        self.scenario_name = '{} To {}'.format(self.arg_tcs[gen_tcs_name.build_from]
                                               , self.arg_tcs[gen_tcs_name.build_to])
        a = ''
