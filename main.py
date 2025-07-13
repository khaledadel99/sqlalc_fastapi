from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from crud import CRUD
from db import engine
from serializer import NoteModel, NoteCreateModel
from typing import List
from models import Note
import uuid
from http import HTTPStatus 

app = FastAPI(title="note API", description="this is a simple note app", docs_url="/")


session = async_sessionmaker(
    bind = engine,
    expire_on_commit=False
)

db = CRUD()

@app.get("/")
async def hello():
    return {"messege": "hello world"}


@app.get("/notes", response_model=List[NoteModel])
async def get_all_notes():
    notes = await db.get_all(session)
    return [NoteModel(**note) for note in notes]

@app.post("/notes", status_code=HTTPStatus.CREATED)
async def create_note(note_data:NoteCreateModel):
    new_note = Note(
        id = str(uuid.uuid4()),
        title = note_data.title,
        content = note_data.content,

    )
    note = await db.add(session, new_note)
    return note

@app.get("/note/{note_id}")
async def get_note_by_id(note_id):
    pass


@app.patch("/note/{note_id}")
async def update_note(note_id):
    pass


@app.delete("/note/{note_id}")
async def delete_note(note_id):
    pass
