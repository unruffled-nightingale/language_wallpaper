rem Get the time in one minute.

SET filepath=%~dp0run.bat

rem Scheduler task to run every time the computer starts up

schtasks /create /tn language_wallpaper /tr %filepath% /sc ONSTART /F
