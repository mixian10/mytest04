import streamlit as st

st.set_page_config(page_title='音频',page_icon='🎶')
st.title('🎶简易音乐播放器')
st.text('使用Sreamlit制作的简单音乐播放器，支持切歌和基本播放控制')

images = [
    {'url':'https://music.163.com/song/media/outer/url?id=488483381.mp3',
     'photo':'https://p2.music.126.net/QxMru_dhWDJhSwIWaSQZwg==/18351948579960531.jpg?param=500y500',
     'name':'到时说爱我',
     'singer':'歌手:茜拉',
     '时长':'时长:3:23'},
    
    {'url':'https://music.163.com/song/media/outer/url?id=30039341.mp3',
     'photo':'https://p2.music.126.net/FtAvIYLF3qwqohQhwycVDg==/109951171386379124.jpg?param=500y500',
     'name':'特别的人',
     'singer':'歌手:方大同',
     '时长':'时长:4:01'},
    
    {'url':'https://music.163.com/song/media/outer/url?id=420401511.mp3',
     'photo':'https://p1.music.126.net/O6d7GYY3gp2uy8zehvcOjQ==/17699938184267410.jpg?param=500y500',
     'name':'和你',
     'singer':'歌手:余佳运',
     '时长':'时长:3:20'},
    {'url':'https://music.163.com/song/media/outer/url?id=1493976789.mp3',
     'photo':'https://p1.music.126.net/Ym3N-yC83r8l0Sf6ht5qIA==/109951165454950112.jpg?param=500y500',
     'name':'My love',
     'singer':'歌手:颜人中',
     '时长':'时长:3:14'}
    ]


if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
    

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
#将一列分成两行    
a1,a2 = st.columns([1,2])
with a1:
    st.image(images[ st.session_state['ind']]['photo'])

with a2:
    st.subheader(images[ st.session_state['ind']]['name'])
    st.text(images[ st.session_state['ind']]['singer'])
    st.text(images[ st.session_state['ind']]['时长'])
    st.audio(images[ st.session_state['ind']]['url'])

    
#将一列分成两行
c1,c2 = st.columns(2)
def lastImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)
with c1:

    st.button('⏮上一首', on_click=lastImg,use_container_width=True)

with c2:

    st.button('⏭下一首', on_click=nextImg,use_container_width=True)

