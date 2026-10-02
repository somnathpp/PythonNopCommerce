@echo off

cd /d "%~dp0"

call .venv\Scripts\activate

python -m pytest -v -s TestCases/test_login.py

pause