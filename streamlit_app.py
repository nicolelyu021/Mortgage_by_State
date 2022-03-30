
##### This app is just an extremely simple example.
##### See the Streamlit documentation for how to create more complex apps.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('/work/practice-project-dataset-mortgage.csv') 
df['property_value'] = df['property_value'].replace('Exempt',np.nan).astype(float)
df['approved'] = (df['action_taken'] == 1) | (df['action_taken'] == 2)

selected_race = st.selectbox(
    "Pick a race:",
    df.derived_race.unique()
)

selected_sex = st.selectbox(
    "Pick a sex:",
    df.derived_sex.unique()
)
df = df[(df['derived_race'] == selected_race) & (df['derived_sex'] == selected_sex)]
new = df.groupby(["state_code"])[["approved", "property_value"]].mean()
plot = plt.scatter(data = new,x='approved',y='property_value')
st.pyplot(plt.gcf())


# ##### Title and intro

# st.title( 'Example Streamlit App' )
# st.write( '''
# This app is very small and does almost nothing.
# It's just an example.
# ''' )


# ##### Inputs

# st.header( 'Choose two numbers' )
# a = st.slider( label='a', min_value=1, max_value=10, value=2, step=1 )
# b = st.slider( label='b', min_value=1, max_value=10, value=3, step=1 )


# ##### Output

# st.header( 'Tiny computations')
# st.write( f'{a} + {b} = {a+b}' )
# st.write( f'{a} - {b} = {a-b}' )
# st.write( f'{a} * {b} = {a*b}' )
# st.write( f'{a} / {b} = {a/b}' )
