from datetime import datetime, timedelta
from flask import jsonify, current_app
from errors import QueryNotFound

# Get the most recent data in the given position
# pos : The ID of the sensor to be queried
# Return value : The jsonified data that is ready to be sent, 404 if any error occured
def get_recent_data(pos, upper, lower):
    try:
        from flask_server import MONGO
        current_app.logger.info(upper)
        current_app.logger.info(lower)
        target_data = MONGO.db.pm_data
        # Find data between lower bound time and upper bound time
        return_data = list(target_data.find({
                '$and': [
                    {
                        'position': pos
                    },
                    {
                        'date': {
                            '$gte': lower,
                            '$lte': upper
                        }
                    }
                ]
        }))
        # How many documents in this query
        data_count = len(return_data)
        current_app.logger.info(data_count)
        if data_count == 0:
            raise QueryNotFound
        sum_pm25 = sum_temp = sum_humidity = 0
        for doc in return_data:
            sum_pm25 += doc.get('pm25', 0)
            sum_temp += doc.get('temp', 0)
            sum_humidity += doc.get('humidity', 0)
        return {
            'avg_pm25': (sum_pm25 / data_count),
            'avg_temp': (sum_temp / data_count),
            'avg_humidity': (sum_humidity / data_count)
        }
    except QueryNotFound as err:
        current_app.logger.info(err)
        result = str(err)
        return result, 404


def get_time_limit():
    half = timedelta(minutes=30)
    cur = datetime(2019, 3, 23, 1, 29, 23)
    # Determine which interval cur is currently in
    # 0 ~ 29 or 30 ~ 59
    if cur.minute < 30:
        time_d = timedelta(minutes=cur.minute, seconds=cur.second)
    else:
        time_d = timedelta(minutes=(cur.minute - 30), seconds=cur.second)
    upper = cur - time_d
    lower = cur - time_d - half
    return upper, lower
