*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Resource    ../Resource/Verify.resource
Resource    ../Resource/Setting.resource
Variables    ../MetaData/common_data.py
Test Setup       Setup      900i
Test Teardown    Teardown

*** Variables ***
${VAR_PATH_RELEASE}    D:${/}tmp${/}CE_Release
${VAR_INTERFACE}    USB-COM

*** Test Cases ***
MT_FU_HDL-USBCOM
    [Documentation]    Running HDL USBOEM
#    load scanner to "build_from" by ServicePort
#    Load Build To Scanner By SP    DR9401648    ${VAR_PATH_RELEASE}
#    prepare something before running HDL
#    Setup Before HostDownload   ${VAR_INTERFACE}
#    execute HDL
#    Load Build To Scanner By Host   ${VAR_INTERFACE}    AppOnly     DR9401657       ${VAR_PATH_RELEASE}
#    verify HDL
    Verify HDL    "AppOnly"