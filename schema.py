from pydantic import BaseModel, ConfigDict
from datetime import datetime

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreateModel(NoteBase):
    pass

class NoteModel(NoteBase):
    id: str
    date_created: datetime
    model_config = ConfigDict(from_attributes=True)