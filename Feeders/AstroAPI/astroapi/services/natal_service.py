# part one, query planetary positions for date of birth based on user input

import swisseph as swe
from datetime import datetime
from astroapi.config import SWISSEPH_PATH
from geopy.geocoders import Nominatim

# Set the path to the Swiss Ephemeris files
swe.set_ephe_path(SWISSEPH_PATH)

# Function to get the position of a planet on a given date and time
def get_planet_position(julian_day, planet):
	# Calculate the position of the planet
	planet_position = swe.calc_ut(julian_day, planet)
	longitude, latitude, distance, speed_longitude, speed_latitude, speed_distance = planet_position
	
	return {
		"longitude": longitude,
		"latitude": latitude,
		"distance": distance,
		"speed_longitude": speed_longitude
	}
	
# Function to get positions for a list of planets
def get_positions_for_date(julian_day, planets):
	positions = {}
	for planet in planets:
		positions[swe.get_planet_name(planet)] = get_planet_position(julian_day, planet)
	return positions

# Function to convert user input into a Julian day number
def convert_to_julian_day(year, month, day, hour, minute, latitude, longitude, timezone):
	# Adjust the time by the timezone offset
	utc_hour = hour - timezone
	# Calculate Julian day
	julian_day = swe.julday(year, month, day, utc_hour + minute / 60)
	return julian_day

# Function to get latitude and longitude from location name
def get_lat_lon(location_name):
	geolocator = Nominatim(user_agent="astroapi")
	location = geolocator.geocode(location_name)
	if location:
		return location.latitude, location.longitude
	else:
		raise ValueError("Location not found")
		
# Example usage
if __name__ == "__main__":
	# Get user input for date, time, and location
	date_input = input("Enter date (YYYY-MM-DD): ")
	time_input = input("Enter time (HH:MM in 24-hour format): ")
	location_input = input("Enter location (city, country): ")
	timezone_input = float(input("Enter time zone offset from UTC (e.g., -5 for EST): "))
	
	# Parse date and time
	year, month, day = map(int, date_input.split('-'))
	hour, minute = map(int, time_input.split(':'))
	
	# Get latitude and longitude for the location
	try:
		latitude, longitude = get_lat_lon(location_input)
	except ValueError as e:
		print(e)
		exit()
		
	# Convert to Julian day
	julian_day = convert_to_julian_day(year, month, day, hour, minute, latitude, longitude, timezone_input)
	
	# List of planets to query (Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto)
	planets = [swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS,
				swe.JUPITER, swe.SATURN, swe.URANUS, swe.NEPTUNE, swe.PLUTO]
	
	# Get positions for the given date and time
	planet_positions = get_positions_for_date(julian_day, planets)
	
	# Print the results
	for planet_name, position in planet_positions.items():
		print(f"{planet_name}: {position['longitude']}° longitude, {position['speed_longitude']}°/day speed")