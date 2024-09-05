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
    Set Global Variable    ${EXPECTED_FILE_TYPE}    "${FILE_TYPE}".upper()
    Run Keyword if   ${EXPECTED_FILE_TYPE} == "APPONLY"   Verify AppOnly
    ...    ELSE   Run Keyword if   ${EXPECTED_FILE_TYPE} == "APPCONFIG"     Verify AppCfg
    ...    ELSE   Run Keyword if   ${EXPECTED_FILE_TYPE} == "CFGONLY"     Verify CfgOnly
    ...    ELSE   Run Keyword if   ${EXPECTED_FILE_TYPE} == "OTHERCONFIG"     Verify OtherCfg
    ...    ELSE   Verify AppOnly
    Log    <======= END - VERIFY HOST DOWNLOAD =======>

Verify AppOnly
    Verify IHS
    Verify Event Log


Verify AppCfg
    Verify IHS
    Verify Event Log
    Verify Config Tag

Verify CfgOnly
    Verify IHS
    Verify Event Log
    Verify Config Tag
  
Verify OtherCfg
    Verify IHS
    Verify Event Log
    Verify Config Tag

Verify IHS
    Log    ======= Verify I-H-S =======
    ${OBSER_IHS}    get_obser_ihs
    ${EXPECTED_IHS}     get_expected_ihs    ${EXPECTED_BUILD}   ${EXPECTED_FILE_TYPE}
    Run Keyword And Continue On Failure    Dictionaries Should Be Equal    ${EXPECTED_IHS}    ${OBSER_IHS}
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

#    Verify the number of events
    ${len_obser} =  Get Length    ${DICT_OBSER_LOG}
    ${len_expected} =   Get Length    ${LIST_EXPECTED_LOG}
    Run Keyword And Continue On Failure    Should Be Equal As Numbers    ${len_obser}   ${len_expected}     msg=The current number of events in the scanner is incorrect.
#    Log    Observation:
#    Log Dictionary    &{DICT_OBSER_LOG}
#    Log    Expected:
#    Log List    @{LIST_EXPECTED_LOG}
    Log    ======= END - Verify Event Log =======

Verify Config Tag
    Log    ======= Verify Config Tag =======
    ${EXPECTED_CFG}    get_expected_config
    ${OBSER_CFG}     get_obser_config
    Run Keyword And Continue On Failure    Dictionaries Should Be Equal    ${EXPECTED_CFG}    ${OBSER_CFG}
    Log    ======= END - Verify Config Tag =======

Verify ULE
    Log    ======= Verify ULE =======
    ${EXPECTED_ULE}    get_expected_ule
    ${OBSER_ULE}     get_obser_ule
    Run Keyword And Continue On Failure    Should Be Equal    ${EXPECTED_ULE}    ${OBSER_ULE}
    Log    ======= END - Verify ULE =======