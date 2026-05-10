import streamlit as st
import joblib
import os

# =========================
# Page Settings
# =========================
st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="wide"
)

# =========================
# Custom CSS Design
# =========================
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #1e293b 100%);
    color: white;
}

/* Main content container */
.block-container {
    padding-top: 3rem;
    max-width: 1050px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    border-right: 2px solid #38bdf8;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Titles */
h1 {
    color: #38bdf8;
    font-size: 48px !important;
    font-weight: 800 !important;
    text-align: center;
}

h2, h3 {
    color: #facc15;
}

/* Paragraph text */
p, label, div {
    font-size: 17px;
}

/* Text area */
textarea {
    background-color: #020617 !important;
    color: #ffffff !important;
    border: 2px solid #38bdf8 !important;
    border-radius: 15px !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.7rem 1.4rem;
    font-size: 17px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #06b6d4, #2563eb);
    transform: scale(1.05);
    color: white;
}

/* Cards */
.info-card {
    background: rgba(30, 41, 59, 0.95);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #38bdf8;
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);
    margin-bottom: 25px;
}

/* Project info box */
.project-box {
    background: rgba(2, 6, 23, 0.85);
    padding: 25px;
    border-radius: 20px;
    border-left: 6px solid #facc15;
    box-shadow: 0 0 20px rgba(250, 204, 21, 0.15);
}

/* Success message */
div[data-testid="stAlert"] {
    border-radius: 15px;
}

/* Sidebar image */
img {
    border-radius: 18px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Password System
# =========================
PASSWORD = st.secrets["APP_PASSWORD"]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h1>🔐 Login Page</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>Welcome</h3>
        <p>Please enter the password to access the Fake News Detection System.</p>
    </div>
    """, unsafe_allow_html=True)

    user_password = st.text_input("Enter Password:", type="password")

    if st.button("Login"):
        if user_password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Wrong password ❌")

    st.stop()

# =========================
# Load Model
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "fake_news_model.pkl")

model = joblib.load(model_path)

# =========================
# Sidebar
# =========================
# =========================
# Sidebar
# =========================
image_path = os.path.join(BASE_DIR, "my_photo.jpg")

if os.path.exists(image_path):
    col1, col2, col3 = st.sidebar.columns([1, 3, 1])
    with col2:
        st.image(image_path, width=180)
else:
    st.sidebar.warning("Student image not found. Please add my_photo.jpg")

st.sidebar.markdown("## 👨‍🎓 Student Information")
st.sidebar.markdown("""
**Name:** Osamah Musaed

**Project:** Fake News Detection System  

**Course:** Machine Learning  

**Programming Language:** Python  

**Model:** Logistic Regression  

**Email:** osama715008285@gmail.com

**phone:** +905340534090
""")

st.sidebar.divider()

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# =========================
# Main Page
# =========================
st.markdown("<h1>📰 Fake News Detection System</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <h3>Project Description</h3>
    <p>
        This system detects whether a news text is <b>Fake</b> or <b>Real</b>
        using Machine Learning. The user enters a news sentence or article,
        and the trained model analyzes the text and gives the prediction.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### ✍️ Enter News Text:")

news_text = st.text_area("", height=220, placeholder="Write or paste news text here...")

col1, col2 = st.columns([1, 4])

with col1:
    check_button = st.button("Check News")

with col2:
    clear_button = st.button("Clear Text")

if clear_button:
    st.rerun()

if check_button:
    if news_text.strip() == "":
        st.warning("Please enter news text first.")
    else:
        prediction = model.predict([news_text])

        if prediction[0].lower() == "real":
            st.success("✅ Result: Real News")
        else:
            st.error("❌ Result: Fake News")

# =========================
# Project Information
# =========================
st.markdown("---")

st.markdown("""
<div class="project-box">
    <h2>📌 Project Information</h2>
    <p><b>Project Name:</b> Fake News Detection System</p>
    <p><b>Student Name:</b> Osamah Ahmed</p>
    <p><b>Course:</b> Machine Learning</p>
    <p><b>Language Used:</b> Python</p>
    <p><b>Library Used:</b> Streamlit</p>
    <p><b>Model Used:</b> Logistic Regression</p>
</div>
""", unsafe_allow_html=True)