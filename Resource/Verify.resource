*** Settings ***
Library    ../Library/verification.py
Library    Collections
Library    String
Library    XML
Library    OperatingSystem

*** Variables ***

*** Keywords ***
Verify HDL
    Log    <======= VERIFY HOST DOWNLOAD =======>
    [Arguments]     ${FILE_TYPE}    ${BUILD}
    Set Global Variable    ${EXPECTED_BUILD}    ${BUILD}
    Run Keyword if   "${FILE_TYPE}".upper() == "APPONLY"   Verify AppOnly
    ...    ELSE   Run Keyword if   ${FILE_TYPE} == "APPCONFIG"     Verify AppCfg
    ...    ELSE   Run Keyword if   ${FILE_TYPE} == "CFGONLY"     Verify CfgOnly
    ...    ELSE   Run Keyword if   ${FILE_TYPE} == "OTHERCONFIG"     Verify OtherCfg
    ...    ELSE   Verify AppOnly
    Log    <======= END - VERIFY HOST DOWNLOAD =======>

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
    Log    ======= Verify I-H-S =======
    ${OBSER_IHS}    get_obser_ihs
    ${EXPECTED_IHS}     get_expected_ihs    ${EXPECTED_BUILD}
    Run Keyword And Continue On Failure    Dictionaries Should Be Equal    ${OBSER_IHS}    ${EXPECTED_IHS}
    Log    ======= END - Verify I-H-S =======

Verify Event Log
    Log    ======= Verify Event Log =======
    ${VAR_RESULT}=  Set Variable    ${False}
    ${VAR_ERROR_CODE}=  Set Variable   Error_Code
    &{DICT_OBSER_LOG}   get_obser_eventlog
    @{LIST_EXPECTED_LOG}    get_expected_eventlog
    FOR    ${EXP_EVT}    IN    @{LIST_EXPECTED_LOG}
        FOR    ${OBSER_EVT}    IN    @{DICT_OBSER_LOG.keys()}
            ${VAR_RESULT}=  Run Keyword And Return Status    Should Be Equal    "${EXP_EVT}"    "${DICT_OBSER_LOG[${OBSER_EVT}]["${VAR_ERROR_CODE}"]}"
            IF    ${VAR_RESULT}
                 BREAK
            END
        END
        Run Keyword And Continue On Failure    Should Be True   ${VAR_RESULT}   Event log: "${EXP_EVT}" is not existed
    END
    Log    ======= END - Verify Event Log =======
