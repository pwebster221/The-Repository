#!/usr/bin/env python3

# python script to calculate aspects from single date

def calculate_aspects(positions):
	aspects = {
		"Conjunction": {"angle": 0, "orb": 8},
		"Opposition": {"angle": 180, "orb": 6},
		"Trine": {"angle": 120, "orb": 6},
		"Square": {"angle": 90, "orb": 6},
		"Sextile": {"angle": 60, "orb": 6},
		"Inconjunct": {"angle": 150, "orb": 4}
	}
	
	aspect_results = []
	planets = list(positions.keys())
	
	for i in range(len(planets)):
		for j in range(i + 1, len(planets)):
			planet1 = planets[i]
			planet2 = planets[j]
			
			longitude1 = positions[planet1][0]
			longitude2 = positions[planet2][0]
			speed1 = positions[planet1][3]
			speed2 = positions[planet2][3]
			
			angle_difference = abs(longitude1 - longitude2)
			if angle_difference > 180:
				angle_difference = 360 - angle_difference
				
			for aspect, data in aspects.items():
				orb = abs(angle_difference - data["angle"])
				if orb <= data["orb"]:
					applying = "applying" if speed1 > speed2 else "fading"
					aspect_results.append({
						"planet1": planet1,
						"planet2": planet2,
						"aspect": aspect,
						"angle": angle_difference,
						"orb": orb,
						"applying": applying
					})
					
	return aspect_results

# calculating aspects between two different querries

def calculate_aspects_between_instances_all_planets(positions1, positions2):
	aspects = {
		"Conjunction": {"angle": 0, "orb": 8},
		"Opposition": {"angle": 180, "orb": 6},
		"Trine": {"angle": 120, "orb": 6},
		"Square": {"angle": 90, "orb": 6},
		"Sextile": {"angle": 60, "orb": 6},
		"Inconjunct": {"angle": 150, "orb": 4}
	}
	
	aspect_results = []
	planets1 = list(positions1.keys())
	planets2 = list(positions2.keys())
	
	for planet1 in planets1:
		for planet2 in planets2:
			longitude1 = positions1[planet1][0]
			longitude2 = positions2[planet2][0]
			speed1 = positions1[planet1][3]
			speed2 = positions2[planet2][3]
			
			angle_difference = abs(longitude1 - longitude2)
			if angle_difference > 180:
				angle_difference = 360 - angle_difference
				
			for aspect, data in aspects.items():
				orb = abs(angle_difference - data["angle"])
				if orb <= data["orb"]:
					applying = "applying" if speed1 > speed2 else "fading"
					aspect_results.append({
						"planet1": planet1,
						"planet2": planet2,
						"aspect": aspect,
						"angle": angle_difference,
						"orb": orb,
						"applying": applying
					})
					
	return aspect_results