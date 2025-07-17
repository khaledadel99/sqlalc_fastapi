from models import Note
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

class CRUD:
    async def get_all(self,async_session:async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(Note).order_by(Note.id)
            result = await session.execute(statement)
            return result.scalars().all()



    async def add(self, async_session:async_sessionmaker[AsyncSession], note:Note):
        async with async_session() as session:
            session.add(note)
            await session.commit()



    async def get_by_id(self, async_session:async_sessionmaker[AsyncSession], note_id:str):
        async with async_session() as session:
            statement = select(Note).filter(Note.id == note_id)
            result = await session.execute(statement)
            return result.scalars().one()
            


    async def update(self, async_session:async_sessionmaker[AsyncSession],note_id:str, data):
        async with async_session() as session:
            note = await self.get_by_id(async_session,note_id)
            note.title = data['title']
            note.content = data['content']
            await session.commit()
            return note 



    async def delete(self, async_session:async_sessionmaker[AsyncSession], note:Note):
        async with async_session() as session:
            session.delete(note)
            await session.commit()