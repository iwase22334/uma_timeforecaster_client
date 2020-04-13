import os
import requests
import json

class TimeForecaster:
    def __init__(self):
        self.__server_url = os.environ['TIME_FORECASTER_URL']

    @classmethod
    def __generate_query_tansyo(cls, id):
        query = '{ "race_id": { "year":"%s", "monthday":"%s", "jyocd":"%s", "kaiji":"%s", "nichiji":"%s", "racenum":"%s" } }' % (id)
        return query.strip()

    # @param id [ 'year', 'monthday', 'jyocd', 'kaiji', 'nichiji', 'racenum']
    def estimate(self, id):

        query = TimeForecaster.__generate_query_tansyo(id)
        r = requests.post(self.__server_url, query)

        if r.status_code == 200:
            body = json.loads(r.text)
            return body['tansyo']

        else:
            body = json.loads(r.text)
            raise RuntimeError("TimeForecaster server says: %s" % (body["error"],))
