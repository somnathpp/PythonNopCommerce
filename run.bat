

@echo off

cd /d E:\Projects\opcommerce

call .venv\Scripts\activate

pytest -v -s -m sanity --html=Reports\report.html TestCases/  

pause