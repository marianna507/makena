import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st
import plotly.graph_objects as go

import pandas as pd


sunset_imgs = [
    '/home/lornam/Downloads/cyber/Cyber victims.png',
    '/home/lornam/Downloads/cyber/geographic distribution.png',
    '/home/lornam/Downloads/cyber/cyber victims per count.png' ,
    '/home/lornam/Downloads/cyber/cyber attack.png',
    '/home/lornam/Downloads/cyber/point pattern 1.png',
    '/home/lornam/Downloads/cyber/Screenshot at 2022-12-17 18-57-23.png',
    '/home/lornam/Downloads/cyber/Screenshot at 2022-12-17 18-58-07.png',
    '/home/lornam/Downloads/cyber/Screenshot at 2022-12-17 19-19-34.png',
    '/home/lornam/Downloads/cyber/Screenshot at 2022-12-17 18-57-23.png',
]
st.image(sunset_imgs, width=400)