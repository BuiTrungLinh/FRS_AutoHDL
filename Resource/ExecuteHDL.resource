*** Settings ***
Library    ../Library/execute.py

*** Variables ***

*** Keywords ***
Execute HDL
        [Arguments]    ${INTERFACE}     ${UPDATETYPE}     ${FILETYPE}     ${BUILD}    ${LASTBUILD}    ${PATHRELEASE}
        exe_hostdownload    ${INTERFACE}     ${UPDATETYPE}     ${FILETYPE}     ${BUILD}    ${LASTBUILD}    ${PATHRELEASE}
