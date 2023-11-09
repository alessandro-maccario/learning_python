"""
    Every functions used is saved here to keep the codebase as clean as possible.
"""

# import packages
import streamlit as st
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
from htbuilder import (
    HtmlElement,
    div,
    ul,
    li,
    br,
    hr,
    a,
    p,
    img,
    styles,
    classes,
    fonts,
)
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def local_css(file_name):
    """
    Open the style.css file
    """
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# create the footer
# https://discuss.streamlit.io/t/st-footer/6447


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):
    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 60px ;}
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        right=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="white",
        text_align="center",
        height="auto",
        opacity=1,
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="none",
        border_width=px(2),
    )

    body = p()
    foot = div(style=style_div)(hr(style=style_hr), body)

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made in ",
        image(
            "https://streamlit.io/images/brand/streamlit-mark-color.png",  # reference the image: https://streamlit.io/brand
            width=px(20),
            height=px(12),
        ),
        " with ❤️ by ",
        link("https://github.com/alessandro-maccario", "Alessandro Maccario"),
        br(),
        # link(
        #     "https://google.com/",  # to be changed!
        #     # "https://buymeacoffee.com/chrischross",  # to be changed!
        #     image(
        #         "https://cdn.buymeacoffee.com/buttons/default-black.png"
        #     ),  # to be changed!
        # ),
    ]
    layout(*myargs)
