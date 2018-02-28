rem Get the filepath for run.vbs

SET filepath=%~dp0run.vbs

rem Execute the script

"%filepath%"

rem Schedule run.vbs to run on startup

schtasks /create /tn language_wallpaper /tr %filepath% /sc ONSTART /F
