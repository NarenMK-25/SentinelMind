import streamlit as st
import os

st.set_page_config(page_title="SentinelMind Dashboard", layout="wide")

st.title("🛡️ SentinelMind: AI Security Agent")
st.markdown("### Real-Time Threat Monitoring")

# A button to manually refresh the web page
if st.button("🔄 Refresh Threat Logs"):
    st.rerun()

# Read the log file that your Actuator creates
if os.path.exists("security_log.txt"):
    with open("security_log.txt", "r") as f:
        logs = f.readlines()
    
    # Display the total number of blocks
    st.metric(label="Active Threats Blocked", value=len(logs))
    
    st.divider()
    st.subheader("🚨 Recent Defense Actions")
    
    # Display the logs in reverse order (newest at the top)
    for log in reversed(logs[-10:]): 
        st.error(log.strip()) # Formats it as a red alert box
else:
    st.success("System Secure: No threats detected yet. Start your main.py agent!")
