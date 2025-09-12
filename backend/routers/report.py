# backend/routers/report.py

"""Report API ルーター"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.reporter import to_markdown

router = APIRouter()

class ReportRequest(BaseModel):
    content: str

@router.post("/generate")
async def generate_report(req: ReportRequest):
    """テキストを Markdown レポートに変換"""
    try:
        markdown = to_markdown(req.content)
        return {"status": "success", "data": {"markdown": markdown}}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="内部エラー: " + str(e))

