@echo off
title FastAPI Server - DO NOT CLOSE THIS WINDOW
color 0A
echo ========================================
echo   FASTAPI SERVER STARTING...
echo   (env vars are set for this session only)
echo ========================================
echo.
cd /d "%~dp0"

:: --- AI keys for this session (do NOT commit secrets to git) ---
:: Replace the placeholder value with your actual OpenRouter key.
:: This stays only in this window's process; it is not system-wide.
set "OPENROUTER_API_KEY=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"

:: Optional: set other AI keys when you get them
set "GEMINI_API_KEY=AIzaSyCD8SpDPh_E-mAudyEkWe3XYSbnbFCVhi4"
set "MISTRAL_API_KEY=Uonls2JriUbJAezqa5415crAhcebOxEW"

python api.py
pause
