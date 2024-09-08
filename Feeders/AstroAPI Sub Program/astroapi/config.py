

import os
from dotenv import load_dotenv

load_dotenv()

SWISSEPH_PATH = os.getenv("SWISSEPH_PATH", "/path/to/AstroAPI/swisseph/ephe")
NEO4J_URI = os.getenv("bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")