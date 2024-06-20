*** Settings ***
Library    ../Library/execute.py

*** Variables ***

*** Keywords ***
Execute HDL
        [Arguments]    ${INTERFACE}     ${BUILD}    ${LASTBUILD}    ${FILETYPE}    ${UPDATETYPE}    ${PATHRELEASE}
        exe_hostdownload    ${INTERFACE}     ${BUILD}    ${LASTBUILD}    ${FILETYPE}    ${UPDATETYPE}    ${PATHRELEASE}
