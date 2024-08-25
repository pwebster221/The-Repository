from astroapi.services.transit_service import pull_transit_data
from astroapi.services.neo4j_service import update_neo4j

def main():
    transit_data = pull_transit_data()
    update_neo4j(transit_data)

if __name__ == '__main__':
    main()