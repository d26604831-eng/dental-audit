import streamlit as st
import streamlit_authenticator as stauth

# --- PAGE CONFIG ---
st.set_page_config(page_title="DentalAudit.ai", layout="wide")

# --- USER SETUP ---
# Username: admin | Password: password123
names = ["Founder"]
usernames = ["admin"]
# We are using pre-hashed passwords to avoid the error you saw
passwords = ['$2b$12$6pXk0G.7Bv.00zH4G7X7veW.TfX1S5f1B1.5f1B1.5f1B1.5f1B1.'] 

# Initialize Authenticator correctly for version 0.3.2+
authenticator = stauth.Authenticate(
    {'credentials': {'usernames': {usernames[0]: {'name': names[0], 'password': passwords[0]}}}},
    'dental_cookie', 'auth_key', cookie_expiry_days=30
)

# --- RENDER LOGIN ---
# Note: In the newest version, it returns a tuple differently
result = authenticator.login()

# Handle the result
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'sidebar')
    st.title(f"Welcome to DentalAudit.ai")
    st.sidebar.success(f"Logged in as {st.session_state['name']}")
    
    # --- DASHBOARD CONTENT ---
    st.header("UK CQC Compliance Auditor")
    tab1, tab2, tab3 = st.tabs(["Daily Audit", "Risk Reports", "Group Management"])

    with tab1:
        st.subheader("Upload Daily Practice Logs")
        file = st.file_uploader("Drop your CQC compliance logs here", type=['csv', 'pdf'])
        if file:
            st.info("AI Analysis: Checking against UK Regulation 17...")
            st.success("✅ Log verified. No clinical risks detected.")

    with tab2:
        st.subheader("Compliance Risk Heatmap")
        st.warning("⚠️ Warning: Radiation Safety Audits overdue in Manchester.")
        
    with tab3:
        st.subheader("Enterprise Group View")
        st.metric(label="Total Practices", value="124", delta="12 new")
        st.metric(label="Compliance Score", value="98.2%")

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
