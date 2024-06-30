*** Settings ***
Library     ../Library/setting.py

*** Variables ***

*** Keywords ***
Setup Before HostDownload
    [Documentation]     Before running HDL, need to erase log and statistics, clear ule, clear customdata, bla bla
    [Arguments]     ${INTERFACE}
    Execute Before Hdl      ${INTERFACE}

Setup
    [Documentation]
    [Arguments]     ${PRODUCT_ID}
    Execute Setup   ${PRODUCT_ID}

Teardown
    [Documentation]     After running HDL, set the scanner to the original settings
    Execute Teardown