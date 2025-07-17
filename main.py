from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from crud import CRUD
from db import engine
from schema import NoteModel, NoteCreateModel
from typing import List
from models import Note
import uuid
from http import HTTPStatus 

app = FastAPI(title="note API", description="this is a simple note app", docs_url="/")


session_maker = async_sessionmaker(
    bind = engine,
    expire_on_commit=False
)

db = CRUD()



@app.get("/notes", response_model=List[NoteModel])
async def get_all_notes():
    notes = await db.get_all(session_maker)
    return notes

@app.post("/notes", status_code=HTTPStatus.CREATED)
async def create_note(note_data:NoteCreateModel):
    new_note = Note(
        id = str(uuid.uuid4()),
        title = note_data.title, 
        content = note_data.content,

    )
    note = await db.add(session_maker, new_note)
    return note

@app.get("/note/{note_id}", response_model=NoteModel)
async def get_note_by_id(note_id):
    note = await db.get_by_id(session_maker, note_id)
    return note


@app.patch("/note/{note_id}")
async def update_note(note_id, data: NoteCreateModel):
    note = await db.update(session_maker, note_id, data)
    return note


@app.delete("/note/{note_id}")
async def delete_note(note_id):
    note = await db.delete(session_maker,note_id)
    return f"note : {note} removed"
