# backend/routers/visualization.py
# 路由层（Controller）：定义 HTTP API，把请求交给服务层处理，并返回响应

from fastapi import APIRouter, HTTPException  # APIRouter = 路由器，HTTPException = HTTP 异常
from pydantic import BaseModel, Field  # BaseModel = 数据模型基类，Field = 字段说明/约束
from typing import Optional, Dict
from backend.services.visualizer import to_mermaid


router = APIRouter()  # 创建路由器对象

class VisualizationRequest(BaseModel):  # 输入数据模型
    content: str = Field(..., description="用户输入文本，例如 'A -> B -> C'")
    direction: Optional[str] = Field("TD", description="图方向：TD 或 LR")

class VisualizationResponse(BaseModel):  # 输出数据模型
    status: str
    data: Optional[Dict] = None
    message: Optional[str] = None

@router.post("/visualize", response_model=VisualizationResponse)  # 定义 POST 路由
def generate_visualization(req: VisualizationRequest) -> VisualizationResponse:
    content = (req.content or "").strip()
    direction = (req.direction or "TD").upper()

    if direction not in ("TD", "LR"):  # 如果方向不合法
        raise HTTPException(status_code=400, detail="direction must be 'TD' or 'LR'")

    if not content:  # 如果输入内容为空
        raise HTTPException(status_code=400, detail="Input content is empty")

    try:
        mermaid = to_mermaid(content=content, direction=direction)  # 调用服务层
        return VisualizationResponse(status="success", data={"mermaid": mermaid})
    except ValueError as ve:  # 可预期的错误
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:  # 其他未预料的错误
        raise HTTPException(status_code=500, detail="Mermaid generation failed")

