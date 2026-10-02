@echo off

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Creating Python virtual environment...
    py -3 -m venv .venv
)

call .venv\Scripts\activate

echo Running NopCommerce login test...
python -m pytest -v -s TestCases/test_login.py

exit /b %ERRORLEVEL%