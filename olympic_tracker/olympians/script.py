import csv
import psycopg2
from django.db import models

conn = psycopg2.connect("host=localhost dbname=koroibos_drf user=tayjames")
cur = conn.cursor()
with open('olympians/data.csv', 'r') as f:
    # next(f)

# cur.copy_from(f, 'public.olympians_olympian', sep=",")
# conn.commit()



# # Notice that we don't need the `csv` module.
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    # breakpoint()
    for row in reader:
        # breakpoint()
        cur.execute("INSERT INTO public.olympians_olympian(name, sex, age, height, weight, team, games, sport, event, medal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
conn.commit()
