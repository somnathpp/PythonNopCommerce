@echo off

cd /d "%~dp0"


echo Running NopCommerce login test...
python -m pytest -v -s TestCases/test_login.py

exit /b %ERRORLEVEL%