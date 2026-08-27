from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# DATABASE_URL = "postgresql://username:password@localhost/blogdb"

# Connection url
DATABASE_URL = "postgresql://postgres:Admin%40123@localhost:5433/blogdb"

# Engine 
engine = create_engine(DATABASE_URL)

# For DB operation
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()
