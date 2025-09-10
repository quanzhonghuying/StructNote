# backend/services/visualizer.py
# サービス層：入力テキストを解析して Mermaid.js コードを生成する

from typing import List
import re


def _tokenize_content(content: str) -> List[str]:
    """テキストを矢印（->, →, =>）で分割してノードのリストに変換"""
    content = content.strip()
    if not content:
        return []
    parts = re.split(r'\s*(?:->|→|=>)\s*', content)
    return [p.strip() for p in parts if p.strip()]

def _normalize_direction(direction: str) -> str:
    """方向を TD または LR に正規化"""
    d = (direction or "TD").upper()
    return "LR" if d == "LR" else "TD"

def _build_mermaid(nodes: List[str], direction: str) -> str:
    """ノードリストと方向から Mermaid.js のコードを組み立てる"""
    if len(nodes) < 2:
        raise ValueError("ノードは最低2つ必要です")
    dir_code = _normalize_direction(direction)
    ids = [f"N{i}" for i in range(len(nodes))]
    labeled = [f"{ids[i]}[{nodes[i]}]" for i in range(len(nodes))]
    edges = " --> ".join(labeled)
    return f"graph {dir_code}; {edges};"

def to_mermaid(content: str, direction: str = "TD") -> str:
    """外部公開関数：入力文字列から Mermaid.js コードを生成"""
    nodes = _tokenize_content(content)
    if not nodes:
        raise ValueError("入力が空または無効です")
    return _build_mermaid(nodes, direction=direction)

