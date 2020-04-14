#!/usr/bin/env python3

import json
import psycopg2
import os
import sys
import timeforecaster

query = '''SELECT year, monthday, jyocd, kaiji, nichiji, racenum \
from n_race \
where concat(year, monthday) > '20000000' and datakubun='7' \
order by year asc, monthday asc, jyocd asc, kaiji asc, nichiji asc, racenum asc limit 1'''.strip()

try:
    connection= psycopg2.connect(os.environ.get('DATABASE_URL_SRC'))
except Exception as e:
    print('psycopg2: opening connection 01 faied: %s' % e)
    sys.exit(0)

with connection.cursor() as cur:
    cur.execute(query)
    id = cur.fetchone()

connection.close()

estimator = timeforecaster.TimeForecaster()
res = estimator.estimate(id)
print(json.dumps(res))

