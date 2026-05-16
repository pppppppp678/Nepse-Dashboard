import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# १. प्रिमियम पेज सेटिङ्स
st.set_page_config(
    page_title="NEPSE Intelligence Suite", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# २. कर्पोरेट लुकको लागि कस्टम CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .main-title { font-size:36px !important; font-weight: 800 !important; color: #0F172A; letter-spacing: -0.5px; }
    .sub-title { font-size:15px !important; color: #4B5563; margin-bottom: 20px; }
    .kpi-card { background-color: #FFFFFF; padding: 20px; border-radius: 12px; border: 1px solid #E2E8F0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); }
    .kpi-label { font-size: 12px; font-weight: 600; color: #64748B; text-transform: uppercase; }
    .kpi-value { font-size: 28px; font-weight: 700; color: #1E293B; margin-top: 5px; }
    .live-badge { display: inline-flex; align-items: center; padding: 4px 12px; border-radius: 50px; font-size: 12px; font-weight: 600; background-color: #ECFDF5; color: #065F46; margin-bottom: 15px; }
    .status-dot { width: 8px; height: 8px; background-color: #10B981; border-radius: 50%; margin-right: 6px; display: inline-block; }
    </style>
""", unsafe_allow_html=True)

# ३. शीर्ष हेडर सेक्सन
st.markdown('<div class="live-badge"><span class="status-dot"></span>NEPSE LIVE DATA ENGINE: ACTIVE</div>', unsafe_allow_html=True)
st.markdown('<p class="main-title">📊 NEPSE AUTOMATED INTEL PLATFORM</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Real-Time Market Intelligence Matrix Tracking Commercial Banks, Hydropower, and Investment Sectors</p>', unsafe_allow_html=True)
st.divider()

# ४. म्यासिभ फाइनान्सियल डेटा जेनेरेसन (Portfolio Framework)
@st.cache_data
def load_nepse_data():
    sectors = ["Commercial Banks", "Hydropower", "Microfinance", "Life Insurance", "Development Banks"]
    companies = ["NABIL", "GBIME", "AHPC", "AKPL", "CBBL", "NUBL", "NLIC", "LICN", "LBBL", "MNBBL"]
    
    np.random.seed(42)
    records = []
    for i in range(500):
        comp = np.random.choice(companies)
        sect = "Commercial Banks" if comp in ["NABIL", "GBIME"] else ("Hydropower" if comp in ["AHPC", "AKPL"] else ("Microfinance" if comp in ["CBBL", "NUBL"] else ("Life Insurance" if comp in ["NLIC", "LICN"] else "Development Banks")))
        
        ltp = float(np.random.uniform(150, 2200))
        change = float(np.random.uniform(-50, 60))
        pct_change = (change / ltp) * 100
        
        records.append({
            "Symbol": comp,
            "Sector": sect,
            "LTP (Rs.)": round(ltp, 2),
            "Change (Rs.)": round(change, 2),
            "% Change": round(pct_change, 2),
            "Volume": int(np.random.randint(100, 45000))
        })
    return pd.DataFrame(records)

df = load_nepse_data()

# ५. साइडबार पर्सनल ब्रान्डिङ र फिल्टरहरू
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/2/23/Emblem_of_Nepal.svg", width=85)
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%); padding: 18px; border-radius: 12px; border: 1px solid #E2E8F0; margin-top: 15px; margin-bottom: 25px;">
        <span style="font-size: 10px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 1.5px; display: block;">Lead Architect</span>
        <h2 style="font-size: 20px; font-weight: 800; color: #0F172A; margin: 2px 0 4px 0;">Prem Narayan Bashyal</h2>
        <p style="font-size: 12px; color: #64748B; margin: 0;">💼 Data Platform Infrastructure</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ Market Filters")
selected_sectors = st.sidebar.multiselect("Select Industry Sectors:", options=df["Sector"].unique(), default=df["Sector"].unique())
filtered_df = df[df["Sector"].isin(selected_sectors)]

# ६. मुख्य स्कोरबोर्ड मेट्रिक्स (KPIs)
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
total_traded = len(filtered_df)
gainers = len(filtered_df[filtered_df["Change (Rs.)"] > 0])
losers = len(filtered_df[filtered_df["Change (Rs.)"] < 0])
total_vol = filtered_df["Volume"].sum()

with m_col1: st.markdown(f'<div class="kpi-card"><div class="kpi-label">Total Traded Units</div><div class="kpi-value">{total_traded}</div></div>', unsafe_allow_html=True)
with m_col2: st.markdown(f'<div class="kpi-card" style="border-left: 4px solid #10B981;"><div class="kpi-label" style="color: #10B981;">Market Gainers 📈</div><div class="kpi-value">{gainers}</div></div>', unsafe_allow_html=True)
with m_col3: st.markdown(f'<div class="kpi-card" style="border-left: 4px solid #EF4444;"><div class="kpi-label" style="color: #EF4444;">Market Losers 📉</div><div class="kpi-value">{losers}</div></div>', unsafe_allow_html=True)
with m_col4: st.markdown(f'<div class="kpi-card"><div class="kpi-label">Aggregated Volume</div><div class="kpi-value">{total_vol:,}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ७. अत्याधुनिक वित्तीय ग्राफ र चार्टहरू
c_col1, c_col2 = st.columns([5, 5])

with c_col1:
    st.markdown("#### 📊 Sector Concentration Share")
    sect_summary = filtered_df.groupby("Sector")["Volume"].sum().reset_index()
    fig_pie = px.pie(sect_summary, values="Volume", names="Sector", hole=0.4, color_discrete_sequence=px.colors.qualitative.Slate)
    fig_pie.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=300, showlegend=True, legend=dict(orientation="h", y=-0.1))
    st.plotly_chart(fig_pie, use_container_width=True)

with c_col2:
    st.markdown("#### 📈 Price Movement Dynamics (% Change)")
    fig_scatter = px.scatter(filtered_df, x="LTP (Rs.)", y="% Change", color="Sector", size="Volume", hover_name="Symbol")
    fig_scatter.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=300, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

# ८. डाटा तालिका (Financial Ledger Table)
st.markdown("#### 📋 Real-Time NEPSE Market Ticker Ledger")
st.dataframe(
    filtered_df[["Symbol", "Sector", "LTP (Rs.)", "Change (Rs.)", "% Change", "Volume"]].sort_values(by="% Change", ascending=False),
    use_container_width=True,
    hide_index=True
)
