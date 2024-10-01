Overview
In this project, I analyzed weather data using SQLAlchemy for database management, Pandas for data manipulation, and Matplotlib for visualization. My objective was to retrieve and explore weather data from the past year stored in a SQLite database, generate statistics, and visualize temperature and precipitation patterns.

For Part 2, I extended the project by building a Flask API to expose the weather data and make it accessible via different routes.

Key Features:
I retrieved the last 12 months of precipitation data and visualized it.
I analyzed the most active weather station and extracted key temperature metrics.
I generated statistical summaries of the precipitation data.
I plotted histograms of temperature data for the most active weather stations.
I performed SQL queries on a weather dataset using SQLAlchemy.

Part 2: I built a Flask API to expose weather data via several routes.

Tools and Libraries I Used

SQLAlchemy: Python SQL toolkit and Object Relational Mapper.
Pandas: Data manipulation and analysis library.
Matplotlib: Python library for creating static, animated, and interactive visualizations.
NumPy: Library for numerical computing with Python.
Flask: Web framework to build APIs.
Datetime: Library for manipulating dates and times.

Project Structure

Weather Data Analysis Project/
├── README.md                # This file

├── climate_starter.ipynb     # Jupyter Notebook containing the analysis

├── app.py                   # Flask application for Part 2

├── resources/               # Folder containing data
│   └── hawaii.sqlite        # SQLite database file containing weather data

├── templates/               # Folder containing HTML templates for the web interface
│   └── index.html           # HTML file for the main page of the Flask app

├── static/                  # Folder containing static files (CSS, JS)
│   └── css/
│       └── style.css        # Custom CSS file for styling the HTML page

Part 1: Weather Data Analysis
In the first part of the project, I used the weather data stored in the SQLite database to perform various analyses and visualizations.

Analysis Workflow
Setting Up the Database Connection
I used SQLAlchemy to connect to the SQLite database, reflect the tables into Python classes, and start a session to query the data.

Retrieving the Last 12 Months of Precipitation Data
I found the most recent date in the Measurement table and calculated the date one year before. I then extracted precipitation data for the last 12 months and plotted it to visualize rainfall over this period.

Calculating the Total Number of Stations
I queried the Station table to calculate how many stations were available in the dataset.

Identifying the Most Active Stations
I performed a query to find the station with the highest number of measurements and listed the station IDs and their counts in descending order.

Temperature Analysis for the Most Active Station
For the most active station, I calculated the lowest, highest, and average temperatures. I retrieved the last 12 months of temperature observation data and plotted a histogram of temperature values.

Part 2: Flask API Creation
In the second part of the project, I built a Flask API to make the weather data available via different routes. This allows the data to be programmatically accessed and used in other applications.

API Endpoints

/
This is the homepage, where I listed all the available API routes.
The HTML file index.html in the templates folder is rendered here to provide a clean user interface to navigate the API.

/api/v1.0/precipitation
This route returns the last 12 months of precipitation data as a JSON dictionary, with the date as the key and the precipitation value as the value.

/api/v1.0/stations
This route returns a JSON list of all weather stations in the dataset.

/api/v1.0/tobs
This route returns the temperature observations (TOBS) of the most active station for the last 12 months.

/api/v1.0/<start>
This route returns the minimum, average, and maximum temperatures for all dates greater than or equal to the specified start date, which should be provided in the format YYYY-MM-DD.

/api/v1.0/<start>/<end>
This route returns the minimum, average, and maximum temperatures for the date range between the specified start and end dates (inclusive), both of which should be in the format YYYY-MM-DD.

Flask App Structure
app.py:
I wrote this file to set up the Flask app, define the routes, and handle database queries. SQLAlchemy was used to connect to the SQLite database, and the Flask jsonify function was used to return the query results in JSON format.

index.html:
This file serves as the homepage for the API. It was built with HTML and styled using the CSS file located in static/css/style.css. The page lists all the available routes with clickable links for easy navigation.

style.css:
I used this file to customize the styles for the HTML page. It enhances the appearance of the web interface and makes it more user-friendly and visually appealing.

How to Run the Project
-Clone the repository to your local machine.
-Set up a Python virtual environment and install the required dependencies by running:
-bash
-Copy code

Open the hawaii.sqlite database located in the resources folder using SQLite or a similar tool.
To perform the data analysis, open and run the climate_starter.ipynb Jupyter notebook.
To start the Flask API, navigate to the project directory and run the following command:
bash
Copy code
python app.py
Go to http://127.0.0.1:5000/ in your web browser to access the homepage of the API.

Conclusion
Through this project, I was able to analyze weather patterns using historical data, employing SQLAlchemy for efficient database interaction, Pandas for data manipulation, and Matplotlib for visualization. By extending the project with a Flask API, I made the weather data easily accessible through different endpoints, allowing it to be used in other applications.
