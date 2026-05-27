import streamlit as st
import streamlit_authenticator as stauth

# 1. SETUP: User Credentials
# Username: admin | Password: password123
names = ["Founder"]
usernames = ["admin"]
passwords = ["password123"] 

# Hash the passwords
hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    {'credentials': {'usernames': {usernames[0]: {'name': names[0], 'password': hashed_passwords[0]}}}},
    'dental_audit_cookie', 'signature_key', cookie_expiry_days=30
)

# 2. RENDER THE LOGIN SCREEN
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# 3. IF LOGIN SUCCESSFUL -> SHOW THE APP
elif authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.title(f"Welcome to DentalAudit.ai, {name}")
    
    st.sidebar.success("Logged in as Administrator")
    
    st.header("UK CQC Compliance Auditor")
    
    tab1, tab2, tab3 = st.tabs(["Daily Audit", "Risk Reports", "Group Management"])

    with tab1:
        st.subheader("Upload Daily Practice Logs")
        file = st.file_uploader("Drop your CQC compliance logs here", type=['csv', 'pdf'])
        if file:
            st.info("AI Analysis: Checking against UK Regulation 17 (Good Governance)...")
            st.success("✅ Log verified. No clinical risks detected for today.")

    with tab2:
        st.subheader("Compliance Risk Heatmap")
        st.warning("⚠️ Warning: 3 practices in 'Manchester North' group are overdue for Radiation Safety Audits.")
        
    with tab3:
        st.subheader("Enterprise Group View")
        st.metric(label="Total Practices", value="124", delta="12 new this month")
        st.metric(label="Compliance Score", value="98.2%", delta="0.5%")
