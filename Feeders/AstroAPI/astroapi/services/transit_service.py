

# display results

def display_aspects_between_instances_all_planets(positions1, positions2, aspect_results):
    for aspect in aspect_results:
        planet1 = aspect['planet1']
        planet2 = aspect['planet2']
        sign1, degree1 = convert_to_sign_and_degree(positions1[planet1][0])
        sign2, degree2 = convert_to_sign_and_degree(positions2[planet2][0])
        
        print(f"{planet1}")
        print(f"\tInstance 1: {sign1} {degree1:.2f}°")
        print(f"{planet2}")
        print(f"\tInstance 2: {sign2} {degree2:.2f}°")
        print(f"{aspect['aspect']} ({planet1} -> {planet2})")
        print(f"\torb: {aspect['orb']:.2f}°")
        print(f"\t{aspect['applying'].capitalize()}")
        print()