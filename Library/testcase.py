from MetaData import common_data as comdata

def gen_testcase(arg):
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

    # self.dict_selected_release = {
    #                     #   4= usbcom
    #                     4: {
    #                         "AppOnly": {
    #                             1: ['DR9401638', 'DR9401643', 'DR9401646'],
    #                             2: ['DR9401638', 'DR9401643', 'DR9401646'],
    #                         },
    #                         "AppCfg": {
    #                             1: ['DR9401638', 'DR9401643', 'DR9401646'],
    #                         }
    #                     },
    #                     #   6 = usboem
    #                     6: {
    #                         "AppOnly": {
    #                             1: ['DR9401638', 'DR9401643', 'DR9401646'],
    #                         },
    #                         "AppCfg": {
    #                             1: ['DR9401638', 'DR9401643', 'DR9401646'],
    #                             2: ['DR9401638', 'DR9401643', 'DR9401646'],
    #                         }
    #                     },
    #                     "LAST_BUILD": "DR9401648"
    #                 }
    tcs_prefix = 'TC_FU_HDL'
    tcs_interface = ''
    match arg[0]:
        case comdata.Interface.rs232std:
            tcs_interface = 'RS232STD'
        case comdata.Interface.rs232wn:
            tcs_interface = 'RS232WN'
        case comdata.Interface.rs232sc:
            tcs_interface = 'RS232SC'
        case comdata.Interface.usbcom:
            tcs_interface = 'USBCOM'
        case comdata.Interface.usbcomsc:
            tcs_interface = 'USBCOM-SC'
        case comdata.Interface.usboem:
            tcs_interface = 'USBOEM'
        case _:
            tcs_interface = 'RS232STD'

    testcase_name = tcs_prefix+'_'+tcs_interface+'_UPOS_' + arg[1] + '_' + arg[2]
    scenario_name = arg[3] + ' To ' + arg[4]
    return [testcase_name, scenario_name, None]
