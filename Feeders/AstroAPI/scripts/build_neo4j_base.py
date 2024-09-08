#!/usr/bin/env python3

#// Step 1: Create Astrological Sign Nodes
#// Create each sign node, providing its name and common attributes like element and modality.

#CREATE (a:Sign {name: 'Aries', element: 'Fire', modality: 'Cardinal'})
#CREATE (t:Sign {name: 'Taurus', element: 'Earth', modality: 'Fixed'})
#CREATE (g:Sign {name: 'Gemini', element: 'Air', modality: 'Mutable'})
#CREATE (c:Sign {name: 'Cancer', element: 'Water', modality: 'Cardinal'})
#CREATE (l:Sign {name: 'Leo', element: 'Fire', modality: 'Fixed'})
#CREATE (v:Sign {name: 'Virgo', element: 'Earth', modality: 'Mutable'})
#CREATE (lb:Sign {name: 'Libra', element: 'Air', modality: 'Cardinal'})
#CREATE (sc:Sign {name: 'Scorpio', element: 'Water', modality: 'Fixed'})
#CREATE (sa:Sign {name: 'Sagittarius', element: 'Fire', modality: 'Mutable'})
#CREATE (cp:Sign {name: 'Capricorn', element: 'Earth', modality: 'Cardinal'})
#CREATE (aq:Sign {name: 'Aquarius', element: 'Air', modality: 'Fixed'})
#CREATE (pi:Sign {name: 'Pisces', element: 'Water', modality: 'Mutable'})

#// These queries create the 12 astrological signs as nodes with attributes like 'element' and 'modality'.

#// Step 2: Create Planet Nodes
#// Create nodes for each planet with relevant properties.

#CREATE (sun:Planet {name: 'Sun', type: 'Luminary'})
#CREATE (moon:Planet {name: 'Moon', type: 'Luminary'})
#CREATE (mercury:Planet {name: 'Mercury', type: 'Personal'})
#CREATE (venus:Planet {name: 'Venus', type: 'Personal'})
#CREATE (mars:Planet {name: 'Mars', type: 'Personal'})
#CREATE (jupiter:Planet {name: 'Jupiter', type: 'Social'})
#CREATE (saturn:Planet {name: 'Saturn', type: 'Social'})
#CREATE (uranus:Planet {name: 'Uranus', type: 'Outer'})
#CREATE (neptune:Planet {name: 'Neptune', type: 'Outer'})
#CREATE (pluto:Planet {name: 'Pluto', type: 'Outer'})
#CREATE (chiron:Planet {name: 'Chiron', type: 'Asteroid'})
#CREATE (lilith:Planet {name: 'Lilith', type: 'Asteroid'})

#// These queries create all the major celestial bodies including personal planets, outer planets, and asteroids.

#// Step 3: Create Astrological House Nodes
#// Create nodes for each house (1st through 12th) with their number as a property.

#CREATE (h1:House {number: 1})
#CREATE (h2:House {number: 2})
#CREATE (h3:House {number: 3})
#CREATE (h4:House {number: 4})
#CREATE (h5:House {number: 5})
#CREATE (h6:House {number: 6})
#CREATE (h7:House {number: 7})
#CREATE (h8:House {number: 8})
#CREATE (h9:House {number: 9})
#CREATE (h10:House {number: 10})
#CREATE (h11:House {number: 11})
#CREATE (h12:House {number: 12})

#// These nodes represent the 12 houses in astrology, with each house having a unique number.

#// Step 4: Create Asteroid Nodes
#// Create asteroid nodes with relevant properties.

#CREATE (ceres:Asteroid {name: 'Ceres'})
#CREATE (pallas:Asteroid {name: 'Pallas Athena'})
#CREATE (juno:Asteroid {name: 'Juno'})
#CREATE (vesta:Asteroid {name: 'Vesta'})

#// These nodes represent asteroids that are important in astrological analysis.

#pip install py2neo

from py2neo import Graph

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "your_password"))

# Step 1: Create Signs Nodes
def create_signs():
	signs = [
		{'name': 'Aries', 'element': 'Fire', 'modality': 'Cardinal'},
		{'name': 'Taurus', 'element': 'Earth', 'modality': 'Fixed'},
		{'name': 'Gemini', 'element': 'Air', 'modality': 'Mutable'},
		{'name': 'Cancer', 'element': 'Water', 'modality': 'Cardinal'},
		{'name': 'Leo', 'element': 'Fire', 'modality': 'Fixed'},
		{'name': 'Virgo', 'element': 'Earth', 'modality': 'Mutable'},
		{'name': 'Libra', 'element': 'Air', 'modality': 'Cardinal'},
		{'name': 'Scorpio', 'element': 'Water', 'modality': 'Fixed'},
		{'name': 'Sagittarius', 'element': 'Fire', 'modality': 'Mutable'},
		{'name': 'Capricorn', 'element': 'Earth', 'modality': 'Cardinal'},
		{'name': 'Aquarius', 'element': 'Air', 'modality': 'Fixed'},
		{'name': 'Pisces', 'element': 'Water', 'modality': 'Mutable'}
	]
	# Run Cypher query to create nodes for each sign
	for sign in signs:
		graph.run("""
			CREATE (s:Sign {name: $name, element: $element, modality: $modality})
		""", parameters=sign)
		
# Step 2: Create Planet Nodes
def create_planets():
	planets = [
		{'name': 'Sun', 'type': 'Luminary'},
		{'name': 'Moon', 'type': 'Luminary'},
		{'name': 'Mercury', 'type': 'Personal'},
		{'name': 'Venus', 'type': 'Personal'},
		{'name': 'Mars', 'type': 'Personal'},
		{'name': 'Jupiter', 'type': 'Social'},
		{'name': 'Saturn', 'type': 'Social'},
		{'name': 'Uranus', 'type': 'Outer'},
		{'name': 'Neptune', 'type': 'Outer'},
		{'name': 'Pluto', 'type': 'Outer'},
		{'name': 'Chiron', 'type': 'Asteroid'},
		{'name': 'Lilith', 'type': 'Asteroid'}
	]
	# Run Cypher query to create nodes for each planet
	for planet in planets:
		graph.run("""
			CREATE (p:Planet {name: $name, type: $type})
		""", parameters=planet)
		
# Step 3: Create House Nodes
def create_houses():
	for i in range(1, 13):
		graph.run("CREATE (h:House {number: $number})", parameters={'number': i})
		
# Step 4: Create Asteroid Nodes
def create_asteroids():
	asteroids = [
		{'name': 'Ceres'},
		{'name': 'Pallas Athena'},
		{'name': 'Juno'},
		{'name': 'Vesta'}
	]
	for asteroid in asteroids:
		graph.run("CREATE (a:Asteroid {name: $name})", parameters=asteroid)
		
# Main function to run all steps
if __name__ == "__main__":
	create_signs()
	create_planets()
	create_houses()
	create_asteroids()
	
	print("Astrological data successfully added to the database!")
	
# python build_neo4j_base.py