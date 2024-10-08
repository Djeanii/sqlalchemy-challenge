# Import the dependencies
import numpy as np
import pandas as pd
from datetime import datetime as dt, timedelta
from flask import Flask, jsonify, render_template, abort
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Home route to list all available routes
@app.route("/")
def welcome():
    return render_template('index.html')

# Precipitation route to retrieve last 12 months of data
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last 12 months as a JSON."""
    
    # Create session
    session = Session(engine)

    # Find the most recent date in the dataset
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latest_date = dt.strptime(latest_date, "%Y-%m-%d")
    
    # Calculate the date one year ago from the latest date
    one_year_ago = latest_date - timedelta(days=365)
    
    # Query for the precipitation data in the last 12 months
    precip_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    
    session.close()
    
    # Convert the query results to a dictionary {date: prcp}
    precip_dict = {date: prcp for date, prcp in precip_data}
    
    return jsonify(precip_dict)

# Stations route to return a list of all weather stations
@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of weather stations."""
    
    # Create session
    session = Session(engine)
    
    # Query for all stations in the dataset
    results = session.query(Station.station).all()
    
    session.close()
    
    # Unpack the results into a list
    stations_list = [station[0] for station in results]
    
    return jsonify(stations_list)

# Temperature observations route for the most active station in the past year
@app.route("/api/v1.0/tobs")
def temperature_observations():
    """Return the temperature observations for the most active station in the past year."""
    
    # Create session
    session = Session(engine)
    
    # Identify the most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]
    
    # Calculate the date one year ago from the latest date
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latest_date = dt.strptime(latest_date, "%Y-%m-%d")
    one_year_ago = latest_date - timedelta(days=365)
    
    # Query for temperature observations from the most active station
    temp_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()
    
    session.close()
    
    # Convert the query results into a list of dictionaries
    temperature_list = [{"date": date, "tobs": tobs} for date, tobs in temp_data]
    
    return jsonify(temperature_list)

# Start route to calculate TMIN, TAVG, TMAX for all dates >= start
@app.route("/api/v1.0/<start>")
def start_date(start):
    """Return TMIN, TAVG, TMAX for all dates greater than or equal to the start date."""
    
    try:
        # Convert the start date to a datetime object
        start_date = dt.strptime(start, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    
    # Create session
    session = Session(engine)
    
    # Query for TMIN, TAVG, TMAX for all dates >= start date
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    
    session.close()
    
    # Unpack the query results
    tmin, tavg, tmax = temp_stats[0]
    
    return jsonify({"Start Date": start, "TMIN": tmin, "TAVG": tavg, "TMAX": tmax})

# Start/End route to calculate TMIN, TAVG, TMAX for all dates between start and end
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return TMIN, TAVG, TMAX for dates between the start and end date."""
    
    try:
        # Convert start and end dates to datetime objects
        start_date = dt.strptime(start, "%Y-%m-%d")
        end_date = dt.strptime(end, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    
    # Create session
    session = Session(engine)
    
    # Query for TMIN, TAVG, TMAX for dates between start and end
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    
    session.close()
    
    # Unpack the query results
    tmin, tavg, tmax = temp_stats[0]
    
    return jsonify({"Start Date": start, "End Date": end, "TMIN": tmin, "TAVG": tavg, "TMAX": tmax})

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
