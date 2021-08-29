rmdir /s/q .\dist\main
D:\Python\python38\python.exe -m PyInstaller main.spec
copy .\ocr_labels.csv .\dist\main\
copy .\single_mode_choices.csv .\dist\main\
copy .\single_mode_races.jsonl .\dist\main\
copy .\pyrightconfig.csv .\dist\main\
copy .\version .\dist\main\
xcopy .\auto_derby\templates .\dist\main\auto_derby\templates\ /s /f /h
xcopy ..\ok-derby-frontend\dist .\dist\main\frontend\dist\ /s /f /h
md .\dist\main\log
REM .\dist\main\main.exe