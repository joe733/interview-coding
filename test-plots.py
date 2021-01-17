import streamlit as slt
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

slt.line_chart(chart_data)

map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])

slt.map(map_data)