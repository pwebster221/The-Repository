from astroapi.services.neo4j_service import Neo4jService
from astroapi.services.transit_service import get_transit_data
from dotenv import load_dotenv
import os

load_dotenv()

neo4juser = os.getenv('neo4juser')
neo4jpass = os.getenv('neo4jpass')
neo4jserver = os.getenv('neo4jserver')
def main():
    neo4j_service = neo4jserver(uri=neo4j, user=neo4juser, password=neo4jpass)
    transit_data = get_transit_data()
    neo4j_service.update_transit_data(transit_data)
    neo4j_service.close()

if __name__ == '__main__':
    main()