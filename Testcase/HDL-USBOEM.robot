*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Resource    ../Resource/Verify.resource
Resource    ../Resource/Setting.resource
Variables    ../MetaData/common_data.py
Test Setup       Setup
Test Teardown    Teardown

*** Variables ***
${VAR_INTERFACE}    ${Interface}
${VAR_UPDATE_TYPE}    ${UpdateType}
${VAR_FILE_TYPE}    ${FileType}
${VAR_PATH_RELEASE}    D:${/}tmp${/}CE_Release

*** Test Cases ***
MT_FU_HDL-USBOEM
    [Documentation]    Running HDL USBOEM
#    load scanner to "build_from" by ServicePort
    Load Build To Scanner By SP    DR9401648    ${VAR_PATH_RELEASE}
#    prepare something before running HDL
    Setup Before HostDownload   ${Interface.usboem_index}
#    execute HDL
    Load Build To Scanner By Host    6    1
    ...     1    DR9401648    DR9401657
    ...     ${VAR_PATH_RELEASE}
#    verify HDL
    Verify HDL