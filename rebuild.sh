#!/bin/bash

git pull origin main
cd ./docker
docker compose down
docker rmi spectrum_app_image:latest
docker compose up -d