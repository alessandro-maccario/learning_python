"""
    Every functions used is saved here to keep the codebase as clean as possible.
"""

# import packages
import streamlit as st


def local_css(file_name):
    """
    Open the style.css file
    """
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
