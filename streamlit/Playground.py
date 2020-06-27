import streamlit as st
import numpy as np
import pandas as pds
import matplotlib.pyplot as plt
import cv2
import time

import PageSummary as PS


class PlayPage():
    def home():
        st.title('Playground')
    
PS.pages['Playground'] = {'Home' : PlayPage.home}