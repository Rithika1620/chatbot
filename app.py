import streamlit as st
import google.generativeai as genai

# --- Configuration ---
st.set_page_config(page_title="Quick Course Planner", page_icon="⚡")

# Setup Gemini API (Replace with your actual API key)
API_KEY = "AIzaSyA2m473JTtIOhjTMWZol9rqkerYB_xqcYY" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# --- UI Layout ---
st.title("⚡ Fast-Track Course Planner")
st.write("Get a concise, high-impact study roadmap in seconds.")

# Sidebar for inputs to keep the main screen clean
with st.sidebar:
    st.header("Settings")
    language = st.selectbox("Language", ("Python", "Java", "C"))
    level = st.selectbox("Level", ("Easy", "Medium", "Advanced"))
    duration = st.selectbox("Duration", ("4 Weeks", "2 Months", "More than 2 months"))

# --- Logic ---
if st.button("Generate Fast Schedule"):
    if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY":
        st.error("Please provide a valid API Key.")
    else:
        # THE PROMPT: This is where we control the "short and attractive" style
        prompt = f"""
        Act as a Senior Software Engineer. 
        Create a SHORT and VISUALLY ATTRACTIVE study plan for {language}.
        Level: {level} | Duration: {duration}
        
        Rules:
        1. Use a Markdown TABLE for the weekly schedule.
        2. Keep descriptions very brief (one sentence max).
        3. Use emojis to make it look modern.
        4. Focus only on high-impact topics.
        5. Add one "Pro-Tip" at the end.
        """

        with st.spinner("Creating your roadmap..."):
            try:
                response = model.generate_content(prompt)
                
                # Display results in a nice card-like container
                st.success(f"🚀 Your {level} {language} Roadmap is ready!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Ensure your API key is correct and library is updated.")

# Footer
st.markdown("---")
st.caption("Simplified AI Tutor • Concise & Effective")