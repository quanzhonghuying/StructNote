# routers/notepad.py

from fastapi import APIRouter, Body
import json, os

router = APIRouter()

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "notes.json")

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

@router.post("/notepad/add")  # ノート追加
async def add_note(content: str = Body(..., embed=True)):
    notes = load_notes()
    new_id = len(notes) + 1
    note = {"id": new_id, "content": content}
    notes.append(note)
    save_notes(notes)
    return {"message": "Note saved", "id": new_id}

@router.get("/notepad/list")  # ノート一覧取得
async def list_notes():
    notes = load_notes()
    return {"notes": notes}

