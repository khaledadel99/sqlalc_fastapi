from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

Base = declarative_base()
engine = create_async_engine(url=os.getenv("db_url"),
                             echo=True
                             )
