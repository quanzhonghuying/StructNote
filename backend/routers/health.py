# routers/health.py

from fastapi import APIRouter  # ルーター管理用クラスをインポート

router = APIRouter()  # ルーターインスタンスを作成

@router.get("/health")  # ヘルスチェック用エンドポイント
async def health_check():
    return {"status": "ok"}  # 稼働確認レスポンス
