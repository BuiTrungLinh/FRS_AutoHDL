*** Settings ***
Library    ../Library/load_build.py

*** Variables ***


*** Keywords ***
Load Build To Scanner By Host
        [Arguments]    ${INTERFACE}     ${FILETYPE}     ${BUILD}      ${PATHRELEASE}
        By Host    ${INTERFACE}     ${FILETYPE}     ${BUILD}      ${PATHRELEASE}

Load Build To Scanner By SP
        [Arguments]    ${BUILD}    ${VAR_PATH_RELEASE}
        By Sp    ${BUILD}    ${VAR_PATH_RELEASE}