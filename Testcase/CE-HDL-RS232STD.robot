*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Resource    ../Resource/Verify.resource
Resource    ../Resource/Setting.resource
Resource    ../Resource/Variable.resource
Test Teardown    Teardown
Test Setup       Setup      ${PID_CE}

*** Variables ***


*** Test Cases ***
CE-AT_HDL-RS232STD-AppOnly-Upgrade-DR9401672_To_DR9401688
    [Documentation]    Running HDL RS232STD
#    load scanner to "build_from" by ServicePort
    Load Build To Scanner By SP    DR9401672
#    prepare something before running HDL
    Setup Before HostDownload   ${INTERFACE_RS232STD}
#    execute HDL
    Load Build To Scanner By Host   ${INTERFACE_RS232STD}    ${FILETYPE_APPONLY}     DR9401688
#    verify HDL
    Verify HDL    ${FILETYPE_APPONLY}     DR9401688