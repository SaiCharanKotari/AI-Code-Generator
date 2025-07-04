import streamlit as st
from code_generator import generate_code

st.set_page_config(page_title="AI Code Generator", page_icon="💻")
st.title("💻 AI Code Generator")
st.markdown(
    "Describe what you’d like the code to do, choose a language, and let the AI write it for you."
)

# User input
spec_text = st.text_area("📝 Describe the code you need:", height=200)

# Language choices
languages = [
    "Python",
    "JavaScript",
    "TypeScript",
    "Java",
    "C++",
    "C#",
    "Go",
    "Rust",
    "Bash",
]
lang = st.selectbox("🌐 Target language:", languages, index=0)

# Generate button
if st.button("🚀 Generate Code"):
    if spec_text.strip() == "":
        st.warning("Please describe what the code should do.")
    else:
        with st.spinner("Generating code…"):
            code = generate_code(spec_text, lang)
            st.success("Code generated!")
            st.code(code, language=lang.lower())

st.success("Created By Sai Charan ( 23BRS1009 )")
