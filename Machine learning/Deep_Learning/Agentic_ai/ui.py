import streamlit as st
from youtube import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered"
)
st.title("Ai Youtube Video Analyzer ▶️")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# for input box
video_url = st.text_input("Enter YouTube video URL:")  # form of string

button = st.button("Analyze Video")  # form of TRUE/FALSE

if video_url and button:
    prompt = f"Get the captions and metadata for this video first, then analyze it: {video_url}"

    with st.spinner("Analyzing video..."):
        try:
            response = agent.run(prompt)
        except Exception as e:
            st.warning(f"First attempt failed ({e}), retrying...")
            try:
                response = agent.run(prompt)
            except Exception as e2:
                st.error(f"Analysis failed after retry: {e2}")
                st.info("Try: pip install -U agno groq, or switch Groq models.")
                st.stop()

    st.markdown("### Analysis Result:")
    st.markdown(response.content)