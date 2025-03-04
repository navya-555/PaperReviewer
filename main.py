import streamlit as st
from process import analyze

def main():
    st.title("Paper Analysis")

    # Upload PDF file
    pdf_file = st.file_uploader("Upload your PDF file", type="pdf")
    if pdf_file is not None:
        # Pass the uploaded file to the function for processing
        with st.spinner('Processing...'):
            res = analyze(pdf_file)

        # Display the extracted text (or other processing results)
            st.write("Answer:")
            st.markdown(f'<div style="word-wrap: break-word; white-space: pre-wrap;">{res[4:-3]}</div>',unsafe_allow_html=True)

if __name__ == "__main__":
    main()