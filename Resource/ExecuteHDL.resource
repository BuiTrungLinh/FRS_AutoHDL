*** Settings ***
Library    ../Library/load_build.py

*** Variables ***

*** Keywords ***
Load Build To Scanner By Host
        [Arguments]    ${INTERFACE}     ${UPDATETYPE}     ${FILETYPE}     ${BUILD}    ${LASTBUILD}    ${PATHRELEASE}
        By Host    ${INTERFACE}     ${UPDATETYPE}     ${FILETYPE}     ${BUILD}    ${LASTBUILD}    ${PATHRELEASE}

Load Build To Scanner By SP
        [Arguments]    ${BUILD}    ${PATHRELEASE}
        By Sp    ${BUILD}    ${PATHRELEASE}