#!/usr/bin/env python3

import swisseph as swe  # Swiss Ephemeris library
from datetime import datetime
import requests


# Step 2: Convert user input into usable form for Swiss Ephemeris
def convert_to_julian_day(birthdate, birthtime):
	"""
	Convert birthdate and birthtime into Julian Day, as required by the Swiss Ephemeris.
	birthdate: string in 'YYYY-MM-DD' format
	birthtime: string in 'HH:MM' format
	"""
	# Convert strings to datetime object
	birth_datetime = datetime.strptime(f"{birthdate} {birthtime}", "%Y-%m-%d %H:%M")
	
	# Extract individual components
	year = birth_datetime.year
	month = birth_datetime.month
	day = birth_datetime.day
	hour = birth_datetime.hour + birth_datetime.minute / 60.0  # Decimal hour
	
	# Convert to Julian Day using Swiss Ephemeris
	jd_ut = swe.julday(year, month, day, hour)  # Universal time in Julian Day
	return jd_ut

# Step 3: Query planetary positions from Swiss Ephemeris
def query_planetary_positions(julian_day, latitude, longitude):
	"""
	Query the positions of all major planets using Swiss Ephemeris.
	julian_day: Julian Day calculated from the birthdate and time
	latitude: latitude of the birth location
	longitude: longitude of the birth location
	"""
	# Initialize Swiss Ephemeris with the default data files
	swe.set_ephe_path("/path/to/ephemeris/files")  # Path to the Swiss Ephemeris data
	
	# List of planets to query
	planets = [swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS,
				swe.JUPITER, swe.SATURN, swe.URANUS, swe.NEPTUNE, swe.PLUTO]
	
	positions = {}  # Dictionary to store planet positions
	
	for planet in planets:
		# Query the planetary position for the specific Julian Day and location
		position, ret = swe.calc_ut(julian_day, planet)  # Use Universal Time (UT)
		
		# Return longitude, latitude, and distance of the planet
		positions[planet] = {
			'longitude': position[0],  # Longitude of the planet in degrees
			'latitude': position[1],   # Latitude (often 0 for most planets)
			'distance': position[2],   # Distance from Earth
			'retrograde': ret == swe.ERR  # Retrograde status (if ret = swe.ERR, it’s retrograde)
		}
		
	return positions

