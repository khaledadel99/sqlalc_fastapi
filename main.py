from fastapi import FastAPI

app = FastAPI(

    title="note API",
    description="this is a simple note app",
    docs_url="/"
)

@app.get('/')
async def hello():
    return {"messege" : "hello world"}



@app.get('/notes')
async def get_all_notes():
    pass


@app.post('/notes')
async def create_note():
    pass


@app.get('/note/{note_id}')
async def get_note_by_id(note_id):
    pass


@app.patch('/note/{note_id}')
async def update_note(note_id):
    pass 


@app.delete('/note/{note_id}')
async def delete_note(note_id):
    pass 