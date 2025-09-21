@echo off
cls

cd /d "%~dp0"
cd docker

echo Сборка/Запуск контейнеров...
docker compose up -d

pause