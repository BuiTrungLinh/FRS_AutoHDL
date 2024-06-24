*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Variables    ../MetaData/common_data.py

*** Variables ***
${VAR_INTERFACE}    ${Interface}
${VAR_UPDATE_TYPE}    ${UpdateType}
${VAR_FILE_TYPE}    ${FileType}

*** Test Cases ***
AT_FU_HDL-USBCOM
    [Documentation]    Running HDL USBCOM
    Execute HDL    4    1
    ...     1    DR9401648    DR9401657
    ...     D:${/}tmp${/}CE_Release
