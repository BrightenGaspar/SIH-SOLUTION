@echo off
echo ========================================================
echo   SIH TELEMETRY COMMAND CENTER - QUICK LAUNCHER
echo ========================================================
echo Installing required dependencies...
pip install -r requirements.txt
echo.
echo Starting FastAPI Real-Time Backend on http://127.0.0.1:8000 ...
start http://127.0.0.1:8000
python server.py
pause
