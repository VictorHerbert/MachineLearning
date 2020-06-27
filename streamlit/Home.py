<<<<<<< HEAD
import streamlit as st

import PageSummary as PS

def main():
    page = 'Home'
    content = ''
    
    def html_inject(file_name):
        with open(file_name) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    def sidebar():
        global page,content

        st.sidebar.title('Navigator')

        page = st.sidebar.selectbox(
            'Page', list(PS.pages.keys()))
        if len(PS.pages[page].keys()) == 1:
            content = 'Home'
        else:
            content = st.sidebar.selectbox(
                'Content', list(PS.pages[page].keys()))

    def body():
        global page,content
        PS.pages[page][content]()
        st.text('Made by Victor Herbert')
    
    sidebar()
    body()
    

if __name__ == '__main__':
=======
import streamlit as st

import PageSummary as PS

def main():
    page = 'Home'
    content = ''
    
    def html_inject(file_name):
        with open(file_name) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    def sidebar():
        global page,content

        st.sidebar.title('Navigator')

        page = st.sidebar.selectbox(
            'Page', list(PS.pages.keys()))
        if len(PS.pages[page].keys()) == 1:
            content = 'Home'
        else:
            content = st.sidebar.selectbox(
                'Content', list(PS.pages[page].keys()))

    def body():
        global page,content
        PS.pages[page][content]()
        st.text('Made by Victor Herbert')
    
    sidebar()
    body()
    

if __name__ == '__main__':
>>>>>>> 3d62429c56aab4cc084c7a673616583298c1139f
    main()