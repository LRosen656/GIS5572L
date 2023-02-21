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
  cursor.execute("SELECT json_build_object('type', 'Feature', \
                 'id', gid, \
                 'geometry', ST_AsGeoJSON(geom)::json, \
                 'properties', json_build_object('feat_type', feat_type,'feat_area', ST_Area(geom)::geography))\
                 FROM table_poly;")
  result = cursor.fetchall()
  conn.close()
  return result[0][0]

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
