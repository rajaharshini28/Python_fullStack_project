# EchoNotes

Description: EchoNotes is a smart voice-to-text note-taking app that converts spoken words into text using OpenAI’s Whisper API. Notes are securely stored in Supabase, and the app supports voice commands, real-time transcription, and easy organization. Capture ideas, meetings, or reminders effortlessly—no typing required!

## Key Features:

1.Voice Recording & Transcription:
    ->Record voice directly through a microphone.
    ->Converts speech to text using Whisper API for high accuracy.

2.Cloud Storage with Supabase:

    ->Notes are securely stored in a cloud database.
    ->Optional support for storing the original audio file.

3.Voice Commands:
    ->Say “new note” to start a fresh note.
    ->Say “stop” to exit the recording session.

4.Tkinter GUI:
    ->User-friendly interface with buttons for Record, Save, and Exit.
    ->Displays transcribed text in real time.
5.Timestamp & Organization:
    ->Each note is automatically timestamped.
    ->Optional tags and categorization for better organization.

6.Future Scalability:
    ->Multi-user support via Supabase authentication.
    ->Tags and search functionality to organize notes efficiently.
    ->Option to access notes from web or mobile apps via Supabase APIs.

## Project Structure

EchoNotes/
|
|---src/    #core application logic
|    |---logic.py  #Business logic task
|opreations    
|    |---db.py       #Database operations
|
|---API/        #Backend api
|   |---main.py     #FastAPI endpoints
|
|---frontend/       #frontend application
|   |---app.py      #streamlit web interface
|
|---requirements.txt        #install python dependencies
|
|---README.md       #project documentation
|
|---.env       #Python variables


## Quick Start

### Prerequisites

- Python 3.8 or higher
- A Supabase account
- Git(push,cloning)

### 1. Clone or Download the Project

# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download and extract the ZIP file

### 2.Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3.Set up Supabase Database

1.Create a Supabase Project:

2.Create the Tasks Table:

- Go to the SQL Editor in your Supabase dashboard
- Run this SQL Command:

``` sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE notes (
    id BIGSERIAL PRIMARY KEY,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    audio_url TEXT,
    timestamp TIMESTAMPTZ DEFAULT now()
);

```
3. **Get Your Credentials:**

### 4. Configure Environment variables

1. Create a `.env` file in the project root

2. Add your Supabase credentials to `.env`:
SUPABASE_URL=your_project_url here
SUPABASE_KEy=your_anon_key_here


### 5.Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at `http://localhost:8501`

## FastAPI Backend

cd api
python main.py
The Api will be available at `http:\\localhost:8000`

## How to use

## Technical Details

### Techologies Used 

- **Frontend**:Streamlit(Python web framwork)
- **Backend** :FastAPI(Python REST API framework)
- **Database**:Supabase(PostgreSQL-based backend-as-a-service)
- **Language**:Python 3.8+

### Key Components

1. **`src/db.py`**:Database operations 
    - Handles all CRUD operations with Supabase

2. **`src/logic.py`**:Business logic 
    - Task validation and processing

## TroubleShooting

## Common Issues
1. **"Module not found" errors**
    - Make sure you've installed all dependencies: `pip install -r requirements.txt`
    - Check that you're running commands from the correct directory

## Future Enhancements
 Ideas for extending this project

## Support

If you encounter any issues or have questions:
