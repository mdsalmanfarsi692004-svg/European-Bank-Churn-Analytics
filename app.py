import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION & CUSTOM CSS ---
st.set_page_config(page_title="Bank Churn Analytics", page_icon="🏦", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* Global Dark Theme Settings */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* Centered Headings */
    h1, h2, h3 {
        text-align: center;
        font-family: 'Inter', sans-serif;
        color: #FFFFFF;
    }
    
    /* Professional Metric Cards */
    div[data-testid="metric-container"] {
        background-color: #1E1E2E;
        border: 1px solid #333344;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        text-align: center;
    }
    
    /* Subtle Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #151521;
        border-right: 1px solid #2B2B36;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATA INGESTION & PREPARATION ---
@st.cache_data
def load_data():
    df = pd.read_excel("European_Bank.xlsx")
    
    # 1. Data Cleaning
    cols_to_drop = ['Surname', 'CustomerId', 'Year']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors='ignore')
    
    # 2. Derived Segmentation Fields
    df['Age_Group'] = pd.cut(df['Age'], bins=[0, 29, 45, 60, 150], labels=['<30', '30-45', '46-60', '60+'])
    
    bal_median = df[df['Balance'] > 0]['Balance'].median()
    df['Balance_Segment'] = df['Balance'].apply(
        lambda x: 'Zero-balance' if x == 0 else ('Low-balance' if x <= bal_median else 'High-balance')
    )
    
    df['Tenure_Group'] = pd.cut(df['Tenure'], bins=[-1, 2, 7, 20], labels=['New', 'Mid-term', 'Long-term'])
    
    return df

df = load_data()

# --- SIDEBAR: DYNAMIC FILTERS ---
st.sidebar.markdown("<h2 style='text-align: left;'>Control Panel</h2>", unsafe_allow_html=True)
geo_filter = st.sidebar.multiselect("Geography", options=df['Geography'].unique(), default=df['Geography'].unique())
gender_filter = st.sidebar.multiselect("Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
age_filter = st.sidebar.multiselect("Age Group", options=df['Age_Group'].unique(), default=df['Age_Group'].unique())

filtered_df = df[
    (df['Geography'].isin(geo_filter)) &
    (df['Gender'].isin(gender_filter)) &
    (df['Age_Group'].isin(age_filter))
]

# --- PDF DOWNLOAD BUTTON ---
st.sidebar.markdown("---")
st.sidebar.markdown("<h3 style='text-align: left; color: white;'>Project Deliverables</h3>", unsafe_allow_html=True)

try:
    with open("European_Bank_Churn_Report.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        
    st.sidebar.download_button(
        label="📄 Download Executive Report",
        data=pdf_bytes,
        file_name="European_Bank_Churn_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )
except FileNotFoundError:
    st.sidebar.warning("Report PDF not found in folder.")

# --- MAIN DASHBOARD INTERFACE ---
st.title("🏦 European Banking: Customer Churn Analytics")
st.markdown("<p style='text-align: center; color: #A0A0B0;'>Segmentation-driven insights to design targeted retention strategies.</p>", unsafe_allow_html=True)
st.markdown("---")

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
else:
    # KPIs
    st.markdown("### 📊 Live Key Performance Indicators")
    total_cust = len(filtered_df)
    churn_rate = (filtered_df['Exited'].sum() / total_cust) * 100 if total_cust > 0 else 0
    
    hv_df = filtered_df[filtered_df['Balance_Segment'] == 'High-balance']
    hv_churn = (hv_df['Exited'].sum() / len(hv_df)) * 100 if len(hv_df) > 0 else 0
    
    inactive_df = filtered_df[filtered_df['IsActiveMember'] == 0]
    engage_drop = (inactive_df['Exited'].sum() / len(inactive_df)) * 100 if len(inactive_df) > 0 else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Segment Base", f"{total_cust:,}")
    c2.metric("Overall Churn Rate", f"{churn_rate:.1f}%")
    c3.metric("High-Value Churn", f"{hv_churn:.1f}%")
    c4.metric("Inactivity Risk (Drop)", f"{engage_drop:.1f}%")
    st.markdown("---")

    # Visualizations
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        st.markdown("### 🌍 Geographic Risk Index")
        geo_data = filtered_df.groupby('Geography')['Exited'].mean().reset_index()
        geo_data['Exited'] *= 100
        fig_geo = px.bar(geo_data, x='Geography', y='Exited', text='Exited', color='Geography',
                         color_discrete_sequence=['#4B4BFF', '#FF4B4B', '#00CC96'])
        fig_geo.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig_geo.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', showlegend=False)
        st.plotly_chart(fig_geo, use_container_width=True)
        
    with col_g2:
        st.markdown("### 📈 Age Segmentation Profile")
        age_data = filtered_df.groupby('Age_Group')['Exited'].mean().reset_index()
        age_data['Exited'] *= 100
        fig_age = px.line(age_data, x='Age_Group', y='Exited', markers=True, line_shape='spline', color_discrete_sequence=['#FF4B4B'])
        fig_age.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig_age, use_container_width=True)

    st.markdown("---")
    col_g3, col_g4 = st.columns(2)
    
    with col_g3:
        st.markdown("### 💰 Wealth Distribution")
        fig_bal = px.pie(filtered_df, names='Balance_Segment', hole=0.5, color_discrete_sequence=px.colors.sequential.Teal)
        fig_bal.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig_bal, use_container_width=True)
        
    with col_g4:
        st.markdown("### ⏳ Tenure & Loyalty Impact")
        tenure_data = filtered_df.groupby('Tenure_Group')['Exited'].mean().reset_index()
        tenure_data['Exited'] *= 100
        fig_tenure = px.bar(tenure_data, x='Tenure_Group', y='Exited', text='Exited', color_discrete_sequence=['#00CC96'])
        fig_tenure.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig_tenure.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig_tenure, use_container_width=True)

    # Drill-down
    st.markdown("---")
    st.markdown("### 🔍 Customer Data Drill-Down")
    st.dataframe(filtered_df.drop(columns=['Exited']).head(50), use_container_width=True)