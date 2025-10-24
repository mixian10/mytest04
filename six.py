import streamlit as st

st.set_page_config(page_title='视频网站', page_icon='📼')

videos = [
    {'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/81/86/348538681/348538681-1-208.mp4?e=ig8euxZM2rNcNbhBhbdVhwdlhzUghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&mid=0&trid=d61614b16674495597eb9bec80090c5h&gen=playurlv3&deadline=1761303370&platform=html5&oi=771356656&nbs=1&os=cosovbv&og=cos&upsig=d555a328b76969aaf6981f0fb12b89dd&uparams=e,uipk,mid,trid,gen,deadline,platform,oi,nbs,os,og&bvc=vod&nettype=0&bw=2822937&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
     'title':'周杰伦《一路向北》万人大合唱现场！我一路向北~',
     'episod':'1'},
    {'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/98/83/319538398/319538398_da2-1-192.mp4?e=ig8euxZM2rNcNbRBhwdVhwdlhWUVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=771356656&trid=4930f2fca2084e5c8904d68231ce9cch&mid=0&deadline=1761302977&nbs=1&os=cosovbv&og=cos&platform=html5&uipk=5&gen=playurlv3&upsig=c53b39792489bd2ce4d4a15d34095890&uparams=e,oi,trid,mid,deadline,nbs,os,og,platform,uipk,gen&bvc=vod&nettype=0&bw=1206716&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
     'title':'周杰伦《暗号》神级现场',
     'episod':'2'},
    {'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/75/07/221860775/221860775-1-208.mp4?e=ig8euxZM2rNcNbKV7bdVhwdl7wdjhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761303239&trid=4ece422eaccc4380b91dc0f13130026h&nbs=1&og=hw&platform=html5&mid=0&gen=playurlv3&os=cosovbv&oi=771356656&uipk=5&upsig=d47d338db8eac1d1c642188d900e250e&uparams=e,deadline,trid,nbs,og,platform,mid,gen,os,oi,uipk&bvc=vod&nettype=0&bw=3258016&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
     'title':'周董《轨迹》最好听的版本！无与伦比演唱会',
     'episod':'3'}
]

if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.title(videos[st.session_state['ind']]['title'])
st.video(videos[st.session_state['ind']]['url'])

c1,c2,c3=st.columns(3)

def play(arg):
    #点击哪个按钮，就播放第几集
    
    st.session_state['ind'] = int(arg)
for i in range(len(videos)):
    st.button('第' + str(i+1) + '集', use_container_width=True,on_click=play,args=([i]))





