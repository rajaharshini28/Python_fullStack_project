# src/logic.py

from src.db import DatabaseManager
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class AudioProcessor:
    """Utility class for audio transcription and voice commands"""

    @staticmethod
    def transcribe_audio(file_path: str) -> str:
        """Convert audio file to text using OpenAI Whisper"""
        with open(file_path, "rb") as audio_file:
            transcript = openai.audio.transcription.create(
                model="whisper-1", file=audio_file
            )
        return transcript.text

    @staticmethod
    def process_voice_command(command: str) -> str:
        """Handle voice commands like 'new note' or 'stop'"""
        cmd = command.lower().strip()
        if "new note" in cmd:
            return "NEW_NOTE"
        elif "stop" in cmd:
            return "STOP"
        return "UNKNOWN"


class UserManager:
    """Handles all user-related operations"""

    def __init__(self):
        self.db = DatabaseManager()

    def create_user(self, name: str, email: str):
        return self.db.create_user(name, email)

    def get_user(self, email: str):
        user = self.db.get_user(email)
        if not user:
            raise Exception("User not found")
        return user

    def update_user(self, email: str, new_name: str):
        user = self.db.get_user(email)
        if not user:
            raise Exception("User not found")
        return self.db.update_user(email, new_name)

    def delete_user(self, email: str):
        user = self.db.get_user(email)
        if not user:
            raise Exception("User not found")
        return self.db.delete_user(email)


class NoteManager:
    """Handles all note-related operations"""

    def __init__(self):
        self.db = DatabaseManager()

    def save_note(self, user_email: str, content: str, audio_url: str = None):
        user = self.db.get_user(user_email)
        if not user:
            raise Exception("User not found")
        user_id = user[0]["id"]
        return self.db.add_note(user_id, content, audio_url)

    def fetch_notes(self, user_email: str):
        user = self.db.get_user(user_email)
        if not user:
            raise Exception("User not found")
        user_id = user[0]["id"]
        return self.db.get_notes(user_id)

    def update_note(self, note_id: int, new_content: str):
        note = self.db.get_note_by_id(note_id)
        if not note:
            raise Exception("Note not found")
        return self.db.update_note(note_id, new_content)

    def delete_note(self, note_id: int):
        note = self.db.get_note_by_id(note_id)
        if not note:
            raise Exception("Note not found")
        return self.db.delete_note(note_id)
