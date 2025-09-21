#!/bin/bash

git pull origin main
cd ./docker
docker compose down
docker rmi -f spectrum_app_image
docker compose up -d