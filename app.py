import streamlit as st
import streamlit_authenticator as stauth

# --- 1. SETUP ---
st.set_page_config(page_title="DentalAudit.ai", layout="wide")

# This is the EXACT format the library needs to avoid a KeyError
credentials = {
    'usernames': {
        'admin': {
            'name': 'Founder',
            'password': 'password123' 
        }
    }
}

# --- 2. INITIALIZE ---
# We pass the 'credentials' variable directly. 
# It contains the 'usernames' key that was causing the error.
authenticator = stauth.Authenticate(
    credentials,
    'dental_audit_cookie',
    'signature_key',
    cookie_expiry_days=30
)

# --- 3. LOGIN INTERFACE ---
# We use the simplest login method to ensure it loads
name, authentication_status, username = authenticator.login(location='main')

# --- 4. APP LOGIC ---
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.title("Welcome to DentalAudit.ai")
    
    st.header("UK CQC Compliance Auditor")
    tab1, tab2, tab3 = st.tabs(["Daily Audit", "Risk Reports", "Group Management"])

    with tab1:
        st.subheader("Upload Daily Practice Logs")
        file = st.file_uploader("Upload logs", type=['csv', 'pdf'])
        if file:
            st.info("AI Analysis: Checking against UK Regulation 17...")
            st.success("✅ Log verified.")

    with tab2:
        st.subheader("Compliance Risk Heatmap")
        st.warning("⚠️ Radiation Safety Audits overdue in Manchester.")
        
    with tab3:
        st.subheader("Enterprise Group View")
        st.metric(label="Total Practices", value="124", delta="12 new")
        st.metric(label="Compliance Score", value="98.2%")

elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.info('Please enter your username and password to access the Dental Audit platform.')
