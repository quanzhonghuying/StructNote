# backend/services/reporter.py

"""Report Generator サービス層"""

import re
from typing import List

def to_markdown(content: str) -> str:
    """入力テキストを Markdown レポートに変換する"""
    if not content.strip():
        raise ValueError("content が空です")

    items: List[str] = re.split(r"[。､,，\n]+", content)
    items = [x.strip() for x in items if x.strip()]

    md_lines = ["# 自動生成レポート\n"]
    for item in items:
        md_lines.append(f"- {item}")

    return "\n".join(md_lines)

