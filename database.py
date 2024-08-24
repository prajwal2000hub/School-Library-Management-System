from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL (using SQLite in this case)
SQLALCHEMY_DATABASE_URL = "sqlite:///./lib.db"


# Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)# Create a session factory (SessionLocal) to generate database sessions