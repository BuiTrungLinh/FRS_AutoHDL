*** Settings ***
Library    ../Library/verification.py
Library    Collections
Library    String
Library    XML
Library    OperatingSystem

*** Variables ***

*** Keywords ***
Verify HDL
    [Arguments]     ${FILE_TYPE}
    Run Keyword if   ${FILE_TYPE}.upper() == "APPONLY"   Verify AppOnly
    ...    ELSE   Run Keyword if   ${FILE_TYPE} == "APPCONFIG"     Verify AppCfg
    ...    ELSE   Run Keyword if   ${FILE_TYPE} == "CFGONLY"     Verify CfgOnly
    ...    ELSE   Run Keyword if   ${FILE_TYPE} == "OTHERCONFIG"     Verify OtherCfg
    ...    ELSE   Verify AppOnly

Verify AppOnly
#    Verify IHS
    Verify Event Log

Verify AppCfg
    Verify IHS
    Log    message

Verify CfgOnly
    Verify IHS
    Log    message
  
Verify OtherCfg
    Verify IHS
    Log    message

Verify IHS
    Log    ======= Verify I-H-S
    ${OBSER_IHS}    get_obser_ihs
    ${EXPECTED_IHS}     get_expected_ihs
    Dictionaries Should Be Equal    ${OBSER_IHS}    ${EXPECTED_IHS}

Verify Event Log
    Log    ======= Verify Event Log
    ${count_passed}=     Set Variable    0
    ${VAR_ERROR_CODE}=  Set Variable   Error_Code
    &{DICT_OBSER_LOG}   get_obser_eventlog
    @{LIST_EXPECTED_LOG}    get_expected_eventlog
    FOR    ${EXP_EVT}    IN    @{LIST_EXPECTED_LOG}
        FOR    ${OBSER_EVT}    IN    @{DICT_OBSER_LOG.keys()}
            ${var_passed}=  Run Keyword And Return Status    Should Be Equal    "${EXP_EVT}"    "${DICT_OBSER_LOG[${OBSER_EVT}]["${VAR_ERROR_CODE}"]}"
            IF    ${var_passed}
                 ${count_passed}=   Evaluate   ${count_passed}+1
            END
        END
    END
#
    ${count_evt_exp}=    Get Length    ${LIST_EXPECTED_LOG}
    Should Be Equal As Numbers    ${count_evt_exp}    ${count_passed}   Total number of log events(expected - obser)