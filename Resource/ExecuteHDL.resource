*** Settings ***
Library    ../Library/execute.py

*** Variables ***

*** Keywords ***
Execute HDL
        [Arguments]    ${INTERFACE}     ${BUILD}    ${LASTBUILD}    ${FILETYPE}    ${UPDATETYPE}    ${PATHRELEASE}
        executehdls    ${INTERFACE}     ${BUILD}    ${LASTBUILD}    ${FILETYPE}    ${UPDATETYPE}    ${PATHRELEASE}
        log    asfafa