*** Settings ***
Resource    ../Resource/ExecuteHDL.resource

*** Variables ***


*** Test Cases ***
MT_FU_HDL-RS232-STD
    [Documentation]    Running HDL
    Execute HDL    RS232-STD    DR9401653    DR9401661    AppOnly    1    D:${/}tmp${/}CE_Release