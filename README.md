# PM2.5 Prediction Server
This is a program that receives data sent by the sensors and saves into the database (mongoDB).


# How to turn on both server and mongodb
1. ssh to the machine and sudo -i
2. navigate to volumes1/docker/server
3. docker-compose up --force-recreate -d

# run pylint
navigate to project directory and input pylint **/*.py