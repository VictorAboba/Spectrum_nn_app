@echo off
cls

cd /d "%~dp0"
cd docker

echo Остановка контейнеров...
docker compose down

pause