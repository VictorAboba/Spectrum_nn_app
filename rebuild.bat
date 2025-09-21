@echo off
cls

cd /d "%~dp0"
echo Загрузка последней версии проекта...
git pull origin main

cd docker
echo Пересборка контейнеров...
docker compose down
docker rmi -f spectrum_app_image
docker compose up -d

pause