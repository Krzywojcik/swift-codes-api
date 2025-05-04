
 #Module name:   database
 #Author:        Krzysztof Wójcik
 #Last modified: 2025-05-03
 #Description:   Database connection and session factory using SQLAlchemy


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./swift_codes.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
