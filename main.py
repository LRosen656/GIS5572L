import os
import sqlalchemy
import numpy
import psycopg2
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "This website is working!"


@app.route("/ffc")
def get_polygon():
  conn = psycopg2.connect(host = '34.171.19.177', database = 'lab1', user = 'postgres', password = 'starman1')
  cursor = conn.cursor()
  cursor.execute("SELECT ST_AsGeoJSON(geom) FROM table_poly;")
  result = cursor.fetchall()
  conn.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
