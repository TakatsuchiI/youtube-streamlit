import streamlit as st
import numpy as np
import pandas as pd

st.title ('streamlit')
st.write('dataframe')
df=pd.DataFrame({
    '1':[1,2,3,4],
    '2':[10,20,30,40]
})
st.write(df)

df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

df
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

