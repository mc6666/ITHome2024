@echo off　

if "%1" == "st" goto a0
if "%1" == "s" goto a1
if "%1" == "r" goto a2
if "%1" == "mk" goto a3
if "%1" == "m" goto a4
if "%1" == "i" goto a5
if "%1" == "re" goto a6
if "%1" == "g" goto a7
if "%1" == "d" goto a8
if "%1" == "c" goto a9
if "%1" == "sync" goto a10
if "%1" == "super" goto a11
if "%1" == "shell" goto a12

rem shell、inspectdb
if NOT "%1" == "" goto a99
goto end

:a0
python manage.py startapp %2
goto end

:a1
python -m SimpleHTTPServer
goto end

:a2
call run.bat runserver
goto end

:a3
call run.bat makemigrations %2
goto end

:a4
call run.bat migrate
goto end

:a5
pip install "%1"
goto end

:a6
pip install -r requirements.txt
goto end

:a7
python manage.py inspectdb > models.py
goto end

:a8
call run.bat check --deploy
goto end

:a9
call run.bat collectstatic
goto end

:a10
call run.bat syncdb
goto end

:a11
call run.bat createsuperuser
goto end

:a12
python manage.py shell
goto end


:a99
call run.bat %1 %2
goto end


:end
