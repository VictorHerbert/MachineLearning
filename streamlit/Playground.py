<<<<<<< HEAD
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
    
=======
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
    
>>>>>>> 3d62429c56aab4cc084c7a673616583298c1139f
PS.pages['Playground'] = {'Home' : PlayPage.home}