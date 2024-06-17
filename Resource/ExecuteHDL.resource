*** Settings ***

*** Variables ***
${INTERFACE}    AAAA
${FILE_TYPE}    BBBB
${UPDATE_TYPE}    CCCC
${BUILD_FROM}    DDDD
${BUILD_TO}    EEEEE

*** Keywords ***
Execute HDL
        [Arguments]    ${INTERFACE}    ${FILE_TYPE}    ${UPDATE_TYPE}    ${BUILD_FROM}    ${BUILD_TO}
