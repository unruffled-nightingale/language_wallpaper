rem SETUP SCHEDULE TO RUN DAILY

schtasks /create /tn language_wallpaper /tr C:\Users\User\PycharmProjects\language_wallpaper\run_language_wallpaper.bat /sc ONCE /st 13:02 /F