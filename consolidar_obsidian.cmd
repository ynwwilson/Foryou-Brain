@echo off
REM consolidar_obsidian.cmd
REM Roda o script de consolidação com modelo barato (Haiku)
REM Configurado via Task Scheduler para rodar todo dia às 03:00

REM Força modelo barato — nunca herda config cara do ambiente pai
set ANTHROPIC_MODEL=claude-haiku-4-5-20251001

REM Caminho do Python — ajuste se necessário
set PYTHON=python

REM Caminho do script
set SCRIPT=C:\Users\ynwwi\Projects\jarvis\stark\Stark\consolidar_obsidian.py

REM Roda o script
%PYTHON% "%SCRIPT%"
