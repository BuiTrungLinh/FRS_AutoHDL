*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Variables    ../MetaData/common_data.py

*** Variables ***
${VAR_INTERFACE}    ${Interface}
${VAR_UPDATE_TYPE}    ${UpdateType}
${VAR_FILE_TYPE}    ${FileType}

*** Test Cases ***
MT_FU_HDL-RS232-STD
    [Documentation]    Running HDL
    Execute HDL    ${VAR_INTERFACE}.rs232std_index    ${VAR_UPDATE_TYPE}.upgrade_index
    ...     ${VAR_FILE_TYPE}.apponly_index    DR9401653    DR9401661
    ...     D:${/}tmp${/}CE_Release


