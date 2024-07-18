*** Settings ***
Library    ../Library/load_build.py
Resource    ../Resource/Variable.resource

*** Variables ***


*** Keywords ***
Load Build To Scanner By Host
        [Arguments]    ${INTERFACE}     ${FILETYPE}     ${BUILD}
        Log    <===== Load Build "${BUILD}" To Scanner By HOST =====>
        ${Result} =     By Host    ${INTERFACE}     ${FILETYPE}     ${BUILD}      ${PATH_RELEASE_CE}
        Should Be True    ${Result}[0]      ${Result}[1]
        Log    <===== END - Load Build "${BUILD}" To Scanner By HOST =====>

Load Build To Scanner By SP
        [Arguments]    ${BUILD}
        Log    <===== Load Build "${BUILD}" To Scanner By SP =====>
        ${Result} =   By Sp    ${BUILD}    ${PATH_RELEASE_CE}
        Should Be True    ${Result}[0]     ${Result}[1]
        Log    <===== END - Load Build ${BUILD} To Scanner By SP =====>