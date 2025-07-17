from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()
ascengine = create_async_engine(url=os.getenv("db_url"), echo=True)
engine = create_engine(url=os.getenv("db_url"), echo=True)

