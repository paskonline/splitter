@echo off

REM 1. Set the folder as System/Read-only (Required for icon to show)
attrib +r .

REM 2. Hide the icon and config file so users don't see them
attrib +h +s exl.ico
attrib +h +s desktop.ini

echo Starting Spreadsheet Splitter...
python Spreadsheet_Splitter.py
pause
