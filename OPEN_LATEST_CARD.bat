@echo off
set "CARD=D:\QMT\_OUTPUT\MARKET_MAINLINE\MAINLINE_V33_SHSZ\LATEST_MARKET_CARD.html"
if exist "%CARD%" (
  start "" "%CARD%"
  exit /b 0
)
echo V3.3 card not found. Run the original mainline BAT first.
pause
