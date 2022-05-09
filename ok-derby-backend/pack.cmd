rmdir /s/q .\dist\main
D:\Python\python38\python.exe -m PyInstaller main.spec
xcopy .\auto_derby\templates .\dist\main\auto_derby\templates\ /s /f /h
xcopy .\auto_derby\data .\dist\main\auto_derby\data\ /s /f /h
xcopy .\auto_derby\web\dist .\dist\main\auto_derby\web\dist /s /f /h
xcopy .\data .\dist\main\data\ /s /f /h
xcopy ..\ok-derby-frontend\dist .\dist\main\frontend\dist\ /s /f /h
md .\dist\main\log