import streamlit as st
#日期选择组件
from datetime import datetime, time


st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")
c1,c2 = st.columns([1,2])
st.title('❇️个人简历生成器')
st.text('使用streamlit创建您的个性化简历')
c1,c2 = st.columns([1,2])
with c1:
    st.header('个人信息表')
    st.markdown('***')

    name = st.text_input('姓名', autocomplete='name')
    position = st.text_input('职位',autocomplete='position')
    
    number = st.text_input('电话', autocomplete='number')
    email = st.text_input('邮箱', autocomplete='email')
    
    date = st.date_input('出生日期', value=None)


    st.write('性别')
    sex = st.radio(
        '性别',
        ['男', '女', '其他'],
        horizontal=True,
        label_visibility='hidden')

    st.text('学历')
    degress = st.selectbox(
        '学历',
        ['高中', '专科', '本科', '硕士', '博士'],
        label_visibility='collapsed')

    language = st.multiselect(
        '语言能力',
        ['中文', '英文', '德语', '法语', '泰语'],
    
        max_selections=5)

    skill = st.multiselect(
        '技能(可多选)',
        ['Python', 'Java', 'JavaScript', 'SQL', 'HTML/CSS','数据分析','机器学习'],
    
        max_selections=7)
    
    experience = st.slider('工作经验(年)', 0, 30)
    
    income = st.slider(
    '期望薪资',
    3000, 20000, (3000, 9000))

    
    profile = st.text_area(label='个人简介', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')

    
    connect_time = st.time_input('最佳联系时间段')

    photo = st.file_uploader('上传个人照片')
    if photo is not None:
        bytes_data=photo.getvalue() 


with c2:
    st.header('简历实时预览')
    st.markdown('***')
    a1,a2 = st.columns(2)
    with a1:
        if photo:
            st.image(photo,width=300)
        
        st.write('职位：',position)
        st.write('电话：',number)
        st.write('邮箱：',email)
        st.write('出生日期：',date)
        st.write('语言能力：',language)
        s=''
        for i in language:
            s = s + i

    with a2:
        st.write('性别：',sex)
        st.write('学历：',degress)
        st.write('工作经验：',experience)
        st.write('期望薪资范围：',income)
        st.write('最佳联系时间：',connect_time)
    st.markdown('***')
    st.subheader('个人简介')
    st.write(profile)
    st.subheader('专业技能')
    st.write(skill)
    




