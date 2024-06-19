*** Settings ***
Resource    ../Resource/ExecuteHDL.resource
Resource    ../Resource/Verify.resource

*** Variables ***


*** Test Cases ***
MT_FU_HDL-RS232-STD
    [Documentation]    Running HDL
    Execute HDL    RS232-STD    DR9401653    DR9401661    AppOnly    Upgrade    D:\tmp\CE_Release