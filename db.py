import os
from supabase import create_client
from dotenv import load_dotenv

#load envirenoment variables
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase=create_client(url,key)

#create Task
"""Insert new User"""
def create_user(name:str, email:str):
    response=supabase.table("users").insert({"name":name , "email":email}).execute()
    return response.data

"""Fetch user by email"""
def get_user(email:str):
    response=supabase.table("users").select("*").eq("email",email).execute()
    return response.data

"""Update user by user email"""
def update_user(email:str, new_name:str ):
    response=supabase.table("users").update({"name":new_name}).eq("email",email).execute()
    return response.data

"""Delete the user by email"""
def delete_user(email:str):
    response=supabase.table("users").delete().eq("email",email).execute()
    return response.data

"""Insert new note in database"""
def add_note(user_id: str,content:str,audio_url:str =None):
    response=supabase.table("notes").insert(
        {"user_id":user_id,"content":content,"audio_url":audio_url}
    ).execute()
    return response.data

"""Fetch the notes of the user"""
def get_notes(user_id:str):
    response=supabase.table("notes").select("*").eq("user_id", user_id).order("timestamp", desc=True).execute()
    return response.data

"""Fetch notes by id"""
def get_notes_by_id(note_id:int):
    response=supabase.table("notes").select("*").eq("id",note_id).execute()
    return response.data

"""Update notes by id"""
def update_note(note_id: int, new_content: str):
    response = supabase.table("notes").update({"content": new_content}).eq("id", note_id).execute()
    return response.data

"""Delete notes"""
def delete_note(note_id: int):
    response = supabase.table("notes").delete().eq("id", note_id).execute()
    return response.data
