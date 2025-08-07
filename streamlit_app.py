import streamlit as st
import pandas as pd

st.set_page_config(page_title="CCI SmartAdvisor 360", layout="wide")

st.title("💼 CCI SmartAdvisor 360 Dashboard")

# File Upload Section
st.sidebar.header("📤 Upload Data")
zoom_file = st.sidebar.file_uploader("Upload Zoom Transcript (.txt)", type=["txt"])
product_file = st.sidebar.file_uploader("Upload Product Pricing CSV", type=["csv"])
advisor_file = st.sidebar.file_uploader("Upload Advisor Metadata CSV", type=["csv"])

# Process Uploads
if zoom_file:
    st.subheader("📝 Zoom Transcript Preview")
    st.text(zoom_file.read().decode("utf-8")[:1000])  # First 1000 characters

if product_file:
    st.subheader("📦 Product & Pricing Data")
    df_products = pd.read_csv(product_file)
    st.dataframe(df_products)

if advisor_file:
    st.subheader("🧑‍💼 Advisor Metadata")
    df_advisors = pd.read_csv(advisor_file)
    st.dataframe(df_advisors)

# Simulated Bedrock Enrichment Output
if st.button("🔍 Analyze with AI"):
    st.subheader("🤖 AI Insights (Simulated)")
    st.info("Emotion: Positive 😊")
    st.info("Next-Best-Action: Recommend SIP Top-Up")
    st.warning("Detected Risk Concern: Crypto Exposure")

# Simulated Amazon Q Style Query Box
st.subheader("💬 Ask SmartAdvisor")
question = st.text_input("Ask a question (e.g., 'What is client's crypto exposure?')")
if question:
    st.success(f"🔍 AI Response: This client has 12% in high-risk crypto assets.")

# Embed Amazon QuickSight Dashboard
st.subheader("📊 QuickSight Dashboard")
st.components.v1.iframe(
    "https://us-east-1.quicksight.aws.amazon.com/sn/embed/share/accounts/888752476895/dashboards/49980764-9dca-48ab-8556-1b37e3341228?directory_alias=Taskmasters",
    width=960,
    height=720,
)
