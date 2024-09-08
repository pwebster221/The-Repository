# convert to sign/degree

def convert_to_sign_and_degree(longitude):
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    # Determine the sign and degree within the sign
    sign_index = int(longitude // 30)
    sign = signs[sign_index]
    degree = longitude % 30
    
    return sign, degree

def display_planetary_positions(positions):
    for planet_name, (longitude, latitude, distance) in positions.items():
        sign, degree = convert_to_sign_and_degree(longitude)
        print(f"{planet_name} - {sign} {degree:.2f}° | Longitude: {longitude:.6f}°, Latitude: {latitude:.6f}°, Distance: {distance:.6f} AU")

# display results

def display_aspects(positions, aspect_results):
    for aspect in aspect_results:
        planet1 = aspect['planet1']
        planet2 = aspect['planet2']
        sign1, degree1 = convert_to_sign_and_degree(positions[planet1][0])
        sign2, degree2 = convert_to_sign_and_degree(positions[planet2][0])
        
        print(f"{planet1}")
        print(f"\t{sign1} {degree1:.2f}°")
        print(f"{planet2}")
        print(f"\t{sign2} {degree2:.2f}°")
        print(f"{aspect['aspect']} ({planet1} -> {planet2})")
        print(f"\torb: {aspect['orb']:.2f}°")
        print(f"\t{aspect['applying'].capitalize()}")
        print()

# bringing single date/location together

def main():
    # Step 1: Get user input
    year, month, day, hour, minute, latitude, longitude = get_user_input()

    # Step 2: Query planetary positions
    positions = query_planetary_positions(year, month, day, hour, minute, latitude, longitude)

    # Step 3: Calculate aspects between the planets
    aspects = calculate_aspects(positions)

    # Step 4: Display the aspects and their details
    display_aspects(positions, aspects)

if __name__ == "__main__":
    main()