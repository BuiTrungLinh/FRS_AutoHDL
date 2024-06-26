*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Resource    ../Resource/Verify.resource
Resource    ../Resource/Setting.resource
Variables    ../MetaData/common_data.py

*** Variables ***
${VAR_INTERFACE}    ${Interface}
${VAR_UPDATE_TYPE}    ${UpdateType}
${VAR_FILE_TYPE}    ${FileType}

*** Test Cases ***
MT_FU_HDL-USBOEM
    [Documentation]    Running HDL USBOEM
#    load scanner to "build_from" by ServicePort
    Load Build To Scanner By SP    DR9401648    D:${/}tmp${/}CE_Release
#    prepare something before running HDL
    Setting Before Running
#    execute HDL
    Load Build To Scanner By Host    6    1
    ...     1    DR9401648    DR9401657
    ...     D:${/}tmp${/}CE_Release
#    verify HDL
    Verify HDL
#    Teardown scanner
    Setting After Running