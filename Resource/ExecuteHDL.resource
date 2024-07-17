*** Settings ***
Library    ../Library/load_build.py

*** Variables ***


*** Keywords ***
Load Build To Scanner By Host
        [Arguments]    ${INTERFACE}     ${FILETYPE}     ${BUILD}      ${PATHRELEASE}
        Log    <===== Load Build "${BUILD}" To Scanner By HOST =====>
        ${Result} =     By Host    ${INTERFACE}     ${FILETYPE}     ${BUILD}      ${PATHRELEASE}
        Should Be True    ${Result}[0]      ${Result}[1]
        Log    <===== END - Load Build "${BUILD}" To Scanner By HOST =====>

Load Build To Scanner By SP
        [Arguments]    ${BUILD}    ${VAR_PATH_RELEASE}
        Log    <===== Load Build "${BUILD}" To Scanner By SP =====>
        ${Result} =   By Sp    ${BUILD}    ${VAR_PATH_RELEASE}
        Should Be True    ${Result}[0]     ${Result}[1]
        Log    <===== END - Load Build ${BUILD} To Scanner By SP =====>