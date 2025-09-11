// API 設定
const API_BASE = "http://127.0.0.1:8000";           // FastAPI のローカルエンドポイント
const API_URL  = API_BASE + "/visualization/visualize";

const $input     = document.getElementById("input");     // 入力
const $direction = document.getElementById("direction"); // 方向 TD/LR
const $generate  = document.getElementById("generate");  // 実行ボタン
const $status    = document.getElementById("status");    // ステータス表示
const $diagram   = document.getElementById("diagram");   // Mermaid コンテナ

function setStatus(text){ $status.textContent = text || ""; } // ステータス更新

$generate.addEventListener("click", async () => {             // 生成処理
  const content   = ($input.value || "").trim();
  const direction = ($direction.value || "TD").toUpperCase();
  if (!content) { alert("テキストを入力してください"); return; }

  setStatus("生成中…");
  $diagram.textContent = "";

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content, direction })
    });
    if (!res.ok) throw new Error("HTTP " + res.status);
    const payload = await res.json();
    if (payload.status !== "success" || !payload.data?.mermaid) throw new Error("Invalid payload");

    $diagram.textContent = payload.data.mermaid;  // Mermaid コードを注入
    mermaid.init(undefined, $diagram);            // SVG にレンダリング
    setStatus("完成 ✅");
  } catch (e) {
    console.error(e);
    setStatus("生成失敗 ❌");
  }
});

