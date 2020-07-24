import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine('sqlite:///Resources/hawaii.sqlite', echo=False)

# Declare a Base using `automap_base()`
auto = automap_base()
# reflect the tables
auto.prepare(engine, reflect=True)

# Save a reference to the measurenment table as 'Measurement'
measurement = auto.classes.measurement
station = auto.classes.station

# Create our session (link) from Python to the DB
#session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        "Hawaii Precipitation and Weather Data<br/><br/>"
        "Pick from the available routes below:<br/><br/>"
        "Precipiation from 2016-08-23 to 2017-08-23.<br/>"
        "/api/v1.0/precipitation<br/><br/>"
        "A list of all the weather stations in Hawaii.<br/>"
        "/api/v1.0/stations<br/><br/>"
        "The Temperature Observations (tobs) from 2016-08-23 to 2017-08-23.<br/>"
        "/api/v1.0/tobs<br/><br/>"
        "Type in a single date (i.e., 2015-01-01) to see the min, max and avg temperature since that date.<br/>"
        "/api/v1.0/temp/<start><br/><br/>"
        "Type in a date range (i.e., 2015-01-01/2015-01-10) to see the min, max and avg temperature for that range.<br/>"
        "/api/v1.0/temp/<start>/<end><br/>"
    )

@app.route("/api/v1.0/tobs")

def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of dates and prcp"""
    # Query all dates and prcp
    results = session.query(measurement.date, measurement.prcp).\
                        filter(measurement.date > begin_date).\
                        order_by(measurement.date).all()

def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(station).all()
    
    return jsonify(results)

def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(measurement.tobs).all()
    
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
