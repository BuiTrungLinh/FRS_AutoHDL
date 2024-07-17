*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Resource    ../Resource/Verify.resource
Resource    ../Resource/Setting.resource
Test Teardown    Teardown
Variables    ../MetaData/common_data.py
Test Setup       Setup      900i

*** Variables ***
${VAR_PATH_RELEASE}    D:${/}tmp${/}CE_Release
${VAR_INTERFACE}    USB-COM

*** Test Cases ***
AT_HDL-USBCOM-AppOnly-Upgrade-DR9401646_To_DR9401648
    [Documentation]    Running HDL USBOEM
#    load scanner to "build_from" by ServicePort
#    Load Build To Scanner By SP    DR9401646    ${VAR_PATH_RELEASE}
#    prepare something before running HDL
    Setup Before HostDownload   ${VAR_INTERFACE}
#    execute HDL
    Load Build To Scanner By Host   ${VAR_INTERFACE}    AppOnly     DR9401648       ${VAR_PATH_RELEASE}
#    verify HDL
#    Verify HDL    "AppOnly"