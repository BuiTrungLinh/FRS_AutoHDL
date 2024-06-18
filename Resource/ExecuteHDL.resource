*** Settings ***
Library    Library/service_port.py
*** Variables ***

*** Keywords ***
Execute HDL
        [Arguments]    ${INTERFACE}    ${FILE_TYPE}    ${UPDATE_TYPE}    ${BUILD_FROM}    ${BUILD_TO}
        set interface
