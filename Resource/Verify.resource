*** Settings ***
Library    ../Library/verification.py
Library    Collections
Library    String

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
    Log    ========== Verify App-Only
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
    ${VAR_ERROR_CODE}=  Set Variable   ERROR_CODE
    ${VAR_RESULT}=  Set Variable    ${False}

    @{DICT_OBSER_LOG}   Split String    get_obser_eventlog
    @{LIST_EXPECTED_LOG}     get_expected_eventlog
    FOR    ${EXP_EVT}    IN    @{LIST_EXPECTED_LOG}
        Log    ${EXP_EVT}
        FOR    ${OBSER_EVT}    IN    @{DICT_OBSER_LOG}
            Log    @{DICT_OBSER_LOG[${OBSER_EVT}]["${VAR_ERROR_CODE}"]}
#            Run Keyword If    ${EXP_EVT} in ${DICT_OBSER_LOG["${OBSER_EVT}"]["${VAR_ERROR_CODE}"]}
#            ...  pass execution  ${EXP_EVT} is existed
#            fail  ${EXP_EVT} is not existed
        END
    END