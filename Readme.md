# Flask Gunicorn Nginx APS Scheduler Docker Compose

## Overview
This script will run Job Scheduler for every 10 minutes (default, can be changed via Rest API or directly in code), and then will log info "TESTING SUCCESS" in log file created in this dir, called logs.log, this log can be seen within exec through docker flask image or seen directly in your directory. 

## Run

```
docker-compose up -d --build
```

## Rest API

```
GET localhost:5001/getTrainingJob
```
- Return the next job scheduler, default : every 10 minutes. 

<br/>

```
GET localhost:5001/pauseTrainingJob
```
- Pause job scheduler.

<br/>

```
GET localhost:5001/resumeTrainingJob
```
- Resume job scheduler.

<br/>

```
POST localhost:5001/modifyTrainingJob
```
- Modify job scheduler. 
- Example Body (Change to interval 5 Minutes) :
```
{
    "trigger" : "interval",
    "seconds" : 0,
    "minutes" : 5,
    "hours" : 0
    }
```


## Further Improvement
any improvement from each FlaskAPSScheduler API (add job, crontab, etc) can be seen in this link : 

https://viniciuschiele.github.io/flask-apscheduler/index.html

and you can edit or change code in main.py

