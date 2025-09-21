#!/bin/bash

cd ./docker
docker compose down
docker rmi -f spectrum_app_image