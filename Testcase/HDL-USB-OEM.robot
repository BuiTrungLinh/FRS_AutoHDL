*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Variables    ../MetaData/common_data.py

*** Variables ***
${VAR_INTERFACE}    ${Interface}
${VAR_UPDATE_TYPE}    ${UpdateType}
${VAR_FILE_TYPE}    ${FileType}

*** Test Cases ***
MT_FU_HDL-USBOEM
    [Documentation]    Running HDL USBOEM
    Execute HDL    6    1
    ...     1    DR9401648    DR9401657
    ...     D:${/}tmp${/}CE_Release


