# PM2.5 Prediction Server
This repository includes all the programs to be run on Synology NAS, along with docker setting files. This includes : 
* server - This is the server that receives data sent by the sensors and saves into the database (mongoDB).
* http_server - This is the server that handles http request from the mobile app, retrieves the requested data from mongoDB and sends back to the users.

## Requirements
Docker

## How to turn on servers and mongodb
1. ssh to the machine and sudo -i
2. navigate to volumes1/docker/server
3. docker-compose up --build --force-recreate -d

## run pylint
navigate to project directory and input pylint **/*.py

## check logs
docker-compose logs
