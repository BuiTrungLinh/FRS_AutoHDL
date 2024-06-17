*** Settings ***
Resource    Resource/ExecuteHDL.resource
Resource    Resource/Verify.resource

*** Variables ***

*** Test Cases ***
MT_FU_HDL-RS232-STD-AppOnly-Upgrade-From Beta RC6 DR9401653 to Beta RC8 DR9401661
    Execute HDL
    VerifyHDL