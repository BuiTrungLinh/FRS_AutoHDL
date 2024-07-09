*** Settings ***
Library    ../Library/verification.py

*** Variables ***

*** Keywords ***
Verify HDL
    [Arguments]
    FOR    ${item1}    IN    @{li}
        List Should Contain Value  ${lj}  ${item1}
    END