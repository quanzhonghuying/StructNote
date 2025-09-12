# backend/main.py
# FastAPI アプリのエントリーポイント

from fastapi import FastAPI
from backend.routers import health, notepad, visualization  # サブルーターをインポート
from backend.routers import report

app = FastAPI()  # アプリインスタンス作成

# ルーター登録
app.include_router(health.router, prefix="/health", tags=["health"])          # ヘルスチェック
app.include_router(notepad.router, prefix="/notepad", tags=["notepad"])      # ノート管理
app.include_router(visualization.router, prefix="/visualization", tags=["visualization"])  # 可視化
app.include_router(report.router, prefix="/report", tags=["report"])
