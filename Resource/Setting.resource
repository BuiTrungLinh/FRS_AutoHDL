*** Settings ***
Library    ../Library/setting.py

*** Variables ***

*** Keywords ***
Setup Before HostDownload
    [Documentation]     Before running HDL, need to erase log and statistics, clear ule, clear customdata, bla bla
    [Arguments]     ${INTERFACE}
    Log    ==== Execute Before HDL ====
    Execute Before Hdl      ${INTERFACE}

Setup
    [Documentation]
    [Arguments]     ${PRODUCT_ID}
    Log    ==== Execute Setup ====
    Execute Setup    ${PRODUCT_ID}

Teardown
    [Documentation]     After running HDL, set the scanner to the original settings
    Log    ==== Execute Teardown ====
    Execute Teardown