import google.generativeai as genai
from pypdf import PdfReader
import os
import streamlit as st

genai.configure(api_key=st.secrets['API'])
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

def analyze(pdf):
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    prompt=f'''I am providing with a pdf, you need to tell whether it is helpful form my review paper or not based on inclusion exclusion criteria.
                Inclusion Criteria

                Studies will be included if they:
                1. Focus on Peer Programming – Research that explicitly discusses peer programming in educational settings.
                2. Use Project-Based Learning (PBL) – Studies that integrate peer programming within a project-based learning framework.
                3. Address Educator Strategies – Papers that provide strategies for integrating peer programming into PBL courses.
                4. Discuss Assessment Techniques – Research that evaluates assessment methods for peer programming in PBL environments.
                5. Cover Collaborative Skill-Building – Studies that explore how programming projects can enhance both individual learning and teamwork.
                6. Empirical or Review Studies – Peer-reviewed empirical studies, systematic reviews, or meta-analyses that provide data-driven insights.
                7. Published in the Last 10-15 Years – To ensure relevance, focus on studies from recent years (e.g., post-2010).
                ---
                Exclusion Criteria

                Studies will be excluded if they:
                1. Do Not Involve Peer Programming – Research that focuses solely on individual programming efforts or other instructional methods.
                2. Lack a Project-Based Learning Component – Papers that do not integrate PBL with peer programming.
                3. Do Not Discuss Assessment or Strategy – Studies that do not provide insights into assessment methods or strategies for implementation.
                4. Theoretical or Opinion-Based Without Empirical Support – Studies without practical application or empirical data.
                5. Focus on Non-Educational Contexts – Research discussing peer programming in professional or corporate environments rather than academic settings.
                6. Are Older Than 15 Years – Unless they are foundational works, older studies may be excluded to focus on current best practices.

                note-if you include criteria numbers in reason, specify the criteria statement as well.

                pdf text:
                {text}

                Response Format (should be in markdown format. Dont include the word markdown):
                response: "Yes" or "No",
                reason: "Brief explanation referencing inclusion/exclusion criteria"

                If response is 'Yes' give the extract all the portions from the pdf that is helpful.
                '''
    result = model.generate_content([prompt,text])
    return result.text