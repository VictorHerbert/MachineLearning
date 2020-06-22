import streamlit as st
import numpy as np
import pandas as pds
import matplotlib.pyplot as plt

import PageSummary as PS


class NCPage():
    def home():
        st.title('Numeric Calculus')

    def NewtonMethod():
        st.header('Newton Method')
        st.text('text')

        st.line_chart(np.linspace(0,1)**2)
    
    
PS.pages['Numeric Calculus'] = {'Home' : NCPage.home,'Newton Method' : NCPage.NewtonMethod}