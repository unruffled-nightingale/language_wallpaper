Set WshShell = CreateObject("WScript.Shell")

Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")

Dim filepath
filepath = fso.GetAbsolutePathName(".") & "\run.py"

WshShell.Run "cmd /c python " & filepath, 0
