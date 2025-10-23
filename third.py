import streamlit as st

st.set_page_config(page_title='大自然',page_icon='🏕')

images = [
    {'url':'https://img1.qunarzz.com/travel/d3/1704/46/6f7a532439a36ab5.jpg',
     'parm': '海🌊'},
    {'url':'https://www.urlaubsguru.de/wp-content/uploads/2015/08/jiuzhaigou-national-park-istock-503099215-2.jpg',
     'parm':'九寨沟'},
    {'url':'https://www.2008php.com/2023_Website_appreciate/2023-04-19/20230419114731xneJy3gxiao.jpg',
     'parm':'冰岛极光'}
    ]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
    



def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
    


    
st.image(images[ st.session_state['ind']]['url'],caption=images[ st.session_state['ind']]['parm'])
#将一列分成两行
a1,a2 = st.columns(2)
def lastImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)
with a1:

    st.button('上一张', on_click=lastImg)

with a2:

    st.button('下一张', on_click=nextImg)

