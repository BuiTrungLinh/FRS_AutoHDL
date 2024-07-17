*** Settings ***
Library    ../Library/setting.py

*** Variables ***

*** Keywords ***
Setup Before HostDownload
    [Documentation]     Before running HDL, need to erase log and statistics, clear ule, clear customdata, bla bla
    [Arguments]     ${INTERFACE}
    Log    <==== Setup Before HDL ====>
    Execute Before Hdl      ${INTERFACE}
    Log    <==== END - Setup Before HDL ====>

Setup
    [Documentation]
    [Arguments]     ${PRODUCT_ID}
    Log    <==== Execute Setup ====>
    Execute Setup    ${PRODUCT_ID}
    Log    <==== END - Execute Setup ====>

Teardown
    [Documentation]     After running HDL, set the scanner to the original settings
    Log    <==== Execute Teardown ====>
    Execute Teardown
    Log    <==== END - Execute Teardown ====>