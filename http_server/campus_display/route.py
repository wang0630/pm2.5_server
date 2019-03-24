from datetime import datetime, timedelta
from flask import Blueprint, request, current_app, jsonify
from .service import get_recent_data, get_time_limit

campus_display = Blueprint("campus_display", __name__, url_prefix="/campus")

@campus_display.route("/<int:campus_id>", methods=["GET"])
def get_partial_data(campus_id):
    try:
        upper, lower = get_time_limit()
        current_app.logger.info(campus_id)
        # Unpack the dict to pass it to the function
        return jsonify(**get_recent_data(campus_id, upper, lower))
    except AttributeError as err:
        current_app.logger.info(err)
        result = "The request may not have the header of application/json"
        return result, 400

@campus_display.route('/init/<int:campus_id>', methods=["GET"])
def init(campus_id):
    try:
        half = timedelta(minutes=30)
        upper, lower = get_time_limit()
        current_app.logger.info(campus_id)
        pm25 = []
        temp = []
        humidity = []
        # Get the data within 6 hours
        for i in range(12):
            data = get_recent_data(campus_id, upper - (half * i), lower - (half * i))
            current_app.logger.info(data)
            pm25.append(data.get('avg_pm25'))
            temp.append(data.get('avg_temp'))
            humidity.append(data.get('avg_humidity'))
        return jsonify(pm25List=pm25, tempList=temp, humidityList=humidity)
    except AttributeError as err:
        current_app.logger.info(err)
        result = "The request may not have the header of application/json"
        return result, 400
