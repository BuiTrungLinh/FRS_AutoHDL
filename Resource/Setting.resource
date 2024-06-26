*** Settings ***
Library     ../Library/setting.py

*** Variables ***

*** Keywords ***
Setting Before Running
    [Documentation]     Before running HDL, need to erase log and statistics, clear ule, clear customdata, bla bla
    Prepare Before

Setting After Running
    [Documentation]     After running HDL, set the scanner to the original settings
    Prepare Teardown