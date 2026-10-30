import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv() # Loads the .env file

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Create the engine (the actual connection to the DB)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session (used to query the DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is the base class our database models will inherit from
Base = declarative_base()