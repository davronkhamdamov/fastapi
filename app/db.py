import os
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, create_engine
from sqlalchemy.sql import func
from databases import Database
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), index=True),
    Column("surname", String(50), index=True),
    Column("email", String(50), unique=True, index=True),
    Column("create_at", DateTime, default=func.now(), nullable=False),
)
database = Database(DATABASE_URL)
