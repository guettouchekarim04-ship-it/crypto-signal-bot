import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Crypto Signal Bot",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {
        background: #0b1220;
        color: white;
    }
    .block-container {
        max-width: 1100px;
        padding: 1rem 1rem 2rem 1rem;
    }
    .title {
        font-size: 30px;
        font-weight: 800;
        margin-bottom: 4px;
    }
    .subtitle {
        color: #8fa1bd;
        margin-bottom: 18px;
    }
    .card {
        background: #121c2e;
        border: 1px solid #24334d;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .coin {
        font-size: 19px;
        font-weight: 800;
    }
    .price {
        font-size: 17px;
        font-weight: 700;
    }
    .signal-buy {
        color: #31d17c;
        font-weight: 800;
    }
    .signal-sell {
        color: #ff5d6c;
        font-weight: 800;
    }
    .signal-wait {
        color: #ffc857;
        font-weight: 800;
    }
    .muted {
        color: #8fa1bd;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# ===== Header =====
st.markdown('<div class="title">📈 Crypto Signal Bot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">مراقبة العملات وإشارات التداول — Multi‑Timeframe جاهز للربط</div>',
    unsafe_allow_html=True
)

# ===== Controls =====
c1, c2, c3 = st.columns(3)

with c1:
    timeframe = st.selectbox(
        "الفريم",
        ["1m", "5m", "15m", "1h", "4h", "1D"],
        index=2
    )

with c2:
    market = st.selectbox(
        "السوق",
        ["USDT", "USDC", "BTC"]
    )

with c3:
    search = st.text_input("بحث عن عملة", placeholder="مثال: BTC")

# ===== Demo data =====
data = [
    ["BTC",  "67,420.50", "BUY",  86, "صاعد"],
    ["ETH",   "3,284.20", "BUY",  79, "صاعد"],
    ["BNB",     "612.80", "WAIT", 61, "محايد"],
    ["SOL",     "154.70", "BUY",  83, "صاعد"],
    ["XRP",       "0.584", "SELL", 72, "هابط"],
    ["ADA",       "0.351", "WAIT", 55, "محايد"],
    ["DOGE",      "0.121", "BUY",  76, "صاعد"],
    ["AVAX",      "28.42", "SELL", 68, "هابط"],
]

df = pd.DataFrame(
    data,
    columns=["Coin", "Price", "Signal", "Strength", "Trend"]
)

if search.strip():
    df = df[df["Coin"].str.contains(search.strip().upper(), na=False)]

# ===== Top stats =====
a, b, c, d = st.columns(4)
a.metric("العملات", len(df))
b.metric("BUY", int((df["Signal"] == "BUY").sum()))
c.metric("SELL", int((df["Signal"] == "SELL").sum()))
d.metric("الفريم", timeframe)

st.markdown("### العملات والإشارات")

# ===== Coin cards =====
for _, row in df.iterrows():
    signal = row["Signal"]

    if signal == "BUY":
        cls = "signal-buy"
        icon = "🟢"
    elif signal == "SELL":
        cls = "signal-sell"
        icon = "🔴"
    else:
        cls = "signal-wait"
        icon = "🟡"

    st.markdown(f"""
    <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;">
            <div>
                <div class="coin">{icon} {row["Coin"]}/{market}</div>
                <div class="muted">الاتجاه: {row["Trend"]} · الفريم: {timeframe}</div>
            </div>
            <div style="text-align:right;">
                <div class="price">${row["Price"]}</div>
                <div class="{cls}">{signal}</div>
            </div>
        </div>
        <div style="margin-top:12px;">
            <div class="muted">قوة الإشارة: {row["Strength"]}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===== Footer =====
st.caption("واجهة تجريبية — الإشارات الحالية بيانات تجريبية وليست توصيات مالية.")
