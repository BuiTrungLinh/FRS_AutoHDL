*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Resource    ../Resource/Verify.resource
Resource    ../Resource/Setting.resource
Resource    ../Resource/Variable.resource
Test Teardown    Teardown
Test Setup       Setup      ${PID_CE}

*** Variables ***


*** Test Cases ***
AT_HDL-USBCOM-AppOnly-Upgrade-DR9401646_To_DR9401648
    [Documentation]    Running HDL USBOEM
#    load scanner to "build_from" by ServicePort
    Load Build To Scanner By SP    DR9401646
#    prepare something before running HDL
    Setup Before HostDownload   ${INTERFACE_USBCOM}
#    execute HDL
    Load Build To Scanner By Host   ${INTERFACE_USBCOM}    ${FILETYPE_APPONLY}     DR9401648
#    verify HDL
    Verify HDL    ${FILETYPE_APPONLY}     DR9401648