# api/main.py

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Import logic classes
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.logic import UserManager, NoteManager, AudioProcessor

# -------------------- App Setup --------------------
app = FastAPI(title="EchoNotes", version="1.0")

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,       
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- Managers --------------------
user_manager = UserManager()
note_manager = NoteManager()
audio_processor = AudioProcessor()

# -------------------- Data Models --------------------
class User(BaseModel):
    name: str
    email: str

class UserUpdate(BaseModel):
    email: str
    new_name: str

class UserDelete(BaseModel):
    email: str

class Note(BaseModel):
    user_email: str
    content: str
    audio_url: str = None

class NoteUpdate(BaseModel):
    note_id: int
    new_content: str

class NoteDelete(BaseModel):
    note_id: int

class VoiceCommand(BaseModel):
    command: str

# -------------------- User Endpoints --------------------
@app.post("/users/")
def create_user(user: User):
    try:
        return user_manager.create_user(user.name, user.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/{email}")
def get_user(email: str):
    try:
        return user_manager.get_user(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/users/")
def update_user(user: UserUpdate):
    try:
        return user_manager.update_user(user.email, user.new_name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/users/")
def delete_user(user: UserDelete):
    try:
        return user_manager.delete_user(user.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# -------------------- Note Endpoints --------------------
@app.post("/notes/")
def create_note(note: Note):
    try:
        return note_manager.save_note(note.user_email, note.content, note.audio_url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/notes/{user_email}")
def get_notes(user_email: str):
    try:
        return note_manager.fetch_notes(user_email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/notes/")
def update_note(note: NoteUpdate):
    try:
        return note_manager.update_note(note.note_id, note.new_content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/notes/")
def delete_note(note: NoteDelete):
    try:
        return note_manager.delete_note(note.note_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# -------------------- Audio & Voice Endpoints --------------------
@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())
        transcript = audio_processor.transcribe_audio(file_location)
        os.remove(file_location)  # clean up temporary file
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/voice-command/")
def voice_command(command: VoiceCommand):
    try:
        result = audio_processor.process_voice_command(command.command)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
