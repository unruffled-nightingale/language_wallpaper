rem Get the time in one minute.

SET filepath=%~dp0run_language_wallpaper.bat

rem Scheduler task to run every time the computer starts up

schtasks /create /tn language_wallpaper /tr %filepath% /sc ONSTART /F
