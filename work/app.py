import streamlit as st
import numpy as np
import pandas as pd


##### function #####

@st.cache
def mM2g(concentration_mM, Mw, solution_mL):
	concentration_g = concentration_mM * Mw * solution_mL * 10**-6
	return concentration_g


##### sub page #####

def calc():
    
    st.header('濃度計算')
    
    concentration_mM = st.number_input(
        '作りたい溶液の濃度(mM)',
        min_value=0, value=5, step=1
    )
    
    Mw = st.number_input(
        '使う溶質の分子量(g/mol)',
        min_value=0, value=313, step=1
    )
    
    solution_mL = st.number_input(
        '作りたい溶液の体積(mL)',
        min_value=0, value=100, step=100
    )

    concentration_g = mM2g(concentration_mM, Mw, solution_mL)
    
    st.metric(
        label="必要な溶質の質量",
        value=f'{round(concentration_g, 4)} g'
    )
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric(
        label="溶液の濃度",
        value=f'{round(concentration_mM, 1)} mM'
    )
    
    col2.metric(
        label="溶質の分子量",
        value=f'{round(Mw, 4)} g/mol'
    )
    
    col3.metric(
        label="溶液の体積",
        value=f'{round(solution_mL, 0)} mL'
    )
    
    st.write('ある濃度の溶液をつくるのに必要な溶質の質量を計算できます。')

    
def man_streamlit():
    st.header('Streamlit')
    st.write('StreamlitでWeb app.を運用する上で必要なコマンドなど')
    
    st.subheader('git/github')
    st.code('git add .')
    st.code('git commit -m "commit changes"')
    st.code('git push origin main')
    
    st.subheader('Streamlit')
    st.code('streamlit run app.py')
    

    
##### main page #####

st.title('Lab Tools')

page = st.multiselect(
     label = 'Page Select',
     options = ['濃度計算', 'Streamlit'],
     default = ['濃度計算'])


if '濃度計算' in page:
    calc()

if 'Streamlit' in page:
    man_streamlit()
    
