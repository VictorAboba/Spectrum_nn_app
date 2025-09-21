@echo off
cls

cd /d "%~dp0"
cd docker

echo Остановка контейнеров и удаление образов...
docker compose down
docker rmi -f spectrum_app_image

pause