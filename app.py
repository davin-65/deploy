import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("mongodb+srv://fadil123:fadil123@atlascluster.jbkflub.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("client.pkl2")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
