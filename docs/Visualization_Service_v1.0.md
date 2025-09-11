# Visualization Service v1.0

対応モジュール: `backend/services/visualizer.py`  
目的: 入力テキストを解析し、Mermaid.js コードを生成する内部ロジック。

---

## 1. 概要
- Visualization API (`/visualization/visualize`) から呼び出されるサービス層。  
- 入力文字列をノード列に分解し、方向指定に基づいて Mermaid.js コードを組み立てる。  
- 外部には直接公開せず、Router 層を経由して利用される。

---

## 2. 主な関数

### 2.1 `_tokenize_content(content: str) -> List[str]`
- 入力文字列を "->"、"→"、"=>" で分割してノードリストに変換。  
- **例**: `"A -> B -> C"` → `["A", "B", "C"]`

### 2.2 `_normalize_direction(direction: str) -> str`
- 入力方向を `"TD"` または `"LR"` に正規化。  
- **例**: `"td"` → `"TD"`、`"lr"` → `"LR"`

### 2.3 `_build_mermaid(nodes: List[str], direction: str) -> str`
- ノードリストと方向から Mermaid.js コードを構築。  
- **例**: `["A", "B", "C"], "TD"`  
  → `"graph TD; N0[A] --> N1[B] --> N2[C];"`

### 2.4 `to_mermaid(content: str, direction: str = "TD") -> str`
- 外部公開関数。入力テキストから直接 Mermaid.js コードを生成。  
- **例**:  
  - 入力: `"A -> B -> C", direction="TD"`  
  - 出力: `"graph TD; N0[A] --> N1[B] --> N2[C];"`

---

## 3. エラーハンドリング
- 空入力: `ValueError("Input content is empty or invalid")`  
- ノード数不足: `ValueError("At least two nodes are required...")`  
- Router 層で HTTP 400 または 500 として返却される。

---

## 4. 将来拡張
- サポート記法の追加（Markdown リストなど）。  
- ノードの装飾（色・形状・アイコン）。  
- Sequence Diagram、Mindmap など他の Mermaid 図式への拡張。  

