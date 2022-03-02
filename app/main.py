from flask import Flask, request, jsonify, Response
import numpy as np
from app.utils.logger import SetUpLogging
import logging
from flask_apscheduler import APScheduler
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

class Config:
    """App configuration."""
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = "Utc" 

# LOGGER
SetUpLogging().setup_logging()

# APP
app = Flask(__name__)
app.config.from_object(Config())

# INIT SCHEDULER
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

loaded_model = None

# SCHEDULER
@scheduler.task('interval', id='training', minutes=10)
def trainingJob():
    try:
        logging.info("TESTING SUCCESS")
        return str("Success")
    except Exception as e:
        logging.warning("TESTING FAILED " + str(e))
        return str(e)

# REST API SCHEDULER
@app.route('/modifyTrainingJob', methods=['GET','POST'])
def modifyTrainingJob():
    param = request.json
    try:
        scheduler.modify_job('training', **param)
        return str(scheduler.get_job('training'))
    except Exception as e:
        return str(e)

@app.route('/getTrainingJob', methods=['GET'])
def getTrainingJob():
    return str(scheduler.get_job('training'))

@app.route('/pauseTrainingJob', methods=['GET'])
def pauseTrainingJob():
    scheduler.pause_job('training')
    return str(scheduler.get_job('training'))

@app.route('/resumeTrainingJob', methods=['GET'])
def resumeTrainingJob():
    scheduler.resume_job('training')
    return str(scheduler.get_job('training'))

# CHECKING
@app.route('/', methods=['GET'])
def testReturn():
    return str("FLASK APS SCHEDULER WITH LOGGING")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)